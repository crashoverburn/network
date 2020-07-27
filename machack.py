#!/usr/bin/python

import subprocess

from termcolor import colored

def change_mac_addr(interface,mac):
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",mac])
        subprocess.call(["ifconfig",interface,"up"])

def main():
        interface = str(input("[*] Enter the interface to change mac addr: "))
        new_mac_addr = input("[*] Enter Mac Address to Change :")
        before_change = subprocess.check_output(["ifconfig",interface])
        change_mac_addr(interface, new_mac_addr)
        after_change = subprocess.check_output(["ifconfig",interface])

        if before_change == after_change:
                print(colored("[!!!] Failed to change Mac Addr to : " + new_mac_addr,"red"))
        else:
                print(colored("[+] Mac Addr changed to : " + new_mac_addr,"green"))

main()
