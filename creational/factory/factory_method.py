"""If we did not use these separate methods, then we would have to pass in a type to constructor, then based on that
have several if else conditions. This keeps things simple.
"""

from math import sin, cos


class Point:
    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x

    def __str__(self):
        return f'({self.x}, {self.y})'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho + sin(theta), rho + cos(theta))


if __name__ == '__main__':
    p1 = Point.new_cartesian_point(10, 11)
    p2 = Point.new_polar_point(10, 11)
    print(p1)
    print(p2)