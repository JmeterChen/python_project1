#encoding=utf-8
#__author__:Chen bolin


import  time

class Gun:

    #属性
    color ="黑色"

    def __init__(self,newName,allNum,eveNum):
        self.__name =newName
        self.__bulletnum =allNum
        self.__jianbulletnum =eveNum

    # # 方法
    # def setNum(self,newName):
    #     self.__name =newName
    #
    # #用来设置当前枪的子弹数量
    # def setBulltNum(self,num):
    #     self.__bulletnum =num
    #
    # #定义一个方法，用来设置一个属性，这个属性用来表示每次开枪射出去的子弹数
    # def sefJianBulletNum(self,num):
    #     self.__jianbulletnum =num


    def biubiu(self):
        if self.__bulletnum >self.__jianbulletnum:
            self.__bulletnum -=self.__jianbulletnum
        print("%s剩余的子弹数量为:%d"%(self.__name,self.__bulletnum))


# AK47 =Gun()
# AK47.setNum("AK47")
# AK47.setBulltNum(100)
# AK47.sefJianBulletNum(4)
#
# MP5  =Gun()
# MP5.setNum("MP5")
# MP5.setBulltNum(80)
# MP5.sefJianBulletNum(3)

AK47 =Gun("AK47",100,4)
MP5 =Gun("MP5",60,3)


while True:

    AK47.biubiu()
    MP5.biubiu()

    time.sleep(0.5)

