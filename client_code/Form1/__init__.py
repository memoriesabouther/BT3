from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)


def main():
    # Địa chỉ IP mạng gốc và mặt nạ mạng
    network_address = '192.168.1.0'
    subnet_mask = '255.255.255.0'  # Ví dụ: mặt nạ mạng /24

    # Chuyển đổi địa chỉ IP và mặt nạ mạng thành đối tượng Network
    network = ipaddress.IPv4Network(f'{network_address}/{subnet_mask}', strict=False)

    # In thông tin về mạng con
    print(f'Mạng gốc: {network.network_address}')
    print(f'Mặt nạ mạng: {network.netmask}')
    print(f'Số lượng mạng con: {network.num_addresses}')
    print(f'Số lượng host trong mỗi mạng con: {network.num_addresses - 2}')  # Trừ đi địa chỉ mạng và broadcast
    print(f'Địa chỉ host đầu tiên: {network.network_address + 1}')
    print(f'Địa chỉ host cuối cùng: {network.broadcast_address - 1}')
    print(f'Địa chỉ broadcast: {network.broadcast_address}')

if __name__ == '__main__':
    main()
