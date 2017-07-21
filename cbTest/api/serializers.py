'''
Created on 20-07-2017

@author: pablo
'''
from rest_framework import serializers
from .models import Address
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='address_list')
    class Meta:
        model = Address
        fields = ('id', 'address', 'latitude', 'longitude', 'elevation')
        
class AddressLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='addres_detail')
    class Meta:
        model = Address
        fields = ('url','id', 'address', 'latitude', 'longitude', 'elevation')