# coding:utf-8

import requests
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings() #解决requests提示警告InsecureRequestWarning的问题

urls = open("urls.txt","r")

for url in urls:
	if ":443" in url:
		address = "https://" + url.strip()
	else:
		address = "http://" + url.strip()
	#print (address)

	try:
		r = requests.get(address,verify=False)
		soup = BeautifulSoup(r.content,"lxml")
		#titles = soup.title.text
		print (r.url,soup.title.text,r.status_code)
	except:
		print (address,"Error")
