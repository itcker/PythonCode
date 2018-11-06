# coding:utf-8

import requests
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()

#url = "http://183.224.16.233:8089/bsys/newPortal/login.html"
urls = open("urls.txt","r")

for url in urls:
	if "http://" in url:
		url = url
	elif "https://" in url:
		url = url
	else:
		url = "http://" + url.strip()
	try:
		r = requests.get(url,verify=False)
		soup = BeautifulSoup(r.content,"lxml")
#print (soup)
		#ContentLength = dict(r.headers).get('Content-Length', 0)
		#print (r.url,soup.title.text,r.status_code,ContentLength)
		if r.status_code == 200:
			print (r.url,"该地址正常")
		else:
			print (r.url,soup.title.text,r.status_code)
	except:
		print (url,"该地址无法连接，访问失败")
	
#if ContentLength == "6242":
	#print ("经测试，该网站正常")
#else:
	#print ("经测试，该网站异常。请手动查看是否存在异常界面")
