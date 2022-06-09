names = input().split(', ')

data = input()
heroes = {}
while not data == 'End':
    name, item, price = data.split('-')
    if name not in names:
        data = input()
        continue
    if not heroes.get(name):
        heroes[name] = {}

    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})

    heroes.update()
    data = input()

print([f"{name} -> Items: {len(inventory)}, Cost: {sum([inventory[item] for item in inventory])}" for name, inventory in heroes.items()], sep='\n')


# not finished, too lazy for that
