'''
def f(n,m):
    print(n)
    if n > m:
        f(n-1,m)
    else:
        return n
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(4))
'''

def div(n, kol=0, array=[]):
    if kol > n/2:
        array.append(n)
        return array
    if kol == n:
        return array
    else:
        kol +=1
        if n % kol == 0:
            array.append(kol)
            return div(n, kol, array)
        else:
            return div(n, kol, array)
x = int(input('делители какого числа вас интересуют? '))
print(div(x))


def space(n,i=0):
    s = str(n)
    print(s[i])
    return s[i] if i ==len(s)-1 else space(s,i = i+1)
space(int(input()))