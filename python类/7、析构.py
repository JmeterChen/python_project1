#encoding=utf-8
#__author__:Chen bolin

class Animal:

    def __init__(self,name,age):
        self.dogname =name
        self.dogage =age

    def __del__(self):
        print("over........")

dog1 =Animal("测试旺财被删除",100)
print(dog1.dogname)

del dog1
print(dog1.dogname)   #  调用del后，对象dog1就被删除不存在了  这是时通过dog1调用name属性会报错
