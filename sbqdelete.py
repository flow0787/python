#!/usr/bin/python3

# from azure_client_factory import AzureClientFactory
# from azure_servicebus import *
# from azure.mgmt.servicebus.models import ErrorResponseException
import requests
import shlex
import subprocess

# ENV stands for the Azure Environment to run the script on
# ENV = str('320749')
ENV = 'techops'
#ENV = '342494'
#ENV = '320749-nc1'

# RES_GROUP is the resource group where the service bus namespace + queues exist
# RES_GROUP = str('320749')
RES_GROUP = 'techops'
#RES_GROUP = '342494'
#RES_GROUP = '320749-nc1'

# The name of the Azure service bus namespace where the queues exist
# NAMESPACE = 'sb-pre-ddm320749'
NAMESPACE = 'sb-techops007'
#NAMESPACE = 'sb-342494'
#NAMESPACE = 'sb-pre-ddm320749-nc1'

# bearber token from DDM
KEY = 'Bearer '

# DDM API URL
URL = 'https://{}-api.ddm.iot-accelerator.ericsson.net/'.format(ENV)
print(URL)
filter = '?PageSize=1000'
header = {'Authorization': '{}'.format(KEY), 'Content-type': 'application/json'}


# lists where we will store all service bus queues and all used queues
all_queues = []
used_queues = []

# the az cli command to get the queues
az_cli = ('az servicebus queue list --resource-group {} --namespace-name {} --query "[].id" -o tsv'.format(RES_GROUP, NAMESPACE))
# split the command into a list which subprocess.check_output can understand
subprocess_cmd = shlex.split(az_cli)
# run the command and save the output in output variable as bytes
output = subprocess.check_output(subprocess_cmd)
# convert the output to string
output = output.decode('utf-8')
# save the queue name into the all_queues variable
all_queues = output.split('/subscriptions/32cefe0b-e9b6-44af-9b2e-35c83da094b4/resourceGroups/techops/providers/Microsoft.ServiceBus/namespaces/sb-techops007/queues/')
#all_queues = output.split('/subscriptions/e90fc754-1e60-4705-a9a1-829827e6c008/resourceGroups/320749-nc1/providers/Microsoft.ServiceBus/namespaces/sb-pre-ddm320749-nc1/queues/')
# remove the trailing \n after each queue name
all_queues = map(lambda s: s.strip(), all_queues)
# re-save the resulted output as a list
all_queues = list(all_queues)
# check if the first element of the list is '' and removeit
if all_queues[0] == '':
  all_queues.remove('')

# remove the queues which are in use by drudgery and httpintegration
for q in 'drudgeryqueue', 'drudgerylightweightqueue', 'drudgeryinternalqueue', 'httpintegrationqueue':
  all_queues.remove(q)

#print(all_queues)


# GET device networks
API = 'api/v3/deviceNetworks'
r = requests.get(URL + API + filter, headers=header)
result = r.json()
# print(result)

print('%20s %20s %20s %36s %36s' % ('Gateway Name', 'Location', 'Gateway Type', 'Gateway ID', 'Queue Name'))
print('-' * 143)

# iterate over all items of the dict and obtain the gateway id
for item in result:
  DN_ID = item['Id']
  DN_NAME = item['Name']
  header = {'Authorization': '{}'.format(KEY), 'X-devicenetwork': '{}'.format(DN_ID),
            'Content-type': 'application/json'}
  API = 'api/v3/datacollectors'
  r = requests.get(URL + API + filter, headers=header)
  DC_DICT = r.json()
  #       print(DC_DICT)
  for dc in DC_DICT['Rows']:
      myid = dc['Id']
      az_cli = ('az servicebus queue show --resource-group {} --namespace-name {} --name {} --query \"id\" -o tsv'.format(RES_GROUP, NAMESPACE, myid))
      subprocess_cmd = shlex.split(az_cli)
      p = subprocess.Popen(subprocess_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      p.wait()
      return_code = p.returncode
      if return_code != 0:
        no_queue = no_queue + 1
      # if the return code of the above command is 0 - which means executed with success, proceed with:
      else:
        output = subprocess.check_output(subprocess_cmd)
        output = output.decode('utf-8')
        output = output.strip()
        output = output.split('/')
        queue_name = output[-1]
        used_queues.append(queue_name)
      print('{!s:<25} {!s:<20} {!s:<20} {!s:<36s} | {!s:<36}'.format(dc['Name'], dc['LocationName'], dc['DataCollectorTypeName'],dc['Id'],queue_name))
#print(used_queues)
print('-' * 143,'\n')

#list of unused queues
unused_queues = []

# check if a queue from the all_queues list is in the list of used_queues
for aq in all_queues:
  # if not, add it to unused_queues
  if aq not in used_queues:
    unused_queues.append(aq)

# FOR DEBUG ONLY
print('all: \n{}'.format(all_queues))
print('used: \n{}'.format(used_queues))
print('unused: \n{}'.format(unused_queues))

print('%20s %20s %20s %20s' % ('Total Queues', 'Used Queues', 'Unused Queues', 'Removed Queues'))
print('-' * 84)
print('{:>10} {:>21} {:>18}'.format(len(all_queues), len(used_queues), len(unused_queues)))
print('-' * 84)
