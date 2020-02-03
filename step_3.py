matrix = [
    [0.5, 0, 0, 0, 0],
    [1, 0.5, 0, 0, 0],
    [1, 1, 0.5, 0, 0],
    [1, 1, 1, 0.5, 0],
    [1, 1, 1, 1, 0.5]
]

# print(matrix)

# итерировать - то, что идет после in (итерэбл)
for row in matrix:
    print(row)
    # print(sum(row))

# транспонирование матрицы
print('*' * 17)

matrix_t = zip(
    matrix[0],
    matrix[1],
    matrix[2],
    matrix[3],
    matrix[4]
)
for row in matrix_t:
    print(row)

# zip() map() filter()    # изучить их - очень полезны!!

print('*' * 17)

matrix_t = zip(*matrix)
for row in matrix_t:
    print(list(row))
