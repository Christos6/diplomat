from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save

from activitytracker.models import User
from ct_projects.models import Campaign
from profile.lists import BUSINESS_SECTORS, WORK_POSITIONS, INFLUENCES, DEVICES, PLATFORMS, BRAND_OPINIONS, \
    TECH_LEVELS

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class UserProfile(models.Model):
    """
    Additional information about CloudTeams customer account
    Initially will be filled in using the wizard
    """

    # Link to user in Activity Tracker
    user = models.OneToOneField(User)

    # Avatar
    profile_picture = models.ImageField(upload_to='avatars/', blank=True, null=True, default=None)

    # Generic info
    first_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    last_name_initial = models.CharField(max_length=1, blank=True, null=True, default=None)
    year_of_birth = models.IntegerField(blank=True, null=True, default=None, validators=[MinValueValidator(1930),
                                                                                         MaxValueValidator(2010)])
    # -- location is in main model -> asume it to be home location

    # Business info
    business_sector = models.CharField(max_length=127, blank=True, default='', choices=BUSINESS_SECTORS)
    work_position = models.CharField(max_length=127, blank=True, default='', choices=WORK_POSITIONS)
    work_location = models.CharField(max_length=255, blank=True, default='')
    years_experience = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    # Tech level
    tech_level = models.CharField(max_length=31, blank=True, default='', choices=TECH_LEVELS)

    # Check if the profile wizard has run at least once
    has_been_saved = models.BooleanField(default=False, editable=False)

    def get_display_name(self):
        return '%s %s.' % (self.first_name, self.last_name_initial)

    def get_display_name(self):
        if self.first_name and self.last_name_initial:
            return '%s %s.' % (self.first_name, self.last_name_initial)
        else:
            return self.user.username

    def get_completion_progress(self):
        """
        :return: A two digit percentage ("00" - "99") indicating how much of the profile info has been completed
        """
        # TODO implement profile complete calculation logic
        points = 0

        if self.profile_picture:
            points += 5

        if self.first_name:
            points += 4

        if self.last_name_initial:
            points += 1

        if self.year_of_birth:
            points += 5

        if self.business_sector:
            points += 3

        if self.work_location:
            points += 5

        if self.years_experience:
            points += 2

        if self.tech_level:
            points += 10

        if self.user.influences.all():
            points += 15

        if self.user.devices.all():
            points += 20

        if self.user.platforms.all():
            points += 20

        if self.user.brand_opinions.all():
            points += 10

        return points

    def avatar(self):
        if not self.profile_picture:
            return None
        else:
            return '/media/avatars/' + self.profile_picture.name.split('/')[-1]


class Influence(models.Model):
    user = models.ForeignKey(User, related_name='influences')
    influence = models.CharField(max_length=255, choices=INFLUENCES)


class DeviceUsage(models.Model):
    user = models.ForeignKey(User, related_name='devices')
    device = models.CharField(max_length=255, choices=DEVICES)


class PlatformUsage(models.Model):
    user = models.ForeignKey(User, related_name='platforms')
    platform = models.CharField(max_length=255, choices=PLATFORMS)


class UserBrandOpinion(models.Model):
    user = models.ForeignKey(User, related_name='brand_opinions')
    brand = models.CharField(max_length=16)
    opinion = models.CharField(max_length=1, choices=BRAND_OPINIONS)


def on_profile_info_updated(sender, instance, created, **kwargs):
    # send campaigns
    Campaign.send_all()


# connect with update events
post_save.connect(on_profile_info_updated, sender=UserProfile)
post_save.connect(on_profile_info_updated, sender=Influence)
post_save.connect(on_profile_info_updated, sender=DeviceUsage)
post_save.connect(on_profile_info_updated, sender=PlatformUsage)
post_save.connect(on_profile_info_updated, sender=UserBrandOpinion)
