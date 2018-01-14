#encoding=utf-8
#__author__:Chen bolin

#定义一个类
class Animal:

    def __init__(self,name,age):
        self.dogname =name
        self.dogage =age


dog1=Animal("旺财",18)
print(dog1.dogname)

dog2 =Animal("哮天犬",88)
print("这个狗的名字叫: ",dog2.dogname)
print("并且%s 的年纪为: %s" %(dog2.dogname,dog2.dogage))
