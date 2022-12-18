phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def change_contact(id):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы действительно хотите изменить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id - 1)
        return True
    return False

def find_contact(name):
    global phone_book

def input_find_contact():
    name = input('Введите имя контакта для поиска: ')
    name = [name]
    for i in phone_book:
        if name == i:
            print([i], {phone_book})




