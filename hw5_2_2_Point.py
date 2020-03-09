import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def from0(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def __str__(self):
        return "X = {0}, Y = {1}. \nLen([0,0],[{0},{1}]) = {2}".format(self.x, self.y, self.from0())

    def get_polar_coordinates(self):
        if self.x == 0 and self.y == 0:
            return [self.from0(), None]
        #p,f
        return [self.from0(),math.acos(self.x*1.0/((self.x**2+self.y**2))**0.5)]

if __name__ == '__main__':

    pt1 = Point(4, 3)
    print('расстояние от [0,0] точки [', pt1.x, ',', pt1.y, ']:=', pt1.from0(), sep='')

    print('\n__str:')
    print(pt1)
    print('Polar coordinate [L, rad]: ',pt1.get_polar_coordinates())