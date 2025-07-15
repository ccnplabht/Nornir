from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result



nr = InitNornir(config_file="config.yaml")



def ping(task):
    task.run(task=napalm_ping , dest="192.168.0.140")



result = nr.run(task=ping)
print_result(result)
