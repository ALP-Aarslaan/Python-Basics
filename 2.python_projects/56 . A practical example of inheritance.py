class Shape:
    dimension1 = 0.0
    dimension2 = 0.0

    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2

    def area(self):
        size = self.dimension1 * self.dimension2


class Triangle(Shape):
    def area(self):
        size = 0.5 * self.dimension1 * self.dimension2
        print("area of triangle is : ", size)


class Rectangle(Shape):
    def area(self):
        size = self.dimension1 * self.dimension2
        print("area of a rectangle :", size)


t = Triangle(20,30)
t.area()

r = Rectangle(20,30)
r.area()
