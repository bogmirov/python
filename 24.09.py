'''f = open('Python.txt', 'a')
f.write('[I think, you are the best] ')
f.close()
f = open('Python.txt', 'r')
print(f.read())
f.close()
books = ['если ты понял, то ты молодец']
f = open('Python.txt','a')
f.writelines(books)
f.close()
f = open('Python.txt', 'r')
print(f.read())
f.close()
f = open('Python.txt', 'w')
f.write('how are you? \nI"m fine')
f.close()
f = open('Python.txt','r')
print(f.read())
f.close()'''

ip = { }
f = open('Python.txt','r')
x = f.readlines()
z = 0
for i in range(len(x)):
    if i % 2 == 0:
        y = x[i][:-1]
    
    else:
        if i !=len(x):
            z = x[i]
        else:
            z = x[i][:-1]
    ip[y] = z
print(ip)
f.close()
