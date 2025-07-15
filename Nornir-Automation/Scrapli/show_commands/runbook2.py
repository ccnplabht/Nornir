from nornir.plugins.inventory.simple import SimpleInventory
from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


"""
host = nr.inventory.hosts["R4"]
print(host.groups[0])
print(host.groups[0].data)
print(host.groups[0].data["ntp_server"])  # ✅ This will now work
print(host.get("ntp_server"))  # ✅ Recommended; searches host → group → defaults

"""





def random_config(task):
    task.run(task=send_config, config=f"ntp server {task.host.groups[0].data["ntp_server"]}")

results = nr.run(task=random_config)
print_result(results)



