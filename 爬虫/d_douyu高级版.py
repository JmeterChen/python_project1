#encoding=utf-8
#__author__:Chen bolin

import urllib
import re
import time

f =urllib.urlopen("http://www.douyu.com")
htmlcode =f.read()
time.sleep(5)

imglist_1 =re.findall('data-original="(.*?\.(jpg|png))"',htmlcode)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# print(imglist_1)
# print(len(imglist_1))

# imglist_2 =[]
# print (type(imglist_2 ))
# for i in range(len(imglist_1)):
# 	print(imglist_1[i][0])
# 	print(">"*30)
# 	imglist_2.append(imglist_1[i][0])
	
# print(imglist_2)

# imglist_str =str(imglist_2)
# print("!"*30,type(imglist_str))

#X imglist_true =re.findall('data-original="(.*?\.(jpg|png))"',imglist_str)

# print(imglist_true)	

# print("*"*50)
print(imglist_1)
# print("*"*50)
# # print(len(imglist_1	))

j=1
for i in imglist_1:
	imgurl =i[0]

	print(imgurl)
	print("-"*30)
	urllib.urlretrieve(imgurl,"./photos/%d.jpg"%j)
	j+=1
