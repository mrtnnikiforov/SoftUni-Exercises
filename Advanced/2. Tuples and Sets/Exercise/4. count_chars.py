text = input()

symbols = {}

for char in text:
    symbols[char] = text.count(char)

for (k, v) in sorted(symbols.items(), key=lambda x: x[0]):
    print(f'{k}: {v} time/s')

