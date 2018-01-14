#encoding=utf-8
#__author__:Chen bolin

import urllib
import re
from bs4 import BeautifulSoup

html ="""<html><head><title>The Dormouse's story</title></head>
<body>
<a href="http://example.com/elise" class="sister1" id ="link1"> <!-- Elsie--></a>

<p class="title" name="dormouse"><b>The Dormouse story</b></p>
<p class="title" name="kobe"><b>The NBA story</b></p>

<p class="story" id="link1">Once upon a time ther were three little sisters;and their names were
	<a href="http://example.com/elise" class="sister1" id ="link1"> aaaa<!-- Elsie--></a>
	<a href="http://example.com/lacie" class="sister1" id ="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister3" id ="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup =BeautifulSoup(html)

# print soup.prettify()        #将HTML补充完整
# print soup.title	           #根据标签名称获取整个标签         <title>The Dormouse's story</title> 
# print soup.ppppp             #如果名称不存在，显示none   	  none
# print soup.title.string      #根据标签名称获取整个标签内容      http://example.com/elise 
# print soup.b.string										   The Dormouse story
# print soup.a['href']          
# print soup.p['class']		   #根据标签下属性名class=''称获取该属性值 
# print soup.p["name"]         #mouse
# print soup.p["class"]         #[u'title']  
# print soup.p.attrs   {u'class': [u'title'], u'name': u'dormouse'}      #通过.attrs显示该标签下所有属性名   #   
# --------------------------------------------------------------------------
#通过CSS选择器
#1、通过标签名查找
# print soup.select('title')  #[<title>The Dormouse's story</title>] 

# 注意下面这两种的区别
# print soup.a             #只会显示第一个a标签
# print soup.select('a')   #会显示所有a标签

#2、通过类名查找   
# print soup.select('.sister')[3]           #[<a class="sister" href="http://example.com/elise" id="link1"> <!-- Elsie--></a>]

#3、通过id名查找
# print soup.select('#link1')               #会显示所有属性值为link1的标签

#4、组合查找  组合进行筛选
# print soup.select('p #link1')             #只会显示p标签(下)属性值为link1 的标签

#5、直接子标签查找
# print soup.select("head > title")         #[<title>The Dormouse's story</title>]

#6、属性值查找
# print soup.select('a[class="sister1"]')   #会显示a标签中属性名称为class的属性值为'sister'的所有标签
#


