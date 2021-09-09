import random
while True:
    def duplication(x):
        i = random.randint(1, 1000)
        return x*i
    name = input('введите имя для размножения')
    print(duplication(name)) 