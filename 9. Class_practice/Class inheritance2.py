# 점, 원, 원기둥의 길이 및 넓이 상속으로 구하기

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return 0
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def __repr__(self):
        return f'x={self.x} y={self.y}'

class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.radius = r
    def area(self):
        return math.pi * self.radius * self.radius
    def __repr__(self):
        return f'{super().__repr__()} radius={self.radius}'

class Cylinder(Circle):
    def __init__(self, x, y, r, h):
        super().__init__(x, y, r)
        self.height = h
    def area(self):
        return 2 * Circle.area(self) + 2*math.pi * self.radius * self.height
    def volume(self):
        return super().area()*self.height
    def __repr__(self):
        return f'{super().__repr__()} height={self.height}'
