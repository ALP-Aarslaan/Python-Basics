num1=int(input("enter a number : "))
num2=int(input("enter a number : "))
num3=int(input("enter a number : "))

if num1>num2 and num1>num3:
    print(num1," is the largest.")
elif num2>num1 and num2>num3:
    print(num2," is the largest")
else:
    print(num3,"is the largest.")

letter = input("enter a letter:")
if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u'or letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U':
    print(letter,"vowel")
else:
    print(letter,"consonant")