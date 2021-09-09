names = ['Spiridonov Bogdan Valerevich', 'Vladimir Vladimirovich Putin ']
def initials(names):
    l = names.split()
    return l[0] + ' ' + l[1][0:1] + ' ' + l[2][0:1] + ' '
def initials_move(names):
    result = []
    for name in names:
        new_name = initials(name)
        result.append(new_name)
    return result   
print(initials_move(names))