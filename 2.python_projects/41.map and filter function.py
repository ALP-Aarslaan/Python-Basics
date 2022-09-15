def square(x):
    return x ** 2


num = [1, 2, 3, 4, 5, 6]
result = list(map(square, num))
print(result)

"""
filter function mainly does filtering on the basis of some conditions
"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, num))
print(result)
