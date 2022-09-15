"""
usually magic methods starts and ends with double underscore
ex: __init__
"""


class Bike:
    colour = ""
    name = ""

    def __init__(self, colour, name):
        self.name = name
        self.colour = colour

    def __str__(self):
        return "name = "+self.name+" colour = "+self.colour

    def __eq__(self, other):
        return self.name == other.name and self.colour == other.colour

    def display(self):
        print("Name :", self.name, "Colour :", self.colour)


bike1 = Bike("R15", "Black")
print(bike1)
bike2 = Bike("R15", "black")
print(bike1 == bike2)