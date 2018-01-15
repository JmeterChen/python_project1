#encoding=utf-8
#__author__:Chen bolin


text = "i am %d years old!"% 22

print(" i sad: %s"%text)

print("i sad : %r"%text)

s = 100
h = 50.0
for i in range(2,11):
    s += 2*h
    h /= 2
print("the sum length of path:%f"%s)
print("the last height is:%f"%h)

