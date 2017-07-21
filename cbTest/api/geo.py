'''
Created on 20-07-2017

@author: pablo
'''
# -*- coding: utf-8-*-
import requests
#Url to get an elevation from a specific latitude and longitude
ELEVATION_BASE_URL = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
#Url to get the latitude and longitude from an address
GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='


#Get elevation from a latitude and longitude point
def getElevation(lat,lon):
    url = ELEVATION_BASE_URL + str(lat) + ',' + str(lon)
    r = requests.get(url)
    if(r.json()["status"]=="OK"):
        return r.json()["results"][0]["elevation"]
    
    
#Get Latitude and Longitude from an Address, just taking the "best match" given by the Google Maps API
def getAddressData(address):
    url = GEOCODE_BASE_URL + address
    r = requests.get(url)
    if(r.json()["status"]=="OK"):
        return r.json()["results"][0]["geometry"]["location"]["lat"],r.json()["results"][0]["geometry"]["location"]["lng"]
    return None,None


    
