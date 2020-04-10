from abc import ABC, abstractmethod


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DrawInterface(ABC):
    @abstractmethod
    def draw(self, entity):
        pass


# API to draw
class DrawPoint(DrawInterface):
    def draw(self, entity: Point):
        print('.', end=' ')


# We need to draw this line, but we only have an API to draw a point
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


# Will convert a line to a list of points
class LineToPointAdapter(list):
    def __init__(self, l: Line):
        # Generating dummy points
        print('Generating Points')
        for index in range(10):
            self.append(Point(index, index))


# This will cache the value and won't generate the adapted DS again and again
class LineToPointAdapterCached:
    cache = {}

    def __init__(self, l: Line):
        # Generating dummy points
        self.hash = hash(l)
        if self.hash in LineToPointAdapterCached.cache:
            return
        self.points = []
        print('Generating Points')
        for index in range(10):
            self.points.append(Point(index, index))
        LineToPointAdapterCached.cache[self.hash] = self.points

    def __iter__(self):
        return iter(LineToPointAdapterCached.cache[self.hash])


def draw_line(l: Line, cached: bool = False):
    if not cached:
        adapter = LineToPointAdapter(l)
    else:
        adapter = LineToPointAdapterCached(l)
    print('Drawing Line', end='\n')
    for point in adapter:
        DrawPoint().draw(point)
    print('\n')


if __name__ == '__main__':
    line = Line(Point(1, 1), Point(5, 5))
    draw_line(line)

    print('\n')
    print('Using cached adapter')
    line = Line(Point(1, 1), Point(10, 10))
    draw_line(line, cached=True)
    draw_line(line, cached=True)
    draw_line(line, cached=True)
    draw_line(line, cached=True)