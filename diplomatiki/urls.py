from django.conf.urls import *
from diplomatiki import views as diplomatiki_views

urlpatterns = [
    url(r'^index/$', diplomatiki_views.index, name='index')
]