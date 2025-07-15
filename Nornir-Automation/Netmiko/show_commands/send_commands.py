from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")

command_list = ['show version' , "show ntp config" , "show ip interface brief"]

def another_show_commands_test(task):
    for cmd in command_list:
        task.run(task=netmiko_send_command , command_string=cmd)


result = nr.run(another_show_commands_test)



print_result(result)