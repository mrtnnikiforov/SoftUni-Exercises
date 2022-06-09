def read_matrix(is_test=True):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    rows_count = int(input())
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = read_matrix()

primary_diagonal_elements = []
secondary_diagonal_elements = []
sum_main = 0
sum_secondary = 0

cols = len(matrix) - 1
for index in range(len(matrix)):
    primary_diagonal_elements.append(str(matrix[index][index]))
    sum_main += int(primary_diagonal_elements[-1])
    secondary_diagonal_elements.append(str(matrix[index][cols]))
    sum_secondary += int(secondary_diagonal_elements[-1])
    cols -= 1

print(f"Primary diagonal: {', '.join(primary_diagonal_elements)}. Sum: {sum_main}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal_elements)}. Sum: {sum_secondary}")


