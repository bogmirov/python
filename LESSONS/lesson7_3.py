import string
from typing import DefaultDict
d = {}
d = {'mango': 1, 'pow-pow': 2} 
d1 = {'helmet': 5, 'ascii': 6} 
{'mango': 1, 'pow-pow': 2}
d['mango'] = 1
d['pow-pow'] = 2
d['soul'] = 3
def ascii_upper():
    return {chr(i): i for i in range(65, 91)}

def counter(s):
    d={}
    for ch in string.ascii_lowercase:
        d[ch]=s.count(ch)
    return d
print(counter('aaaaaaaaaabbbbbbbbbcccccccccdddddddd'))

