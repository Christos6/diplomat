from django import forms
from activitytracker.models import User as ActUser
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = ActUser
        fields = ("username",)