import anvil.server
# Trong file my_ip_module.py
import ipaddress

def subnet_calculation(ip_address, subnet_mask):
    try:
        # Tạo đối tượng IPv4Network từ địa chỉ IP và subnet mask
        network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)

        # Trả về thông tin về mạng và subnet mask
        return f"Địa chỉ IP: {network.network_address}, Subnet Mask: {network.netmask}"

    except ValueError:
        return "Địa chỉ IP hoặc subnet mask không hợp lệ."


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
