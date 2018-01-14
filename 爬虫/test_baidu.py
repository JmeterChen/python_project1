#encoding=utf-8
#__author__:Chen bolin

import urllib
import time  
from selenium import webdriver  
  
  
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.implicitly_wait(6)  
  
driver.get("http://www.baidu.com/")  

print(driver.current_url)
time.sleep(1)  
driver.find_element_by_link_text("新闻").click()  
time.sleep(1)  
print (driver.current_url)  # current_url 方法可以得到当前页面的URL 

url_a = driver.current_url
htmlcode = urllib.urlopen(url_a).read()
# print(htmlcode)
