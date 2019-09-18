#！/usr/bin/env python3
# coding:utf-8

import time,os
from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path

def phones_360_take_screenshot(phones):
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	browser = webdriver.Chrome(chrome_options = options)
	browser.set_window_size(780,450)

	for phone in phones:
		browser.get("https://www.so.com/s?ie=utf-8&fr=none&src=home_www&nlpv=3.7.1&q="+phone)
		time.sleep(0.5)

		html_text = browser.page_source
		
		soup = BeautifulSoup(html_text,'html.parser')
		#print(soup)
		result = soup.find_all("div",class_="mohe-tips")
		#print(result)
		if(result == []):
			print(phone.strip('\n'),"无标记")
		else:
			for i in result:
				pfilename = u'.\\360_image'
				pic_path = pfilename + '\\' + phone.strip('\n') + '.png'
				if Path(pfilename).is_dir():
					pass
				else:
					Path(pfilename).mkdir()
				#print(pic_path)
				time.sleep(0.2)	
				browser.save_screenshot(pic_path)
			
				print(phone.strip('\n'),i.text.replace('\n','').replace('\t',''))

	browser.quit()			
	#os.system("taskkill /f /im chromedriver.exe")
	input('Press Enter to exit...')

if __name__ == "__main__":
 
    phones_360_take_screenshot(open("phones.txt","r"))
