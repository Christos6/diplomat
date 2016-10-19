from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from social.apps.django_app.default.models import UserSocialAuth
from django.db.models import signals
from activitytracker.models import User
import math


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=200)
    activity_description = models.CharField(max_length=500,default="")
    icon = models.CharField(max_length=500,default="")
    def __str__(self):              # __unicode__ on Python 2
        return '%s' %  self.activity_name

class Frenemy(models.Model):
    Frenemy_id = models.AutoField(primary_key=True)
    Frenemy_name = models.CharField(max_length=100)
    Frenemy_of_user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return '%s' % self.friend_name

class Thing(models.Model):
    thing_name = models.CharField(max_length=100)
    thing_id = models.AutoField(primary_key=True)
    thing_of_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __str__(self):
        return '%s' % self.object_name

class acts(models.Model):
    man = models.ForeignKey(settings.AUTH_USER_MODEL)
    activitay = models.ForeignKey(Activity, db_column="Activity_key")
    withusing = models.ManyToManyField(Thing)
    acts_id = models.AutoField(primary_key=True)
    acts_goal = models.CharField(max_length=200)
    status_choices = (
        ('Reached','Reached'),
        ('Inprogress','In progress'),
        ('Failed', 'Failed'),
    )
    acts_goal_status = models.CharField(max_length=20,choices=status_choices,null=True)
    astart_date = models.DateTimeField('Start time')
    aend_date = models.DateTimeField('End time')
    def __str__(self):              # __unicode__ on Python 2
        return '%s %s %s %s' % (self.activity, self.start_date, self.end_date, str(self.utc_offset))
    def aduration(self):
        d = self.end_date - self.start_date
        days, seconds = d.days, d.seconds
        hours = seconds/3600
        minutes = int(math.ceil((seconds - hours*3600)/60.0))
        return [days, hours, minutes]












