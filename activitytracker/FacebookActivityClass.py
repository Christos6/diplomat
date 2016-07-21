from myfunctions import *
from AuthorizationChecks import *
from django.db import transaction

class FacebookActivity(OAuth2Validation):

    def __init__(self, user_social_instance):
        super(FacebookActivity, self).__init__(user_social_instance)
        self.api_user_timeline_url = 'https://graph.facebook.com/v2.4/me/posts'

    # Fetch Full Name & Timezone of user.
    def fetchUserExtraData(self, token):

        api_url = 'https://graph.facebook.com/v2.4/me'
        params = {
            'access_token': token,
            'fields': 'timezone,name'
        }

        r = requests.get(url=api_url, params=params).json()

        if ('timezone' or 'name') not in r:
            return r['name'], 0

        return r['name'], int(r['timezone'])

    @transaction.atomic()
    def _insertMedia(self, feed, user_fullname, utc_offset):

        _max_id = 0
        _time_barrier = datetime.strptime(EARLIEST_DATA_DATE + ' 00:00:00', "%Y-%m-%d %H:%M:%S")

        for media in feed:

            time_posted = datetime.strptime(media['created_time'], '%Y-%m-%dT%H:%M:%S+0000')

            if time_posted < _time_barrier:
                return _max_id, 'Reached Barrier'

            if media['type'] == "status":
                activity_performed = Activity.objects.get(activity_name="Status Update")

            elif media['type'] == "photo" and media['status_type'] == 'added_photos':
                activity_performed = Activity.objects.get(activity_name="Image Upload")

            elif media['type'] == "video" and media['status_type'] == 'added_video':
                activity_performed = Activity.objects.get(activity_name="Video Upload")

            else:
                activity_performed = Activity.objects.get(activity_name="Share / Retweet")

            # IMPORTANT: Only counting comments on the original post.
            # Not comment-replies to other comments of the post
            result = 'Your post has been liked by %s and commented by %s people' % (
                media['likes']['summary']['total_count'],
                media['comments']['summary']['total_count']
            )

            if 'place' in media:
                if 'location' in media['place']:
                    location_address = media['place']['location']['street']
                    location_lat = media['place']['location']['latitude']
                    location_lng = media['place']['location']['longitude']
                else:
                    location = Geocoder.geocode(media['place']['name'])
                    location_address = media['place']['name']
                    location_lat = location.latitude
                    location_lng = location.longitude
            else:
                location_lat, location_lng, location_address = None, None, ''

            object_used = 'Facebook'
            object_used += ',Smartphone' if media['status_type'] == 'mobile_status_update' else ''

            goal = ''
            goal_status = None

            start_date = time_posted - timedelta(seconds=60) + timedelta(hours=utc_offset)
            end_date = time_posted + timedelta(hours=utc_offset)

            tags = list()

            if 'story_tags' in media:
                for key, tag_list in media['story_tags'].iteritems():
                    for tag in tag_list:
                        tags.append(tag['name'])

            if 'with_tags' in media:
                for key, tag_list in media['with_tags'].iteritems():
                    for tag in tag_list:
                        tags.append(tag['name'])

            tags = list(set(tags))
            tags.remove('') if '' in tags else True
            tags.remove(user_fullname) if user_fullname in tags else True

            friends = ','.join(tags)

            performs_instance = addActivityFromProvider(user=self.user,
                                                        activity=activity_performed,
                                                        friends=friends,
                                                        goal=goal, goal_status=goal_status,
                                                        location_address=location_address,
                                                        location_lat=location_lat,
                                                        location_lng=location_lng,
                                                        start_date=start_date,
                                                        end_date=end_date,
                                                        result=result,
                                                        objects=object_used,
                                                        utc_offset=utc_offset
                                                        )
            # To be confirmed
            if media['id'] > self.metadata.since_id:
                self.metadata.since_id = media['id']

            # To be fixed
            if (_max_id > media['id']) or (_max_id == 0):
                _max_id = media['id']

            media_url = 'https://www.facebook.com/' + media['id']
            createActivityLinks(provider=self.PROVIDER.lower(),
                                instance=performs_instance,
                                provider_instance_id=str(media['id']),
                                url=media_url
                                )

        return _max_id, 'Ok'

    def fetchData(self):

        if self.validate() != 'Authentication Successful':
            return HttpResponseBadRequest(ERROR_MESSAGE)

        params = {'access_token': self.provider_data['access_token'],
                  'fields': 'created_time,type,status_type,place,likes.summary(true),comments.summary(true),story_tags,with_tags'
        }

        if self.metadata.last_updated != DUMMY_LAST_UPDATED_INIT_VALUE:
            params['since'] = time.mktime(datetime.strptime(
                                self.metadata.last_updated,
                                "%Y-%m-%d %H:%M:%S"
                              ).timetuple())

        last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        response = requests.get(url=self.api_user_timeline_url, params=params).json()

        user_fullname, utc_offset = self.fetchUserExtraData(self.provider_data['access_token'])

        while True:

            feed = response['data']

            if not feed:
                break

            if 'error' in response:
                return HttpResponse(ERROR_MESSAGE)

            _ , status = self._insertMedia(feed, user_fullname, utc_offset)

            if status == "Barrier Reached":
                break

            response = requests.get(url=response['paging']['next']).json()

        self.metadata.last_updated = last_updated
        self.metadata.save()

        # I still need to get the checkins, both personal and from other people.
        return HttpResponse(self.PROVIDER.capitalize() + SUCCESS_MESSAGE)
