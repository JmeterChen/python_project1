#encoding=utf-8
#__author__:Chen bolin

def checkio(data):
    if len(data) >=10:
        if data.isalnum() and data !=data.upper() and data !=data.lower():
            while True:
               for i in data:
                   if i.isdigit():
                       return True
               else:
                   return False
        else:
            return False
    else:
        return False
# checkio('asasasasasasasaas')

# Some hints
# Just check all conditions

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    
#最好的方法
def checkio(data):
    if  not ( len(data)<=9 or
    data.isdigit() or
    data.isalpha() or
    data.islower() or
    data.isupper()) :
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    
    
