#encoding=utf-8
#__author__:Chen bolin

#基类
class Cat:

    #属性
    color = "black"
    legs  = 4
    weight = 6

    #方法
    def miaomiao(self):
        print("猫在喵喵叫。。。。")

    def catch(self):
        print("抓老鼠")

#波斯猫基类
class Bosi(Cat):   #继承基类的属性与方法

    def naoyangyang(self):    #直接在子类中添加新的方法
        print("波斯猫在挠痒痒。。。。")

class TomCat(Bosi):
    pass




xiaohua =Cat()
xiaohua.miaomiao()
xiaohua.catch()

bosi =Bosi()
bosi.miaomiao()
bosi.catch()
bosi.naoyangyang()


tom =TomCat()
tom.naoyangyang()


