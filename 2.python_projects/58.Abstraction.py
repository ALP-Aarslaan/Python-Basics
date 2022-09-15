from abc import ABC, abstractmethod


class A(ABC):  # abstract class creation
    @abstractmethod
    def print(self):  # abstract method creation
        pass


# obj = A()  # we can not create or instantiate object of abstract class.
"""
if any class inherits any abstract class then all the abstract methods need to 
implement the method which is in the abstract class.

"""
