def getNumber():
    while True:
        try:
            num = float(input('введите число: '))
        except Exception as e:
            print('its not a number, try again')
            print('Excception: ' + str(e))
        else:
            return num


def getWord():
    while True:
        str1 = input('enter the word : ')
        str1 = str1.strip(' ')
        if str1.find(' ') == -1:
            return str1
        print('it is not a word because it contains a space')


def is_year_leap(year):
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

def isTriangle(a,b,c):
    if c<a+b and a<b+c and b<a+c:
        return True
    else:
        return False

def getTypeTriangle(a,b,c):
    if isTriangle(a,b,c):
        if a==b==c:
            return 'Equilateral triangle (равносторонний)'
        elif a==b or b==c or a==c:
            return 'Isosceles triangle (равнобедренный)'
        else:
            return 'Versatile triangle (разносторонний)'
    else:
        return 'Not a triangle'

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

# print('entered number '+str(getNumber()))
# print('entered word '+str(getWord()))

#print(is_year_leap(2020))
#print(is_year_leap(1965))
#print(is_year_leap(1984))
#print(is_year_leap(1980))

print(isTriangle(3,4,5))
print(isTriangle(9,4,5))
print(isTriangle(4.1,9,5))
print('*******type triangle')
print(getTypeTriangle(9,4,5))
print(getTypeTriangle(3,4,5))
print(getTypeTriangle(4.1,9,5))
print(getTypeTriangle(9,5,5))
print(getTypeTriangle(5,5,5))
print('*******distance')
print(distance(0,4,3,0))
print(distance(1,5,4,1))
