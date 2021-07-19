import subprocess

define_interface = input('Enter INTERFACE: eth0, wlan0, lo0:>>> ')
define_mac_address = input('Enter desired MAC ADDRESS: 00:11:22:33:44:55:>>> ')

print("=================================================================")
print(f"[+] Changing the Interface Mac Address for {define_interface} to {define_mac_address}")

subprocess.call("ifconfig " + define_interface + " down ", shell=True)
subprocess.call("ifconfig " + define_interface + " hw ether " + define_mac_address, shell=True)
subprocess.call("ifconfig " + define_interface + " up ", shell=True)