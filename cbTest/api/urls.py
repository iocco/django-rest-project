'''
Created on 20-07-2017

@author: pablo
'''
from django.conf.urls import url
from api import views
urlpatterns = [
    url(r'^api/$', views.address_list), #Url to get all the addresses and register a new one
    url(r'^api/(?P<pk>[0-9]+)/?$', views.address_detail), #Url to get one specific address
]