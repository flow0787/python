#!/usr/bin/python3

import shlex
import subprocess

# script's first argument, for example lab
# ENV = str('320749')
ENV = 'techops'
#ENV = '342494'
# RES_GROUP = str('320749')
RES_GROUP = 'techops'
#RES_GROUP = '342494'

# NAMESPACE = 'sb-pre-ddm320749'
NAMESPACE = 'sb-techops007'
#NAMESPACE = 'sb-342494'

# bearber token from DN - ABOUT in DDM
KEY = 'Bearer '

URL = 'https://{}-api.ddm.iot-accelerator.ericsson.net/'.format(ENV)
print(URL)
filter = '?PageSize=1000'
header = {'Authorization': '{}'.format(KEY), 'Content-type': 'application/json'}


gateways = ()


no_queue = 0

# GET device networks
API = 'api/v3/deviceNetworks'
r = requests.get(URL + API + filter, headers=header)
result = r.json()
# print(result)

print('%20s %20s %20s %36s %36s' % ('Gateway Name', 'Location', 'Gateway Type', 'Gateway ID', 'Queue Name'))
print('-' * 141)

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
    for gw in gateways:
      if dc['Name'] == gw:
#        print('{!s:<25} {!s:<20} {!s:<20} {!s:<40s}'.format(dc['Name'], dc['LocationName'], dc['DataCollectorTypeName'], dc['Id']))
        myid = dc['Id']
        az_cli = (
          'az servicebus queue show --resource-group {} --namespace-name {} --name {} --query \"id\" -o tsv'.format(
            RES_GROUP, NAMESPACE, myid))
        subprocess_cmd = shlex.split(az_cli)
        output = subprocess.check_output(subprocess_cmd)
        output = output.decode('utf-8')
        output = output.split('/')
        queue_name = output[-1]
        print('{!s:<25} {!s:<20} {!s:<20} {!s:<36s} {!s:<36}'.format(dc['Name'], dc['LocationName'], dc['DataCollectorTypeName'],dc['Id'],queue_name))
        myid = dc['Id']
        p = subprocess.Popen(subprocess_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        return_code = p.returncode
        if return_code != 0:
          no_queue = no_queue + 1

print('-' * 141,'\n')
print('+' * 31)
print('Total Gateways: {!s:>15}'.format(len(gateways)))
print('Total Gateways without queue: {}'.format(no_queue))
print('+' * 31)
