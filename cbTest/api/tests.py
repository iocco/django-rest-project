# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import requests

# Create your tests here.
class UrlTestCase(TestCase):
    baseUrl = "localhost:8000/"
    def createUrl(self):
        postData = {"address='Libertad 835'"}

        create = requests.post(baseUrl+'api/',params = postData)
        self.assertEqual(create.status_code, 201)
    def getAddresses(self):
        r = requests.get(baseUrl+'api/')
        self.assertEqual(r.status_code, 200)
        