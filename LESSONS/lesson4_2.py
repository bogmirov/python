import string


l1 = list(string.ascii_lowercase)
l2 = []
for c in string.ascii_lowercase:
    l2.append(c)
l3 = [c for c in string.ascii_lowercase]
print(list(string.ascii_lowercase))