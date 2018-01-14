#encoding=utf-8
#__author__:Chen bolin

import urllib
import re

f =urllib.urlopen("http://www.douyu.com")
htmlcode =f.read()
print(type(htmlcode))

print(htmlcode)

# imglist =re.findall('src="(.*?\.(jpg|png))"',htmlcode)  #通过src链接元素，使用正则表达式获取所有图片链接，但是斗鱼有反爬虫机制，图片不是直接给的链接，链接前有一串字符串干扰；

imglist =re.findall('data-original="(.*?\.(jpg|png))"',htmlcode)   #注意与上面这行代码获取的链接的区别


print(imglist)
print("*"*50)
print(len(imglist))
print("*"*50)

j=1
for i in imglist:
	imgurl =i[0]

	print(imgurl)
	print(type(imgurl))
	print("-"*30)
	# urllib.urlretrieve(imgurl,"./photos/%d.jpg"%j)
	j+=1





