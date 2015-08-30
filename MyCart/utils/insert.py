import os
import sys
import requests
import json
import urllib2
from django.db import IntegrityError
from ..models import ProductCatalog


# reads in plain text file and imports data into database
def insert_data(overwrite=False, verbosity=1):

    # fp = open( r"C:\SEQUOIA2015\mycart\test.json",'r')
    # json_data = json.load(fp)
    # fp.close()

    json_data = json.load(urllib2.urlopen("http://54.157.29.215:8080/mykart-api/product/list"))

    # {u'categoryname': u'grains', u'id': 177, u'name': u'Channa Dal'}
    for each in json_data:
        try:
            obj, created = ProductCatalog.objects.get_or_create(product_id=each['id'], product_name=each['name'], product_category=each['categoryname'])

        except IntegrityError as e:
            print e.message