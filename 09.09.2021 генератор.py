import random

words = ['a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'w']


def generation_name(words,num):
    i = 1
    while i < num :
        name = ''
        for x in range(0, 3):
            name += random.choice(words)

        yield name
        i += 1
for name in generation_name(words,5):
    print(name)