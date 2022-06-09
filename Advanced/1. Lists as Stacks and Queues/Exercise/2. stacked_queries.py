n = int(input())
stack = []


for _ in range(n):
    command = input()
    cmd_info = command.split(' ')
    type_of_cmd = int(cmd_info[0])

    if type_of_cmd == 1:
        num = int(cmd_info[1])
        stack.append(num)

    elif type_of_cmd == 2:
        if stack:
            stack.pop()

    elif type_of_cmd == 3:
        print(max(stack))

    elif type_of_cmd == 4:
        print(min(stack))

stack = [str(el) for el in stack]
stack = reversed(stack)
print(', '.join(stack))

