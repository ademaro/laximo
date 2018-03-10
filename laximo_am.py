#!/usr/bin/python3
# -*- coding: utf-8 -*-

from zeep import Client
import hashlib

def call_laximo_am_FindOEM(endpoint, login, password, brand, oem):
    
    client = Client('{}?wsdl'.format(endpoint[:len(endpoint)-1]))
    current_query = 'FindOEM:Locale=ru_RU|Brand={}|OEM={}|Options=crosses|ReplacementTypes=Replacement,Duplicate,Synonym,Bidirectional'.format(brand, oem)            
    key = '{}{}'.format(current_query, password)
    md5_key=hashlib.md5(key.encode('utf-8')).hexdigest()
    responce = ''
    responce = client.service.QueryDataLogin(current_query, login, md5_key)
    return responce 

endpoint = 'http://aws.laximo.net/ec.Kito.Aftermarket/services/Catalog.CatalogHttpSoap12Endpoint/'
login = "yourusername"
password = "yourpassword"
brand = "RVI"
oem = "5001837172"

responce = call_laximo_am_FindOEM(endpoint, login, password, brand, oem)
print(responce)