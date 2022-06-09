rows, cols = [int(el) for el in input().split()]


def is_command_valid(command):
    cmd_info = command.split()
    if cmd_info[0] == 'swap':
        if 0 <= int(cmd_info[1]) < rows and 0 <= int(cmd_info[2]) < cols:
            if 0 <= int(cmd_info[3]) < rows and 0 <= int(cmd_info[4]) < cols:
                return True

    print()
    print('Invalid input!')
    return False


def print_matrix(matrix):
    for r in range(rows):
        if not r == rows:
            print()
        for c in range(len(matrix[r])):
            print(matrix[r][c], end=' ')


matrix = []

for r in range(rows):
    matrix.append(input().split())

end_command = 'END'
command = input()
if command == '':
    print('Invalid input!')
    command = input()
while command != end_command:
    cmd_info = command.split()
    if is_command_valid(command):
        matrix[int(cmd_info[1])][int(cmd_info[2])], matrix[int(cmd_info[3])][int(cmd_info[4])] = matrix[int(cmd_info[3])][int(cmd_info[4])], matrix[int(cmd_info[1])][int(cmd_info[2])]
        print_matrix(matrix)
    command = input()


