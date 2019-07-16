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
    chrome_driver_path = 'chromedriver.exe'
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

# 获取页面初始高度
js = "return action=document.body.scrollHeight"
height = driver.execute_script(js)

# 将滚动条调整至页面底部
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(5)

#定义初始时间戳（秒）
t1 = int(time.time())

#定义循环标识，用于终止while循环
status = True

# 重试次数
num=0

while num < 30:
	# 获取当前时间戳（秒）
    t2 = int(time.time())
    # 判断时间初始时间戳和当前时间戳相差是否大于30秒，小于30秒则下拉滚动条
    if t2-t1 < 30:
        new_height = driver.execute_script(js)
        if new_height > height :
            time.sleep(1)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            # 重置初始页面高度
            height = new_height
            # 重置初始时间戳，重新计时
            t1 = int(time.time())
    num = num+1

dict1 = {}
news_and_likes_and_dates = []
#sortedlist = []

i = 1

while i<=30:
    news = driver.find_elements_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]/following-sibling::ul//div[@class="left_title"]')
    likes = driver.find_elements_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]/following-sibling::ul//div[@class="like_text"]')
    dates = driver.find_elements_by_xpath('//div[@class="zy_day" and position()='+str(i)+']/div[@class="day_date"]')
    news_list = []
    dates_list = []
    likes_list = []
    for t in news:
        news_list.append(t.text)
    for t in likes:
        likes_list.append(int(t.text))
    for t in dates:
        dates_list.append(t.text)
    dates_list = dates_list * len(likes_list)
    i = i+1

    x = 0
    for x in range(0,len(likes_list)):
        dict1.setdefault(news_list[x],[]).append(likes_list[x])
        dict1.setdefault(news_list[x],[]).append(dates_list[x])

sortedlist = sorted(dict1.items(), key=lambda x : x[1][0],reverse = True)

for x in sortedlist[:10]:
    print('点赞数:', x[1][0], '\t','时间：',x[1][1],'\t',x[0])

quit()




