from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result



nr = InitNornir(config_file="config.yaml")



def pull_random_info(task):
    task.run(task=napalm_get , getters=["get_environment","get_interfaces"])



result = nr.run(task=pull_random_info)
print_result(result)