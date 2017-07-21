# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
'''Model for db of an Address '''
class Address(models.Model):
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(decimal_places=8, max_digits=11)
    longitude = models.DecimalField(decimal_places=8, max_digits=11)
    elevation = models.DecimalField(decimal_places=3, max_digits=10)
