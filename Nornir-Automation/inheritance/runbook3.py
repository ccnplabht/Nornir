from nornir.plugins.inventory.simple import SimpleInventory
from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")



def remove_config(task):

    task.run(task=send_config, config="no ntp")

results = nr.run(task=remove_config)
print_result(results)
