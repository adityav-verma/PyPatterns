"""If there are too many factory methods, or the overall implementation if conplext, we can move things out
into their own separate factory class
"""

from math import sin, cos


class Point:
    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x

    def __str__(self):
        return f'({self.x}, {self.y})'


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho + sin(theta), rho + cos(theta))


if __name__ == '__main__':
    p1 = PointFactory.new_cartesian_point(10, 11)
    p2 = PointFactory.new_polar_point(10, 11)
    print(p1)
    print(p2)