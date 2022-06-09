import re


def replace_symbols(line):
    return re.sub(r"[\?,\!\.-]", "@", line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row_number in range(len(lines)):
        if row_number % 2 == 0:
            replaced = replace_symbols(lines[row_number]).split()
            print(" ".join(replaced[::-1]))
 # to_replace = {"-", ",", ".", "!", "?"}
#
# with open('text.txt', 'r') as file:
#     counter = 0
#     for line in file.readlines():
#         if counter == 0 or counter % 2 == 0:
#             for i in range(len(line)):
#                 if line[i] in to_replace:
#                     line[i] = '@'
#             to_print = line.split()
#             print(" ".join(to_print[::-1]))
#         counter += 1
