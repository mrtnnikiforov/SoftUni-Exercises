def read_matrix(is_test=False):
    if is_test:
        return [
            [10, 30, 'B', 4, 20, 24],
            [7, 8, 27, 23, 11, 19],
            [13, 3 ,14, 'B', 17, 'B'],
            [12, 5, 21, 22, 9, 6],
            ['B', 26, 1, 28, 29, 2],
            [25, 'B', 16, 15, 'B', 18],
        ]
    size = 6
    matrix = []
    for row_index in range(size):
        row = list(map(str, input().split(' ')))
        matrix.append(row)
    return matrix


score = 0
matrix = read_matrix()
rewards = []
for throw in range(3):
    current_points = 0

    row, col = input().strip('()').split(', ')
    row = int(row)
    col = int(col)

    if not 0 <= row < 6 or not 0 <= col < 6:
        continue
    if matrix[row][col] == 'B':
        matrix[row][col] = 0
        for row in range(6):
            current_points += int(matrix[row][col])
    score += current_points

if 100 <= score < 200:
    rewards.append('Football')
elif 200 <= score < 300:
    rewards.append('Teddy Bear')
elif score >= 300:
    rewards.append('Lego Construction Set')

if rewards:
    print(f"Good job! You scored {score} points, and you've won {''.join(rewards)}.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")

