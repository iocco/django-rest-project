'''
Created on 20-07-2017

@author: pablo
'''
from rest_framework import serializers
from .models import Address
class AddressSerializer(serializers.HyperlinkedModelSerializer):
       class Meta:
        model = Address
        fields = ('id', 'address', 'latitude', 'longitude', 'elevation')