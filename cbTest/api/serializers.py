'''
Created on 20-07-2017

@author: pablo
'''
from rest_framework import serializers
from .models import Address
#Regular Serializer
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address', 'latitude', 'longitude', 'elevation')

#Serializer used to hyperlink an address
class AddressLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='addres_detail')
    class Meta:
        model = Address
        fields = ('url','id', 'address', 'latitude', 'longitude', 'elevation')