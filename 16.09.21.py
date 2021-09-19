d ={}

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




def add_to_book():
    while True:
        name = input('Введите ваше имя - ')
        if name == 'q':
            break
        phone = input('Введите ваш телефон - ')
        if valide_number(phone) != True :
            t = ['Неверный номер телефона!!']
            print(*t, sep = '\n')
            return False
        d[name] = phone
    return d

print(add_to_book())