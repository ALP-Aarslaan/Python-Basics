"""
set is known as unordered collection of items
it doesn't stores duplicate values, even if you stores it will not print
duplicate values. we can add values into set. we can not print a certain index value in set
set prints elements in ascending orders. we can use set union and not operations in set
"""

num1 = {1, 2, 3, 4, 5, 5, 5}
num1.add(6)
print(num1)
# print(num1[1])

num2 = set([12,4,16,8,10])
num2.remove(8)
print(num2)
print(8 in num2)
print(8 not in num2)
# print(num2[1])
# set union:
print(num1|num2)
# set intersection :
print(num1 & num2)
# set difference :
print(num1 - num2)