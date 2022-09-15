try:
    num = input("enter a number :")
    num = int(num)
    result = 20 / num
    print(result)
except ZeroDivisionError:
    print("we cant divide something by zero")

try:
    num = [20, 0, 40]
    result = num[0] / num[5]
    print(result)
except:
    print("cant divide with zero")
# finally:
#     print("done")
