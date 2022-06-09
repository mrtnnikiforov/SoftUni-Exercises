# [0, 0, 0, 0, 0, 0,],
# [0, 0, 0, 0, 0, 0,],
# [0, 0, 0, 0, 0, 0,],
# [0, 0, 0, 0, 0, 0,],

rows_count, columns_count = map(int, input().split(' '))

matrix = []
for r in range(rows_count):
    matrix.append([0] * columns_count)

start_of_alphabet = 97
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        matrix[r][c] = chr(start_of_alphabet + r) + chr(start_of_alphabet + r + c) + chr(start_of_alphabet + r)

for row in range(rows_count):
    print(' '.join(matrix[row]))



