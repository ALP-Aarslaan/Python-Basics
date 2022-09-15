class Triangle:
    base = 0.0
    height = 0.0

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        total = 0.5 * self.base * self.height
        print(total)


t1 = Triangle(10, 10)
t1.area()
