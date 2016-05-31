import os 
message = "17 02 01 1a 03 03 aa fe 0f 16 aa fe 10 ed 03 64 65 6d 70 73 65 79 73 07 00 00 00 00 00 00 00 00"
#Stop advertising
os.system("sudo hcitool -i hci0 cmd 0x08 0x000a 00")
#Set message
os.system("sudo hcitool -i hci0 cmd 0x08 0x0008 " + message)
#Resume advertising
os.system("sudo hcitool -i hci0 cmd 0x08 0x000a 01")
