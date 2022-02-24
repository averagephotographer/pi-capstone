import os

# get a lsit of nearby devices and write them to a text file

output_command = os.popen("sh /home/pi/pi-capstone/bluetooth.sh").readlines()
# output_command = os.popen("scan on").readline()

print(output_command)
