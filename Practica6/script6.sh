#!/bin/bash

priv=$(hostname -I)
pub=$(curl ifconfig.me)

nmap 192.168.0.1
nmap --script ssh-auth-methods -p 22 $priv
nmap -Pn $pub