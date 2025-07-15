from nornir import InitNornir

from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result



nr = InitNornir(config_file="config.yaml")




def send_configs_test(task):
    #task.run(task=send_configs_from_file, file="/home/autoomation-vm/Automation/Nornir-Automation/Scrapli/send_config/randomconfigs.txt",dry_run=True)
    task.run(task=send_configs_from_file, file="/home/autoomation-vm/Automation/Nornir-Automation/Scrapli/send_config/randomconfigs.txt")
    

result = nr.run(task=send_configs_test)


print_result(result)
#print(type(result))