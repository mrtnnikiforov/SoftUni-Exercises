text = input()

VOWELS = {'o', 'u', 'e', 'i', 'a'}
[VOWELS.add(x.upper()) for x in list(VOWELS)]

result = [x for x in text if x not in VOWELS]
print(''.join(result))
