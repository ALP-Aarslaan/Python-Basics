num = int(input("enter a number :"))
if num>10:
    if num<20:
        print("hi")
    else:
        print("bye")

else:
    print("good bye")

num1 = int(input("enter number 1 :"))

num2 = int(input("enter number 2 :"))

num3 = int(input("enter number 3 :"))

if num1>num2:
    if num1>num3:
        print(num1," is highest ")
    else:
        print(num3," is highest ")

else:
    if num2>num3:
        print(num2," is the highest")
    else:
        print(num3," is the highest")
