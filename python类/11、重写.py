# -*- ecoding=utf-8 -*-
# Author:Chen Bolin

#情况一：
# class Cat:
#
#     def __init__(self,newName,newAge):
#         self.__name =newName
#         self.__age  =newAge
#         print("我是Cat类型中的构造方法")
#
# class Bosi(Cat):
#
#     #子类的方法名与父类的方法名相同
#     def __init__(self,a,b):
#         print("我是波斯类型中的构造方法")
#
# bosi =Bosi("aaa",100)  # 我是波斯类型中的构造方法    ##子类与继承的基类拥有相同名称的方法的时候，会优先调用自己类中的方法


#那么问题来了，子类如果与基类中拥有相同名称的方法的时候，怎么调用基类的那个与自己同名的方法呢？
#情况二：
class Cat:

    def __init__(self,newName,newAge):
        self.name =newName
        self.age  =newAge
        print("我是Cat类型中的构造方法")

class Bosi(Cat):

    #子类的方法名与父类的方法名相同
    def __init__(self,a,b,c):
        Cat.__init__(self,a,b)
        self.weight = c
        print("我是波斯类型中的构造方法")


bosi =Bosi("贡菊",100,6)
print(bosi.name)
print(bosi.age)
print(bosi.weight)