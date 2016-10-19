from django.contrib import auth
from django.core.context_processors import csrf
from django.http import *
from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from activitytracker.models import User
from activitytracker.models import Activity
from activitytracker.models import Performs
from diplomatiki.forms import MyRegistrationForm
import json




def start(request):
    return render_to_response('diplomatiki/start.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('diplomatiki/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/diplomatiki/loggedin')
    else:
        return HttpResponseRedirect('/diplomatiki/invalid')


def loggedin(request):
    return render_to_response('diplomatiki/loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('diplomatiki/invalid_login.html')

def compare(request):
    return render_to_response("diplomatiki/compare.html")


def logout(request):
    auth.logout(request)
    return render_to_response('diplomatiki/logout.html')


def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/diplomatiki/register_success')

    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('diplomatiki/register.html', args)


def register_success(request):
    return render_to_response('diplomatiki/register_success.html')

def settings(request):
    return render_to_response('diplomatiki/settings.html')

def index(request):
    all_activities = Activity.objects.all()
    context = {'all_activities':all_activities}
    return render(request,"diplomatiki/index.html",context)

def detail(request, pk):
    activity = get_object_or_404(Activity , pk=pk)
    return render(request, "diplomatiki/detail.html", {'activity': activity})

def userindex(request):
    all_users = User.objects.all()
    all_performs = Performs.objects.all()
    context = {'all_users':all_users,'all_performs':all_performs}
    return render(request, "diplomatiki/userindex.html",context)

def userdetail(request, pk):
    user = get_object_or_404(User , pk=pk)
    return render(request, "diplomatiki/userdetail.html", {'user': user})

def christosactivities(request):
    with open('diplomatiki/JsonFiles/christosactivities.json') as data_file:
        data = json.load(data_file)

    return render_to_response('diplomatiki/christosactivities.html', {'data': data})

def iosifactivities(request):
    with open('diplomatiki/JsonFiles/iosifactivities.json') as data_file:
        data = json.load(data_file)

    return render_to_response('diplomatiki/iosifactivities.html', {'data': data})

def hasactivity(request):
    with open('diplomatiki/JsonFiles/useractivities.json') as data_file:
        data = json.load(data_file)

    return render_to_response('diplomatiki/hasactivity.html', {'data': data})

def commonnactivities(request):
    with open('diplomatiki/JsonFiles/commonactivities.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/commonactivities.html', {'data': data})

def compare2(request):
    with open('diplomatiki/JsonFiles/compare2.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/compare2.html', {'data': data})

def allactivityentries(request):
    with open('diplomatiki/JsonFiles/allactivityentries.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/allactivityentries.html', {'data': data})

def runningentries(request):
    with open('diplomatiki/JsonFiles/runningentries.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/runningentries.html', {'data': data})

def socialmediaentries(request):
    with open('diplomatiki/JsonFiles/socialmediaentries.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/socialmediaentries.html', {'data': data})

def statusupdateentries(request):
    with open('diplomatiki/JsonFiles/statusupdateentries.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/statusupdateentries.html', {'data': data})

def runningfrequency(request):
    with open('diplomatiki/JsonFiles/runningfrequency.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/runningfrequency.html', {'data': data})

def socialmediafrequency(request):
    with open('diplomatiki/JsonFiles/socialmediafrequency.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/socialmediafrequency.html', {'data': data})

def statusupdatefrequency(request):
    with open('diplomatiki/JsonFiles/statusupdatefrequency.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/statusupdatefrequency.html', {'data': data})

def runningmeantime(request):
    with open('diplomatiki/JsonFiles/runningmeantime.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/runningmeantime.html', {'data': data})

def socialmediameantime(request):
    with open('diplomatiki/JsonFiles/socialmediameantime.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/socialmediameantime.html', {'data': data})

def statusupdatemeantime(request):
    with open('diplomatiki/JsonFiles/statusupdatemeantime.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/statusupdatemeantime.html', {'data': data})

def comparerunning(request):
    with open('diplomatiki/JsonFiles/compareandjudgerunning.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/comparerunning.html', {'data': data})

def comparesocialmedia(request):
    with open('diplomatiki/JsonFiles/comparesocialmedia.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/comparesocialmedia.html', {'data': data})

def comparestatusupdate(request):
    with open('diplomatiki/JsonFiles/comparestatusupdate.json') as data_file:
        data = json.load(data_file)
    return render_to_response('diplomatiki/comparestatusupdate.html', {'data': data})

def semanticusers(request):
    return render_to_response('diplomatiki/semanticusers.html')













