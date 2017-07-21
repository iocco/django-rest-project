# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
Based on http://levipy.com/crear-api-rest-con-django-rest-framework/

'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from api.models import Address
from api.serializers import AddressSerializer
from api.serializers import AddressLinkSerializer
from api import geo

        
class AddressApi(APIView):
    """
    List all coded addresses, or register a new address.
    """
    def get(self, request, format=None):
        addresses = Address.objects.all()
        serializer = AddressLinkSerializer(addresses, context={'request': request},many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        lat,lon = geo.getAddressData(data["address"])
        if lat == None or lon == None:
            return Response(serializer.errors, status=404)
        data["latitude"] = round(lat,8)
        data["longitude"] = round(lon,8)
        elevation = geo.getElevation(lat, lon)
        if elevation == None:
            return Response(serializer.errors, status=404)
        data["elevation"] = round(elevation,2)

        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class AddressDetail(APIView):
    """
    Retrieve one address by the id specified in the url
    """
    def get(self, request, pk, format=None):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return HttpResponse(status=404)
        serializer = AddressSerializer(address,context={'request': request})
        return Response(serializer.data)
