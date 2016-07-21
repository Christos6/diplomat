from django.shortcuts import render
from activitytracker.models import *

def index(request):
    return render(request, 'diplomatiki/index.html', {
        'objects': User.objects.all()
    })