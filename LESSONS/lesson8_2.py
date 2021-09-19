
def valide_number(p):
    if len(p) != 16:
        return False
    if p[0:3] != '+7-':
        return False
    if p[6] != '-' or p[10] != '-' or p[13] != '-':
        return False
    ap = p[3:6] + p[7:10] + p[11:13] + p[14:16]
    digits = '0123456789'
    for sym in ap:
        if not sym in digits:
            return False
    return True
d = {}
def add_to_book(name, phone):
    d[name] = phone
 
while True:
    name = str(input('Введите имя:'))
    if name == 'q':
        print(d)
        break
    phone = str(input('Введите номер:'))
    if phone == 'q':
        print(d)
        break
    if valide_number(phone):
        print('Number is okay, adding to book...')
        add_to_book(name,phone)
        print('New phone added')
    else:
        print('Number is incorrect, please give another')

    
