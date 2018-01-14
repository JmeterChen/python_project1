#encoding=utf-8
#__author__:Chen bolin

import urllib

f = urllib.urlopen("http://www.baidu.com")


htmlCode =f.read()
# print(htmlCode)
# print(f.info())
# print(f.getcode())
a = (f.geturl())
# print(a)

m = urllib.urlopen(a)


htmlCode_2 =m.read()
print(htmlCode_2)





