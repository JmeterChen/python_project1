#encoding=utf-8
#__author__:Chen bolin


class Book:
    def __init__(self, x=-1, y=-1):
        self.x = x;
        self.y = y;


def printBook(book):
    print('x : ' + str(book.x));
    print('y ：' + str(book.y));


book1 = Book()
printBook(book1)

book2 = Book(1)
printBook(book2)

book3 = Book(1, 2)
printBook(book3)