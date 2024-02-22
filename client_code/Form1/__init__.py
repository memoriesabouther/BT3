from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import ipaddress
class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def subnet_calculation(self, ip_address, subnet_mask):
        try:
            # Tạo đối tượng IPv4Network từ địa chỉ IP và subnet mask
         network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)

            # Trả về thông tin về mạng và subnet mask
         return f"Địa chỉ IP: {network.network_address}, Subnet Mask: {network.netmask}"

        except ValueError:
            return "Địa chỉ IP hoặc subnet mask không hợp lệ."

    def button_1_click(self, **event_args):
      ip_address = self.text_box_ip_address.text
      subnet_mask = self.text_box_subnet_mask.text
  
          # Gọi hàm subnet_calculation để tính toán và hiển thị thông tin mạng con
      result = self.subnet_calculation(ip_address, subnet_mask)
  
          # Hiển thị kết quả trong textbox_result
      self.textbox_result.text = result
