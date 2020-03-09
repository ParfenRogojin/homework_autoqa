class Rectangle():
    def __init__(self, len_x, len_y):
        self.len_x = len_x
        self.len_y = len_y

    def sq(self):
        return self.len_x * self.len_y

    def p(self):
        return 2 * self.len_x + 2 * self.len_y

    def __str__(self):
        return "side1 = {}, side2={}. \nS = {}, P = {}".format(self.len_x,self.len_y,self.sq(),self.p())

if __name__ == '__main__':
    room1 = Rectangle(4, 5)
    print('периметр комнаты ', room1.len_x, ' на ', room1.len_y, ':=', room1.p())
    print('площадь комнаты ', room1.len_x, ' на ', room1.len_y, ':=', room1.sq())

    print('\n__str:')
    print(room1)



