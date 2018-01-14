#encoding=utf-8
#__author__:Chen bolin

#urlretrieve方法将URL定位到的html文件下载到你本地的硬盘中
#如果不指定filename，则会存为临时文件
#urlretrieve()返回一个二元组（filename,mine_hdrs）

# import urllib.request
# import ssl

# ret =urllib.request.urlretrieve("https://rpic.douyucdn.cn/anrpic/180104/2371789_2140.jpg","test_1.jpg")

# print(ret)


import urllib
import ssl

ret =urllib.urlretrieve("https://staticlive.douyucdn.cn/storage/webpic_resources/upload/slide/2017/1122/201711221752515656.jpg","./photos/test_2.jpg")

print(ret)