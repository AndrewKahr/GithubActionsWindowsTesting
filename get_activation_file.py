import modules.run_cmd as run_cmd
import modules.install_unity as install_unity

get_activation_cmd = [r"C:\Program Files\Unity\Hub\Editor\2020.3.24f1\Editor\Unity.exe", '-batchmode', '-createManualActivationFile',  '-logfile']

install_unity.install_unity()
run_cmd.run_cmd(get_activation_cmd)


