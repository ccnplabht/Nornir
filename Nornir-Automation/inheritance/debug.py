from nornir.plugins.inventory.simple import SimpleInventory
from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result
from pprint import pprint

nr = InitNornir(config_file="config.yaml")



host = nr.inventory.hosts["R1"]

#pprint(host.dict())
print(type(host.groups))
pprint(host.groups)
print(type(host.groups[0]))
print(host.groups[0])

print("##########################################")
for group in host.groups:
    print(f"Group name: {group.name}")
    pprint(group.data)          # Custom data like ntp_server
    pprint(group.data["ntp_server"])  
    pprint(group.username)        # If defined
    pprint(group.password)        # If defined
    pprint(group.platform)        # If defined

