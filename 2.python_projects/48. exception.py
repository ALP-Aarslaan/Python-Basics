try:
    num1 = int(input("enter a number :"))
    num2 = int(input("enter another number :"))
    result = num1 / num2
    print(result)
except (ZeroDivisionError, ValueError,):
    print("enter an integer")

    """
    we can also use raise keyword for detecting exceptions
    """
