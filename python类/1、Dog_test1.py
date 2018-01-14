#encoding=utf-8
#__author__:Chen bolin


#定义一个类
class Animal:

    #方法
    def setName(self,name):
        self.__name =name

    def printName(self):
        print("名字为：",self.__name)


#定义一个函数
def myPrint(animalName):
    animalName.printName()

dog_one =Animal()
dog_one.setName("旺财")
myPrint(dog_one)

dog_two =Animal()
dog_two.setName("哮天犬")
myPrint(dog_two)


