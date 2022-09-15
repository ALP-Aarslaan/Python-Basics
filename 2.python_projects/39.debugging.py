def addition(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum


result = addition(1,2,3,4,5)
print(result)