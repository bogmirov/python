list_ = [1, 1, 2, 2]
g = set(list_)
d = set('aabbcc')

a = [1, 1, 2, 2, 4, 5]
b = [9, 8, 7, 6, 5, 4]
def unique(a):
    return list(set(a))


def intersection_lists(a, b):
    a, b = set(a), set(b)
    return list(a & b)

print(intersection_lists(a, b))