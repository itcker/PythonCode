# coding:utf-8

import requests
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings() #解决requests提示警告InsecureRequestWarning的问题

def open_ipFile():
    ip_list=[]
    with open('ip.txt','r') as f:
        for ip in f.readlines():
            ip=ip.strip()
            ip_list.append(ip)
        ip_list = list(set(ip_list))
        return ip_list
#print (open_ipFile())

def port():
	port_list=["80","443","8080"]
	return port_list

def gettitle():
	url = "http://"+str(ip)+":"+str(port)+"/"
	try:
		r = requests.get(url,verify=False,timeout=3)
		soup = BeautifulSoup(r.content,"lxml")
		titles = soup.title.text
		return r.url,soup.title.text,r.status_code
	except:
		return url,"Error"

for ports in port():
	port = ports
	for ip in open_ipFile():
		#print (ip)
		print (gettitle())
		#print (ports)
