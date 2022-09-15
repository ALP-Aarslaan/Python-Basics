matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][1])

matrix[1][1] = matrix[1][1] * 2

print(matrix[1][1])

print("all numbers of the matrix :")
for row in matrix:
    for column in row:
        print(column)
