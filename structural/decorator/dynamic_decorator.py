from abc import ABC


class Shape(ABC):
    def __iter__(self):
        yield self


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'Circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'Square of size {self.size}'


class DynamicColorDecorator:
    """This will also have properties of the Shape objects
    """
    def __init__(self, color: str, shape: Shape):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} and color: {self.color}'

    # Adding properties of Shape or decorated class
    def __getattr__(self, item):
        return getattr(self.__dict__['shape'], item)

    def __setattr__(self, key, value):
        if key == 'shape':
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['shape'], key, value)

    def __delattr__(self, item):
        delattr(self.__dict__['shape'], item)

    def __iter__(self):
        return self.shape.__iter__()

    def __next__(self):
        return self.shape.__next__()


if __name__ == '__main__':
    c1 = Circle(2)
    s1 = Square(10)

    colored_c1 = DynamicColorDecorator('red', c1)
    colored_s1 = DynamicColorDecorator('blue', s1)

    print(c1)
    print(s1)
    print(colored_c1)
    print(colored_s1)

    # Now we can call functions on decorated class from the decorator
    colored_c1.resize(10)
    print(colored_c1)

    # even iterate
    for obj in colored_s1:
        print(colored_s1)