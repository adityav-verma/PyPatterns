from abc import ABC


class Shape(ABC):
    pass


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'Circle of radius {self.radius}'


class Square:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'Square of size {self.size}'


class ColorDecorator:
    """Adding more properties to Shape without modifying it, OCP
    However, this doesn't have the properties of Shape, we cannot call Shape function on this
    for that check Dynamic decorator
    """
    def __init__(self, color: str, shape: Shape):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} and color: {self.color}'


if __name__ == '__main__':
    c1 = Circle(2)
    s1 = Square(10)

    colored_c1 = ColorDecorator('red', c1)
    colored_s1 = ColorDecorator('blue', s1)

    print(c1)
    print(s1)
    print(colored_c1)
    print(colored_s1)