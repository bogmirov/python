'''
l = [0, 1]
try:
    l[2]
except IndexError as err:
    print('Неверный индекс',err)
else:
    print('Всё OK!')
'''


 #Типы ошибок 
 # TypeError: '1' + 1
 # IndexError l[2]  <l[0, 1]>
 # ZeroDivisionError   1/0

a = 2
b = 'Hello'
try:
    a + b
except TypeError as err:
    print('Неверный тип данных',err)
else:
    print('Всё норм!')



try:  
    a = 100 / 0
    print(a)
except ZeroDivisionError as err:  
    print('На ноль делить нельзя!',err)
else:
    print('wow')


a = 'Hello'
try:
    a[10]
except IndexError as err:
    print('Неверный индекс',err)
else:
    print('OK')   










 