from typing import List


# This class basically handles both scalar and composite properties by keeping children within itself
class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children: List[GraphicObject] = []
        self._name = 'Graphic'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)
    

class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'


if __name__ == '__main__':
    red_circle = Circle('red')
    blue_circle = Circle('blue')

    green_square = Square('green')
    group = GraphicObject()
    group.children.append(Circle('Purple'))
    group.children.append(Square('Yellow'))

    print(red_circle)
    print(blue_circle)
    print(green_square)

    print(group)