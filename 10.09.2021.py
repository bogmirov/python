import string
s = string.ascii_lowercase
list_ = [c for c in s]
def f2(list_):
    i = 0
    while i < len(list_):
        print(list_[i])
        i += 1

f2(list_)


def dec(leng):
    def new_leng(*args,**kwargs):
        print('Running function: ', leng.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        result = leng(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_leng

f2_dec = dec(f2)

f2_dec(list_)

