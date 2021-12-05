from subprocess import Popen, PIPE

def run_cmd(cmd):
    assert isinstance(cmd, list)
    with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            print(line, end='')  # process line here

install_cmd = ["C:/Program Files/Unity Hub/Unity Hub.exe", '--', '--headless',  'install', '--version',  '2020.3.24f1',  '--changeset',  '79c78de19888']
get_activation_cmd = [r"C:\Program Files\Unity\Hub\Editor\2020.3.24f1\Editor\Unity.exe", '-batchmode', '-createManualActivationFile',  '-logfile']

run_cmd(install_cmd)
run_cmd(get_activation_cmd)


