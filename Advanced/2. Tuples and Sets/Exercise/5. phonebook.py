def fill_phone_book():
    data = input()

    phone_book = {}

    while not data.isdigit():
        name, phone_number = data.split('-')
        phone_book[name] = phone_number
        data = input()
    return phone_book, data

def search_contact(contact_name):
    if phone_book.get(contact_name):
        print(f'{name} -> {phone_book[contact_name]}')
    else:
        print(f'Contact {name} does not exist.')


for _ in range(int(data)):
    name = input()
    search_contact(name)


