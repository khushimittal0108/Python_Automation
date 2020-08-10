import os
import sys

#check for saved networks
saved_profiles=os.popen('netsh wlan show profiles').read()
print(saved_profiles)

#check for the available netwroks
available_profiles=os.popen('netsh wlan show networks').read()
print(available_profiles)

#input preferred network
preferred_ssid=input('Enter the preferred wifi for your connection:')

#disconnect the currently connected network
response=os.popen('netsh wlan disconnect').read()
print(response)

#check if preferred network is saved or not
#use if-else
if preferred_ssid not in saved_profiles:
	print("Profile for "+preferred_ssid+" is not saved in sysytem")
	print("Sorry but can't establish the connection")
	sys.exit()
else:
	print("Profile for "+preferred_ssid+" is saved in sysytem")

#check if preferred network is available or not
while True:
	avail =os.popen('netsh wlan show network').read()
	if preferred_ssid in avail:
		print('Found')
		break

#connect to the preferred network
print('--------Connecting----------')
resp = os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()
print(resp)



