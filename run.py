import os
import time
import subprocess

cmd = ["C:/Program Files/Unity Hub/Unity Hub.exe", '--', '--headless',  'install', '--version',  '2020.3.24f1',  '--changeset',  '79c78de19888']
subprocess.call(cmd)

while(not os.path.exists(r"C:\Program Files\Unity\Hub\Editor\2020.3.24f1\Editor\Unity.exe")):
  print(os.system("tasklist"))
  time.sleep(10)
