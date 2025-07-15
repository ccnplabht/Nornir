from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")


def another_show_config_test(task):
    task.run(task=netmiko_send_config , config_file="randomconfigs.txt")


result = nr.run(another_show_config_test)



print_result(result)