import random

a = random.randint(1, 8)
b = chr (random.randint(65 , 90))
def small(num = 1):
    for index in range(a):
        i = random.randint(97, 122)
        return chr(i)

c = 0
while c < a:
    b += small(a)
    c += 1
print(b)    