materials = [int(x) for x in input().split()]
magic_levels = [int(x) for x in input().split()]

gifts = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic_levels:
    present_value = materials[-1] + magic_levels[0]

    if present_value < 100:
        if present_value % 2 == 0:
            present_value = (materials[-1] * 2) + (magic_levels[0] * 3)
        else:
            present_value *= 2

    if present_value > 499:
        present_value /= 2

    if 100 <= present_value < 200:
        gifts['Gemstone'] += 1
        materials.pop()
        magic_levels.pop(0)
        continue

    elif 200 <= present_value < 300:
        gifts['Porcelain Sculpture'] += 1
        materials.pop()
        magic_levels.pop(0)
        continue

    elif 300 <= present_value < 400:
        gifts['Gold'] += 1
        materials.pop()
        magic_levels.pop(0)
        continue

    elif 400 <= present_value < 500:
        gifts['Diamond Jewellery'] += 1
        materials.pop()
        magic_levels.pop(0)
        continue

    if materials and magic_levels:
        materials.pop()
        magic_levels.pop(0)

if gifts['Gemstone'] >= 1 and gifts['Porcelain Sculpture'] >= 1 or gifts['Gold'] >= 1 and gifts[
    'Diamond Jewellery'] >= 1:
    print('The wedding presents are made!')
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")


for key, value in sorted(gifts.items()):
    if value > 0:
        print(f'{key}: {value}')

