#encoding=utf-8
#__author__:Chen bolin

from selenium import webdriver
import urllib
from bs4 import BeautifulStoneSoup
import time

dr = webdriver.Chrome()
now_handle = dr.current_window_handle   #获取当前窗口句柄
print(now_handle)
dr.maximize_window()  
dr.implicitly_wait(3)  
dr.get("http://xyq.cbg.163.com/cgi-bin/xyq_overall_search.py?act=show_search_role_form")
time.sleep(1)

dr.find_element_by_id('level_min').send_keys(69)
time.sleep(0.1)
dr.find_element_by_id('level_max').send_keys(69)
dr.find_element_by_id('btn_do_query').click()
time.sleep(1)
# dr.current_url
print(dr.current_url)

# htmlCode = urllib.urlopen(url_1).read()
# print(htmlCode)





