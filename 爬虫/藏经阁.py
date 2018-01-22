#coding=utf-8

import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import time


#打开谷歌浏览器
driver = webdriver.Chrome()
url = "http://xyq.cbg.163.com/cgi-bin/xyq_overall_search.py?act=show_search_role_form"
driver.get(url)

#获取当前窗口句柄
now_handle = driver.current_window_handle
# print(now_handle)

#xpath路径定位角色
role_list_source = driver.find_elements_by_xpath("//*[@id='race_list']/li")

#获得角色列表
role_list = []
for role in role_list_source:
    role_list.append(role.text)
print(role_list)

#xpath路径等级
rolelevel_list_source = driver.find_elements_by_xpath("//ul[@class='btnList']/li[@data-level]")
rolelevel_list = []
#获得角色等级列表
for rolelevel in rolelevel_list_source:
    rolelevel_list.append(rolelevel.text)

for a in range(len(rolelevel_list)):
    rolelevel_list[a]=rolelevel_list[a].replace("级","")
print(rolelevel_list)





# handle_list =[]
# for s in rolelevel_list:
#     driver.find_element_by_id("level_min").send_keys(s)
#     time.sleep(1)
#     driver.find_element_by_id("level_max").send_keys(s)
#     time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="btn_do_query"]').click()
#     time.sleep(1)
#     driver.close()




#将一个列表的元素改成梯度列表
# a  = [11,22,33,44]
# b=[]
# for i in range(len(a)):
# 	for j in range(i,len(a)):
# 		b.append((a[i],a[j]))
# print(b)

#将等级列表元素改成梯度列表
# rolelevel_list_nums =[]
# for i in range(len(rolelevel_list)):
#     for j in range(i,len(rolelevel_list)):
#         rolelevel_list_nums.append((rolelevel_list[i],rolelevel_list[j]))
# print(rolelevel_list_nums)


#使用特例69
# driver.find_element_by_id("level_min").send_keys(rolelevel_list_nums[0][0])
# driver.find_element_by_id("level_max").send_keys(rolelevel_list_nums[0][1])
# driver.find_element_by_xpath('//*[@id="btn_do_query"]').click()

#使用列表中的每个元素
# for x,y in rolelevel_list_nums:
	# print(x,y)
# for i in rolelevel_list_nums:
#     if driver.current_window_handle == now_handle:
#         driver.find_element_by_id("level_min").send_keys(i[0])
#         driver.find_element_by_id("level_max").send_keys(i[1])
#         driver.find_element_by_xpath('//*[@id="btn_do_query"]').click()




#//*[@id="btn_do_query"]
	
 




