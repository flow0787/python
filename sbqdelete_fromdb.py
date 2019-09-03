#!/usr/bin/python3
# obtain json from appiot db using this query:
# SELECT name, id FROM datacollectors WHERE inactive = 0 and name != 'AppIot Internal'
# add the json inside  this script's root named as gateways.json
# add these lines at the top of the file:
# { "gateways": [
# add this at the bottom:
#   }]
#}

import json
import shlex
import subprocess
import argparse


# arguments parser
parser = argparse.ArgumentParser()

parser.add_argument('-s', help='subscription id', required=True)
#  parser.add_argument('-e', help='IOT environment', required=True)
parser.add_argument('-rg', help='resource group of the service bus', required=True)
parser.add_argument('-n', help='namespace of the service bus', required=True)
parser.add_argument('-d', help='delete queues flag; if set, will delete unused queues', action='store_true')

args = parser.parse_args()

SUBSCRIPTION = args.s
#  ENV = args.e
RES_GROUP = args.rg
NAMESPACE = args.n
DELETE = args.d


# lists where we will store all service bus queues and all used queues
all_queues = []
used_queues = []
# number of gateways without queues
no_queue = 0

# the az cli command to get the queues
az_cli = ('az servicebus queue list --subscription {} --resource-group {} --namespace-name {} --query "[].id" -o tsv'.format(SUBSCRIPTION, RES_GROUP, NAMESPACE))
# split the command into a list which subprocess.check_output can understand
subprocess_cmd = shlex.split(az_cli)
# run the command and save the output in output variable as bytes
output = subprocess.check_output(subprocess_cmd)
# convert the output to string
output = output.decode('utf-8')
# save the queue name into the all_queues variable
all_queues = output.split('/subscriptions/'+SUBSCRIPTION+'/resourceGroups/'+RES_GROUP+'/providers/Microsoft.ServiceBus/namespaces/'+NAMESPACE+'/queues/')
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

print('-' * 123)
print('|%20s %36s %36s %27s' % ('Gateway Name', 'Gateway ID', 'Queue Name', '|'))
print('-' * 123)

# open the gateways.json file
try:
  with open('gateways.json', 'r') as f:
    gateways = json.load(f)
except FileNotFoundError:
  print('gateways.json file not found.')
except Exception:
  print('Something went wrong...')      # iterate over all items of the dict and obtain the gateway id

# iterate over all gateways in the gateways.json file and find the queue
for gw in gateways['gateways']:
  gw_name = gw['name']
  gw_id = gw['id']
  az_cli = ('az servicebus queue show --subscription {} --resource-group {} --namespace-name {} --name {} --query \"id\" -o tsv'.format(SUBSCRIPTION, RES_GROUP, NAMESPACE, gw_id))
  subprocess_cmd = shlex.split(az_cli)
  p = subprocess.Popen(subprocess_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  p.wait()
  return_code = p.returncode
  if return_code != 0:
    no_queue = no_queue + 1
    queue_name = 'NO QUEUE'
  # if the return code of the above command is 0 - which means executed with success, proceed with:
  else:
    output = subprocess.check_output(subprocess_cmd)
    output = output.decode('utf-8')
    output = output.strip()
    output = output.split('/')
    queue_name = output[-1]
    used_queues.append(queue_name)
  print('{!s:<45} | {!s:<20} | {!s:<20}'.format(gw_name, gw_id, queue_name))
print('-' * 123)
#list of unused queues
unused_queues = []

# check if a queue from the all_queues list is in the list of used_queues
for aq in all_queues:
  # if not, add it to unused_queues
  if aq not in used_queues:
    unused_queues.append(aq)

# no of deleted queues
deleted_queues = 0

# delete all unused queues if there are any:
if DELETE:
  if len(unused_queues) > 1:
    for q in unused_queues:
      az_cli = ('az servicebus queue delete --subscription {} --resource-group {} --namespace-name {} --name {}'.format(SUBSCRIPTION, RES_GROUP, NAMESPACE, q))
      subprocess_cmd = shlex.split(az_cli)
      delete_return_code = subprocess.call(subprocess_cmd)
      if delete_return_code == 0:
        print('Successfully deleted unused queue {}'.format(q))
        deleted_queues += 1
      else:
        print('Could NOT delete unused queue {}'.format(q))
  else:
    print('There are no unused queues to delete.')
else:
  print('Will not remove unused queues. Delete flag (-d) isn\'t set.')

print('-' * 123)
print('|%20s %20s %20s %20s %38s' % ('Total Queues', 'Used Queues', 'Unused Queues', 'Removed Queues', '|'))
print('-' * 123)
print('|{:>10} {:>21} {:>18} {:>18} {!s:>51}'.format(len(all_queues), len(used_queues), len(unused_queues),deleted_queues, '|'))
print('-' * 123)

# FOR DEBUG ONLY
#print('all: \n{}'.format(all_queues))
#print('used: \n{}'.format(used_queues))
#print('unused: \n{}'.format(unused_queues))
