# https://stackoverflow.com/questions/15940280/how-to-get-utc-time-in-python
from datetime import datetime,timezone

class Device():
    def __init__(self, mac_addr, rssi):
        self.mac = mac_addr
        self.RSSIs = [rssi]

file = open('test.txt', 'rt')

device_list: list[Device] = []

for line in file: 
    if line.startswith("hci0 dev"):
        line_list = line.split()
        mac = line_list[2]
        device_type = line_list[4]
        if device_type == "LE":
            rssi = line_list[7][1:]
        if device_type == "BR/EDR":
            rssi = line_list[6][1:]

        now_utc = datetime.now(timezone.utc)
        if len(device_list) == 0:
            device_list.append(Device(mac, (rssi, now_utc)))

        for device in device_list:
            if device.mac == mac:
                device.RSSIs.append((rssi, now_utc))
                break
            else:
                device_list.append(Device(mac, (rssi, now_utc)))
                break

for device in device_list:
    print(device.mac, len(device.RSSIs))
