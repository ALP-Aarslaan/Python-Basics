"""
there are 3 types of inheritance in Python
1.hierarchical inheritance. Example : b and c class inherits from a class
2.multi level inheritance. Example : b inherits a, c inherits b
3. multiple inheritance. Example :b and c class inherits from a class and d inherits from b,c
"""


class A:
    def display1(self):
        print(" I am in A class")


class B(A):
    def display2(self):
        print(" I am in B class")


class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am in c class")


a1 = A()
a1.display1()
b1 = B()
b1.display2()
c1 = C()
c1.display3()


class A1:
    def display(self):
        print("i am inside a1 class")


class B1:
    def display(self):
        print(" i am inside b1 class")


class C1(A1,B1):
    pass


c1 = C1()
c1.display()