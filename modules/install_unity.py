import modules.run_cmd as run_cmd

install_cmd = ["C:/Program Files/Unity Hub/Unity Hub.exe", '--', '--headless',  'install', '--version',  '2020.3.24f1',
               '--changeset',  '79c78de19888', '--module', 'windows-il2cpp']


def install_unity():
    run_cmd.run_cmd(install_cmd)