import modules.run_cmd as run_cmd
import modules.install_unity as install_unity
import modules.activate_unity as activate_unity


build_cmd = [r"C:\Program Files\Unity\Hub\Editor\2020.3.24f1\Editor\Unity.exe", '-quit', '-batchmode', '-projectPath',
             'test-project', '-executeMethod', "UnityBuilderAction.Builder.BuildProject", '-buildTarget', 'StandaloneWindows64',
             '-customBuildTarget', 'StandaloneWindows64', '-customBuildPath', "../output/output.exe", "-buildVersion", "v1.0.0",  "-androidVersionCode", "1"]

install_unity.install_unity()
activate_unity.activate_unity()
run_cmd.run_cmd(build_cmd)


