a = int(2)
b = str(1)
c = int(0)
k = "{2:d}+{1:s}+{0:x}".format(a,b,c)
print(k)


a = int(2)
b = int(1)
c = str(0)
e = "{2:^10s}{1:^10x}{0:^10x}".format(a,b,c)
print(e)


a = int(0)
r = "{0:>100}".format(a)
print(r)