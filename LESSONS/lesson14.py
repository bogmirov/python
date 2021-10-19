from typing import ValuesView


f = open ("1.txt","r")
print(f.read())
f.close()

#f = open('D:\\homework\\1.txt', 'w')
#f.write()
#f.close()

f = open('2.txt', 'a')

f = open('1.txt', 'r')
print(f.readline)
f.close()

#f = open('2.txt', 'w')
#f.writelines('fffffffff')
#f.close()


f = open('2.txt', 'r')

dic = {} 

lines = f.readlines()
for line in lines:
    key, value = line.split(': ')
    dic.update({key:value})
print(dic)
