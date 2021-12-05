from modules.run_cmd import run_cmd

activate_cmd = [r"C:\Program Files\Unity\Hub\Editor\2020.3.24f1\Editor\Unity.exe", '-batchmode', '-quit', '-nographics',
                '-manualLicenseFile',  'license.ulf', '-logfile']


def activate_unity():
    run_cmd(activate_cmd)
