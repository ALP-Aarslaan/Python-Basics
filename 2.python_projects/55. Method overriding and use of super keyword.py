class Phone:
    def __init__(self):
        print("i am in phone class")


class Samsung(Phone):
    def __init__(self):
        print("I am in samsung class")  # here we overridden init method in samsung class


class IPhone(Phone):
    def __init__(self):
        super().__init__() # use of super keyword
        print("i am in IPhone class")


p1 = Samsung()

p2 = IPhone()
