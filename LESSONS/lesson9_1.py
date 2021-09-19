a = [1, 2, 3, 4, 5,]
while True:
    b = int(input())
    if b == 'q':
        break
    c = input()
    try:
        a[b] = c
    except IndexError as err:
        print('Неверный индекс',err)
    else:
        print('Всё в порядке!')