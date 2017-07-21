# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
Based on http://levipy.com/crear-api-rest-con-django-rest-framework/

'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import Address
from serializers import AddressSerializer
import geo

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def address_list(request):
    """
    List all coded addresses, or register a new address.
    """
    if request.method == 'GET':
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        lat,lon = geo.getAddressData(data["address"])
        if lat == None or lon == None:
            return JSONResponse(serializer.errors, status=404)
        data["latitude"] = round(lat,8)
        data["longitude"] = round(lon,8)
        elevation = geo.getElevation(lat, lon)
        if elevation == None:
            return JSONResponse(serializer.errors, status=404)
        data["elevation"] = round(elevation,2)

        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    
@csrf_exempt
def address_detail(request, pk):
    """
    Retrieve one address by the id specified in the url
    """
    try:
        address = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AddressSerializer(address)
        return JSONResponse(serializer.data)
