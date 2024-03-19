#!/usr/bin/env python3

import sys
import re

def validate_ip(ip):
    pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    if not pattern.match(ip):
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
    return True

def ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_list = []

    if not validate_ip(start_ip) or not validate_ip(end_ip):
        raise ValueError("Invalid IP address")

    ip_list.append(start_ip)
    while temp != end:
        for i in (3, 2, 1):
            if temp[i] == 255:
                temp[i] = 0
                temp[i-1] += 1
                break
        temp[3] += 1
        ip_list.append(".".join(map(str, temp)))

    return ip_list

#get user input
while True:
    start_ip = input("Enter starting IP address: ")
    if validate_ip(start_ip):
        break
    print("Invalid IP address. Please try again.")

while True:
    end_ip = input("Enter ending IP address: ")
    if validate_ip(end_ip):
        break
    print("Invalid IP address. Please try again.")

#unfold the IP range
ip_list = ip_range(start_ip, end_ip)

#output unfolded IP range
for ip in ip_list:
    print(ip)
