import os
import time
from subprocess import Popen, PIPE, CalledProcessError


def list_files(startpath):
  for root, dirs, files in os.walk(startpath):
      level = root.replace(startpath, '').count(os.sep)
      indent = ' ' * 4 * (level)
      print('{}{}/'.format(indent, os.path.basename(root)))
      subindent = ' ' * 4 * (level + 1)
      for f in files:
          print('{}{}'.format(subindent, f))


cmd = ["C:/Program Files/Unity Hub/Unity Hub.exe", '--', '--headless',  'install', '--version',  '2020.3.24f1',  '--changeset',  '79c78de19888']
with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        print(line, end='') # process line here

list_files(r'C:\Program Files\Unity\Hub\Editor')


