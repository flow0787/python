#!/usr/bin/python3
# AUTHOR: FLORIN BADEA for Support Eng application @ GitLab
# DESCRIPTION: Script which takes a folder or path as argument
# and filters all files inside to 3 folders by size: small, medium, large
# USAGE: ./filesorter.py -d $FOLDER_NAME 
#        ./filesorter.py -d $FOLDER_PATH

import argparse
import shutil
import os

# arguments parser
parser = argparse.ArgumentParser()

# add the -d argument as required
parser.add_argument('-d', help='directory name', required=True)

args = parser.parse_args()

# save the argument value as path
path = args.d


# if the given folder/path as argument exists, let's continue
if os.path.isdir(path):

  # traversing all folders inside folder/path using os.walk
  for r, d, f in os.walk(path):

  	# for each of the files found
    for file in f:

      # save the full file path and size as variables
      filepath = os.path.join(r, file)
      filesize = os.path.getsize(filepath)

      if filesize <= 500000:
      	# if 'small' folder exists in current working directory, copy the file
        if os.path.isdir('small'):
          shutil.copy(filepath, 'small')

        # else let's create it then copy the file
        else:
          os.mkdir('small')
          shutil.copy(filepath, 'small')

      if filesize > 500000 and filesize <= 1000000:

      	# if 'medium' folder exists in current working directory, copy the file
        if os.path.isdir('medium'):
          shutil.copy(filepath, 'medium')

        # else let's create it then copy the file
        else:
          os.mkdir('medium')
          shutil.copy(filepath, 'medium')
      
      if filesize > 1000000:

      	# if 'large' folder exists in current working directory, copy the file
        if os.path.isdir('large'):
          shutil.copy(filepath, 'large')

        # else let's create it then copy the file
        else:
          os.mkdir('large')
          shutil.copy(filepath, 'large')

# if the given folder/path does not exist, print this message
else:
  print("Given folder/path does not exist")
#### END SCRIPT ####
