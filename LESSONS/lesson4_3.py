import string
s = string.ascii_lowercase
list_ = [c for c in s]
def f2(list_):
    i = 0
    while i < len(list_):
        print(list_[i])
        i += 1

f2(list_)


