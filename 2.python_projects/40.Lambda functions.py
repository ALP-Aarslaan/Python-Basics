"""
lambda function is known as anonymous function without any name it is not as powerful
as named function, it only works on single line code
lambda (parameter : expression)(inputs)
"""

# find (a+b)^2 value:
z = (lambda a, b: (a * a) + (2 * a * b) + (b * b))
print(z(2,3))
