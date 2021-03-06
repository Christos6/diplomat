from django.conf.urls import *
from activitytracker import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^terms_and_conditions/$', views.terms_and_conditions, name='terms_and_conditions'),
    url(r'^social_login/(?P<action>.+)/$', views.social_login, name='social-login'),
    url(r'^account/passforgot/$', views.passwordforget, name='passwordforget'),
    url(r'^account/verification/(?P<verification_token>\w+)/$', views.email_verification, name='emailVerification'),
    url(r'^account/password_reset/(?P<passwordreset_token>\w+)/$', views.password_reset, name='passwordReset'),
    url(r'^account/register/$', views.register, name='register'),
    url(r'^account/routine(?:/(?P<setting>\w+))?/$', views.routineSettings, name='routineSettings'),
    url(r'^account/delete/$', views.delete_account, name='delete-account'),
    url(r'^activity/add/$', views.addactivity, name='addactivity'),
    url(r'^activity/display-activity/(?P<performs_identification>[0-9]+)/$', views.showactivity, name='showactivity'),
    url(r'^activity/display-group-activity/(?P<group_identification>[0-9_]+)/$', views.showgroupactivity, name='showGroupactivity'),
    url(r'^activity/(?P<performs_id>[0-9]+)/$', views.activitydetails, name='activitydetails'),
    url(r'^activity/delete-activity/(?P<performs_id>[0-9]+)/$', views.deleteactivity, name='deleteactivity'),
    url(r'^activity/edit-activity/(?P<performs_id>[0-9]+)/$', views.editactivity, name='editactivity'),
    url(r'^activity/update-activity/(?P<performs_id>[0-9]+)/$', views.updateactivity, name='updateactivity'),
    url(r'^activity/listallactivities/$', views.listallactivities, name='listallactivities'),
    url(r'^configuration/$', views.configuration, name='configuration'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index/eventstojson/$', views.eventstojson, name='json-events'),
    url(r'^index/chartdatajson/$', views.chartdatajson, name='chartdatajson'),
    url(r'^index/displayperiod/$', views.displayperiod, name='displayPeriod'),
    url(r'^index/fetch_tokenfield_values/$', views.fetch_tokenfield_values, name='fetchTokenfieldValues'),
    url(r'^index/getgroupedactivities/$', views.getgroupedactivities, name='getgroupedactivities'),
    url(r'^index/(?P<new_user>\w+)/$', views.index, name='index'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/places/$', views.places, name='places'),
    url(r'^settings/placestojson/$', views.placestojson, name='placestojson'),
    url(r'^settings/sync/(?P<provider>[-\w]+)/$', views.syncProviderActivities, name='syncProviderActivities'),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^goals/goalstojson/$', views.goalstojson, name='goalstojson'),
    url(r'^goals/goalhandler/$', views.goalhandler, name='goalhandler'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^timelinejson/$', views.timeline_events_json, name='timelineEventsJson'),
    url(r'^analytics/activities/$', views.analytics_activities, name='analytics-activities'),
    url(r'^analytics/friends/$', views.analytics_friends, name='analytics-friends'),
    url(r'^analytics/goals/$', views.analytics_goals, name='analytics-goals'),
    url(r'^analytics/places/$', views.analytics_places, name='analytics-places'),
    url(r'^analytics/objects/$', views.analytics_objects, name='analytics-objects'),
    url(r'^analytics/routine/$', views.analytics_routine, name='analytics-routine'),
    url(r'^analytics/friends/update/activities_friend/$', views.updateonefriendmanyactivitiescharts, name='updateOneFriendManyActivitiesCharts'),
    url(r'^analytics/friends/update/activity_friends/$', views.updateoneactivitymanyfriendscharts, name='updateOneActivityManyFriendsCharts'),
    url(r'^analytics/friends/update/activity_friend/$', views.updateoneactivityonefriendchart, name='updateOneActivityOneFriendChart'),
    url(r'^analytics/friends/update/activities_friends/$', views.updatemanyactivitiesmanyfriendschart, name='updateManyActivitiesManyFriendsChart'),
    url(r'^analytics/friends/update/friends_chartbanner/$', views.updatefriendsbanner, name='updateFriendsBanner'),
    url(r'^analytics/objects/update/activities_object/$', views.updateoneobjectmanyactivitiescharts, name='updateOneObjectManyActivitiesCharts'),
    url(r'^analytics/objects/update/activity_objects/$', views.updateoneactivitymanyobjectscharts, name='updateOneActivityManyObjectsCharts'),
    url(r'^analytics/objects/update/activity_object/$', views.updateoneactivityoneobjectchart, name='updateOneActivityOneObjectChart'),
    url(r'^analytics/objects/update/activities_objects/$', views.updatemanyactivitiesmanyobjectschart, name='updateManyActivitiesManyObjectsChart'),
    url(r'^analytics/objects/update/objects_chartbanner/$', views.updateobjectsbanner, name='updateObjectsBanner'),
    url(r'^analytics/goals/update/activity/$', views.updateactivitydonutchart, name='updateActivityDonutChart'),
    url(r'^analytics/goals/update/categories_activities/$', views.updateactivityandcategorybarchart, name='updateActivityAndCategoryBarChart'),
    url(r'^analytics/goals/update/activities_objects/$', views.updateactivityandobjectbubblechart, name='updateActivityAndObjectBubbleChart'),
    url(r'^analytics/goals/update/activities_friends/$', views.updateactivitysandfriendbubblechart, name='updateActivityAndFriendBubbleChart'),
    url(r'^analytics/goals/update/goals_chartbanner/$', views.updategoalsbanner, name='updateGoalsBanner'),
    url(r'^analytics/places/update/categories_activities/$', views.updateactivitiesinplacedonutchart, name='updateActivitiesInPlaceDonutChart'),
    url(r'^analytics/places/update/places_all/$', views.updateallplacesbarchart, name='updateAllPlacesBarChart'),
    url(r'^analytics/places/update/places_chartbanner/$', views.updateplacesbanner, name='updatePlacesBanner'),
    url(r'^analytics/activities/update/activities_all/$', views.updateallactivitiescharts, name='updateAllActivitiesCharts'),
    url(r'^analytics/activities/update/activities_single/$', views.updatesingleactivitycharts, name='updateSingleActivityCharts'),
    url(r'^analytics/activities/update/activities_chartbanner/$', views.updateactivitiesbanner, name='updateActivitiesBanner'),
    url(r'^analytics/routine/update/activities_all/$', views.updateallroutinecharts, name='updateAllRoutineCharts'),
]