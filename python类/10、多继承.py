#encoding=utf-8
#__author__:Chen bolin

# #情况一： 多继承的时候，调用不同基类的不同名称方法
# class A:
#     def test1(self):
#         print("-------testA------")
#
# class B:
#     def test2(self):
#         print("-------testB------")
#
# class C(A,B):
#     pass
#
# c =C()
# c.test1()   #-------testA------
# c.test2()   #-------testB------





# # #情况二：多继承的时候，调用不同基类的相同名称方法
#
# class A:
#     def test1(self):
#         print("-------test1------")
#
#     def test(self):
#         print("-------testA------")
#
# class B:
#     def test2(self):
#         print("-------test2------")
#
#     def test(self):
#         print("-------testB------")
#
# class C(A,B):  #不同基类中拥有相同名称方法的时候，子类调用的时候，A写在前面A先被调用
#     pass
#
# class D(B,A):  #不同基类中拥有相同名称方法的时候，子类调用的时候，B写在前面B先被调用
#     pass
#
# c =C()
# c.test()    #-------testA------
#
# d= D()
# d.test()    #-------testB------





#情况三：多继承的时候，不同基类中相同名称方法，且子类中也有与此方法相同名称的方法
class A:
    def test1(self):
        print("-------test1------")

    def test(self):
        print("-------testA------")

class B:
    def test2(self):
        print("-------test2------")

    def test(self):
        print("-------testB------")

class E(A,B):
    def test(self):
        print("-------testE------")

e =E()
e.test()   #-------testE------   想子类与多继承的不同基类中拥有相同名称的方法时，子类会E优先选择自己类中的方法

#