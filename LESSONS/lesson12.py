
''''
n = 0
def f(n):
    print(n)
    if n > 0:
        f(n-1)
def  factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''
def diriders(n,div = 1, all_divs = []):
    if n == div:
        all_divs.append(div)
        return all_divs
    elif div < n:
        if n % div == 0:
            all_divs.append(div)
        return diriders(n, div=div + 1, all_divs = all_divs)
    else:
        print('Невверно')