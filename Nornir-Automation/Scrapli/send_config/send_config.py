from nornir import InitNornir

from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result



nr = InitNornir(config_file="config.yaml")




def send_config_test(task):
    task.run(task=send_config , config="ntp server 7.7.7.7")

result = nr.run(task=send_config_test)


print_result(result)
#print(type(result))