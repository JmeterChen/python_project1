

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(executable_path='/Library/Frameworks/Python.framework/Versions/3.6/bin/chromedriver',chrome_options=options)
# options.add_argument('disable-infobars')
# driver = webdriver.Chrome(chrome_options=options)



list_menpai =["大唐官府"]
list_lishimenpai = []
list_juese = []
list_renwudengji = [69,89,109,129,155,159,175]   #目前直接先写基础数据，后期优化爬虫获取的急促数据
list_jiage = []
list_juesezongjingyan =[]


for dengji  in list_renwudengji:

    dr = webdriver.Chrome()
    dr.get("http://xyq.cbg.163.com/cgi-bin/xyq_overall_search.py?act=show_search_role_form")
    dr.find_element_by_id('level_min').send_keys(dengji)
    dr.find_element_by_id('btn_do_query').click()


#
# a =[123]
# print(a)