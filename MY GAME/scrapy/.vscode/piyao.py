from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
import re
import platform
from lxml import etree
from datetime import datetime
from lxml import etree

main_page_url = 'http://piyao.sina.cn/'
chrome_driver_path = ""

if platform.system()=='Windows':
    chrome_driver_path = "chromedriver.exe"
elif platform.system()=='Linux' or platform.system()=='Darwin':
    chrome_driver_path = "./chromedriver"
else:
    print('Unknown System Type. quit...')

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options, \
executable_path= chrome_driver_path)

driver.get(main_page_url)
time.sleep(1)

news = driver.find_elements_by_xpath('//div[@class="left_title"]') # 谣言的内容
likes = driver.find_elements_by_xpath('//div[@class="like_text"]') # 点赞数

news_list=[]
likes_list=[]
for t in news:
    news_list.append(t.text)

for t in likes:
    likes_list.append(t.text)

dict1=dict(zip(news_list,likes_list))

dict2=sorted(dict1.items(),key=lambda x:x[1],reverse=True)

for k,v in dict2:
    print(k,v)
quit()

