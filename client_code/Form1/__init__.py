from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def subnet_calculation(self, ip_address, subnet_mask):
        # Chuyển đổi địa chỉ IP và subnet mask sang dạng list của các số thập phân
        ip_parts = [int(part) for part in ip_address.split('.')]
        mask_parts = [int(part) for part in subnet_mask.split('.')]

        # Tính toán địa chỉ mạng và broadcast address
        network_address = [ip & mask for ip, mask in zip(ip_parts, mask_parts)]
        broadcast_address = [(ip | ~mask) & 255 for ip, mask in zip(network_address, mask_parts)]

        # Hiển thị thông tin về mạng và subnet mask trên giao diện
        self.label_ip_address.text = f"Địa chỉ IP: {'.'.join(map(str, network_address))}"
        self.label_subnet_mask.text = f"Subnet Mask: {subnet_mask}"
        self.label_broadcast_address.text = f"Broadcast Address: {'.'.join(map(str, broadcast_address))}"

    # Xử lý sự kiện khi nút "Tính toán" được nhấn
    def button_calculate_click(self, **event_args):
        ip_address = self.text_box_ip_address.text
        subnet_mask = self.text_box_subnet_mask.text

        # Gọi hàm subnet_calculation để tính toán và hiển thị thông tin mạng con
        self.subnet_calculation(ip_address, subnet_mask)