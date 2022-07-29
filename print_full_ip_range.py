#!/usr/bin/env python3

import sys

def ip_range(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_list = []

   ip_list.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_list.append(".".join(map(str, temp)))

   return ip_list

#get user input
start_ip = input("Enter starting IP address: ")
end_ip = input("Enter ending IP address: ")

#unfold the IP range
ip_list = ip_range(start_ip, end_ip)

#output unfolded IP range
for ip in ip_list:
   print(ip)
