from scrapli import Scrapli



conn = Scrapli(
    host="192.168.0.14",
    auth_username="euro",
    auth_password="europass",
    platform="cisco_iosxe",
    transport="ssh2",
    auth_secondary=False,
    auth_strict_key=False,  # <–– disables known_hosts verification
)



conn.open()
response = conn.send_command("show version")
print(response.result)
conn.close()
