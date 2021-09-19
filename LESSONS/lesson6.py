from random import randrange, randint, random
elements = []
list_ = []
for i in range(100):
    elements.append(randint(-50, 50))
def sort_list(elements):
    for i in range(len(elements)):
        for j in range(len(elements)-i-1):
            if elements[j] < elements[j + 1]:
                elements [j], elements [j + 1] = elements[j + 1], elements[j]
    return elements   

def create_list(length,minimum,maximum):
    list_=[]
    for i in range(length):
        list_.append(randint,maximum,minimum)     
    return list_



s = (input())
def get_format(s):
    l = s.split('.')
    if len(l) < s:
        return 'Invalid'
    else:
        return '.' + l[-1]

def generate_list(num, minimum, maximum):
    i = 0
    while i < num:
        yield random.randrange(minimum, maximum)
        i += 1
def sort_3(elements):
    return elements.sort()
list_ = [i for i in generate_list(30, 0, 40)]   
print(generate_list,sort_3)      

