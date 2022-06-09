def read_board():
    return [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['Q', '.', '.', '.', '.', '.', '.', '.'],
        ['.', 'K', '.', '.', '.', 'Q', '.', '.'],
        ['.', '.', '.', 'Q', '.', '.', '.', '.'],
        ['Q', '.', '.', '.', 'Q', '.', '.', '.'],
        ['.', 'Q', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', 'Q', '.'],
        ['.', 'Q', '.', 'Q', '.', '.', '.', '.']
    ]


def find_king_position(board):
    pass


def get_capturing_queens(board, king):
    pass


def print_result():
    pass


board = read_board()
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)
