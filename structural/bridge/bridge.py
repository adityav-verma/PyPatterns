# Circles and Squares
# Raster and Vector
from abc import abstractmethod, ABC


class Renderer(ABC):
    @abstractmethod
    def render_circle(self):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        return f'Drawing on the screen for circle with radius {radius}'


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        return f'Drawing pixel on the screen for circle with radius {radius}'


# Basically one side of the cartesian product is injected as a dependency into the other
class Circle:
    def __init__(self, radius, renderer: Renderer):
        self.renderer = renderer
        self.radius = radius

    def __str__(self):
        return self.renderer.render_circle(self.radius)


if __name__ == '__main__':
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()
    c1 = Circle(1, vector_renderer)
    c2 = Circle(2, raster_renderer)

    print(c1)
    print(c2)