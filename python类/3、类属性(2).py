#encoding=utf-8
#__author__:Chen bolin

class Dog:

    color ="白色"
    __sex ="公"


    def __setName(self,newName):
        self.name =newName
        self.money =100000
        self.__girlfriend ="alice"

    def  newSetName(self,newName):
        self.__setName(newName)

    def showGirfriend(self):
        print("girlFriend's name is %s"%self.__girlfriend)

    def showSex(self):
        print("这个狗狗的性别为%s"%self.__sex)

    def showSex2(self):
        return self.__sex

    def eat(self):
        print("这个狗狗的名字叫%s,存款有%s"%(self.name,self.money))


d =Dog()
#d.setName("旺财")  #当类中的方法也变为私有的时候，此时类外面就无法直接调用
d.newSetName()  #必须在类中新增一个方法才能调用对应的私有方法
d.eat()

print(d.color)

# print(d.sex)   这个直接引用类私有属性会报错

d.showGirfriend()

d.showSex()
print(d.showSex2())
