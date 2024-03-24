#Напишите функцию для транспонирования матрицы

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed_matrix = [[0] * rows for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose(matrix)

print("Исходная матрица: ")
for row in matrix:
    print(row)

print("Транспонированная матрица: ")

for row in transposed_matrix:
    print(row)
