#!/usr/bin/python3

#from azure_client_factory import AzureClientFactory
#from azure_servicebus import *
#from azure.mgmt.servicebus.models import ErrorResponseException
import requests
import json
import sys
import subprocess
import shlex

# script's first argument, for example lab
#ENV = str(320749)
ENV = 'techops'
RES_GROUP = 'techops'
# example arguments as predefined variables
#ENV = 'lab'
#PARAM = '-n'
#GW = 'HTTPGateway'


NAMESPACE = 'sb-techops007'


KEY = 'Bearer '

URL = 'https://{}-api.ddm.iot-accelerator.ericsson.net/'.format(ENV)
print(URL)
filter = '?PageSize=1000'
header = {'Authorization':'{}'.format(KEY), 'Content-type': 'application/json'}
counter = 0


# GET device networks
API = 'api/v3/deviceNetworks'
r = requests.get(URL + API + filter, headers=header)
result = r.json()
#print(result)
print('%20s %20s %20s' %('Gateway Name', 'Location', 'Gateway ID'))
print('-'*65)

for item in result:
       DN_ID = item['Id']
       DN_NAME = item['Name']
       header = {'Authorization':'{}'.format(KEY), 'X-devicenetwork':'{}'.format(DN_ID), 'Content-type': 'application/json'}
       API = 'api/v3/datacollectors'
       r = requests.get(URL + API + filter, headers=header)
       DC_DICT = r.json()
#       print(DC_DICT)
       for dc in DC_DICT['Rows']:
               print('{!s:<25} {!s:<20} {!s:<40s}'.format(dc['Name'],dc['LocationName'],dc['Id']))
               myid = dc['Id']
               az_cli = ('az servicebus queue show --resource-group {} --namespace-name {} --name {} --query \"id\" -o tsv'.format(RES_GROUP,NAMESPACE,myid))
               subprocess_cmd = shlex.split(az_cli)
               subprocess.call(subprocess_cmd)
               print('\n')
