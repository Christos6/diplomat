from django.conf.urls import *
from diplomatiki import views as diplomatiki_views

app_name = 'diplomatiki'

urlpatterns = [
    #url(r'^index/$', diplomatiki_views.index, name='index'),
    url(r'^start/$', diplomatiki_views.start, name='start'),
    url(r'^register/$', diplomatiki_views.register, name='register'),
    url(r'^register_success/$', diplomatiki_views.register_success, name='register_success' ),
    url(r'^login/$', diplomatiki_views.login, name='login'),
    url(r'^auth/$',  diplomatiki_views.auth_view, name='auth'),
    url(r'^logout/$', diplomatiki_views.logout, name='logout'),
    url(r'^loggedin/$', diplomatiki_views.loggedin, name='loggedin'),
    url(r'^invalid/$', diplomatiki_views.invalid_login, name='invalid'),
    url(r'^settings/$', diplomatiki_views.settings, name='settings'),
    url(r'^index/$', diplomatiki_views.index, name='index'),
    url(r'^index/(?P<pk>[0-9]+)/$', diplomatiki_views.detail, name = 'detail'),
    url(r'^userindex/$',diplomatiki_views.userindex, name='userindex'),
    url(r'^userindex/(?P<pk>[0-9]+)/$', diplomatiki_views.userdetail, name = 'userdetail'),
    url(r'^compare/$', diplomatiki_views.compare, name='compare'),
    url(r'^hasactivity/$', diplomatiki_views.hasactivity, name='hasactivity'),
    url(r'^christosactivities/$', diplomatiki_views.christosactivities, name='christosactivities'),
    url(r'^iosifactivities/$', diplomatiki_views.iosifactivities, name='iosifactivities'),
    url(r'^commonactivities/$', diplomatiki_views.commonnactivities, name='commonactivities'),
    url(r'^compare2/$', diplomatiki_views.compare2, name='compare2'),
    url(r'^runningentries/$', diplomatiki_views.runningentries, name='runningentries'),
    url(r'^socialmediaentries/$', diplomatiki_views.socialmediaentries, name='socialmediaentries'),
    url(r'^statusupdateentries/$', diplomatiki_views.statusupdateentries, name='statusupdateentries'),
    url(r'^allactivityentries/$', diplomatiki_views.allactivityentries, name='allactivityentries'),
    url(r'^runningfrequency/$', diplomatiki_views.runningfrequency, name='runningfrequency'),
    url(r'^socialmediafrequency/$', diplomatiki_views.socialmediafrequency, name='socialmediafrequency'),
    url(r'^statusupdatefrequency/$', diplomatiki_views.statusupdatefrequency, name='statusupdatefrequency'),
    url(r'^runningmeantime/$', diplomatiki_views.runningmeantime, name='runningmeantime'),
    url(r'^socialmediameantime/$', diplomatiki_views.socialmediameantime, name='socialmediameantime'),
    url(r'^statusupdatemeantime/$', diplomatiki_views.statusupdatemeantime, name='statusupdatemeantime'),
    url(r'^comparerunning/$', diplomatiki_views.comparerunning, name='comparerunning'),
    url(r'^comparesocialmedia/$', diplomatiki_views.comparesocialmedia, name='comparesocialmedia'),
    url(r'^comparestatusupdate/$', diplomatiki_views.comparestatusupdate, name='comparestatusupdate'),
    url(r'^semanticusers/$', diplomatiki_views.semanticusers, name='semanticusers'),


]
