def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = [x for x in input()]
        matrix.append(row)

    return matrix

def find_symbol_in_matrix(matrix,symbol):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            current_symbol = matrix[row_index][col_index]
            if current_symbol == symbol:
                return row_index, col_index


def print_result(location, symbol):
    if location:
        print(location)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = read_matrix()
symbol = input()

print_result(find_symbol_in_matrix(matrix, symbol), symbol)
