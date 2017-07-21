'''
Created on 20-07-2017

@author: pablo
'''
from django.conf.urls import url
from api import views
urlpatterns = [
    url(r'^api/$', views.AddressApi.as_view(),name="address_list"), #Url to get all the addresses and register a new one
    url(r'^api/(?P<pk>[0-9]+)/?$', views.AddressDetail.as_view(),name="addres_detail"), #Url to get one specific address
]