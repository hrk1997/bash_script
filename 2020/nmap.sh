#/bin/bash
ip=192.168.43.250
sudo nmap -sV $ip
echo " one "
#sudo nmap -A -sC -p- $ip -oN bz.txt
nmap $ip
echo " two "
dirb http://$ip
echo "three"
