#encoding=utf-8
#__author__:Chen bolin



class GetNum():
    def getNums(self):
        self.a =int(input("请输入第一个数："))   #这里__a与__b需要更改为公有属性
        self.b =int(input("请输入第二个数："))




#定义一个类：完成面积的计算
class juxingArea(GetNum):

    # def getNums(self):
    #     self.__a =int(input("请输入第一个数："))
    #     self.__b =int(input("请输入第二个数："))

    # def calArea(self):
    #     print("矩形面积为:%s"%(self.__a * self.__b))

    def calArea(self):
        print("矩形面积为:%s"%(self.a * self.b))  #这里的原本的__a,__b需要更改变为共有属性才可以在子类中继承


class sanJiaoArea(GetNum):

    # def getNums(self):
    #     self.__a =int(input("请输入第一个数："))
    #     self.__b =int(input("请输入第二个数："))

    # def calArea(self):
    #     print("三角形的面积为:%s" %((self.__a * self.__b)/2))

    def calArea(self):
        print("三角形的面积为:%s" %((self.a * self.b)/2)) #这里的原本的__a,__b需要更改变为共有属性才可以在子类中继承
#
# juxing =juxingArea()
# juxing.getNums()
# juxing.calArea()

# sanjiao =sanJiaoArea()
# sanjiao.getNums()
# sanjiao.calArea()

sanjiao =sanJiaoArea()
sanjiao.getNums()
sanjiao.calArea()  #这次虽然获取a,b的时候调用了基类中的方法，缩短了代码，但是基类中的__a与__b是基类的私有属性，所以需要更改



