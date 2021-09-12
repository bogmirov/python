import random
import string
f = string.ascii_letters
def create_str(width):
    s = ' '
    for i in range(len(width)):
        c = random.choice(string.ascii_letters)
        s += c
    return s



def cont_str(s):
    big = 0
    small = 0
    for  sum in s:
     if sum.isupper():
        big += 1
    else:
        small += 1
    if big > small:
         return 1
    elif small > big:  
         return 0
    else:
        return -1    


def procent_str (width, num):
    a = [create_str(width) for i in range(num) ]
    s = ''
    big = 0
    small = 0
    statb = 0
    stats = 0
    statr = 0
    for el in a:
        s += el
        s += ' '
        for i in el:
            if i.isupper():
                big += 1
            else:
                small += 1
        if big > small:
            statb += 1
            s += '1'
        elif small > big:
            stats += 1
            s += '0'
        else:
            statr += 1
            s += '-1'
        
        s += ' '
    s += '> A ' + str(statb/(statb+stats+statr)*100) + '% '
    s += '> a ' + str(stats/(statb+stats+statr)*100) + '% '
    s += 'a == A ' + str(statr/(statb+stats+statr)*100) + '%'
    return s

print (procent_str(f, 5))






