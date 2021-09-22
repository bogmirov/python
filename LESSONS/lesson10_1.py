class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_p(self):
        return (self.w + self.h) * 2
    def get_s(self):
        return self.w * self.h
pr = Rectangle(4, 5)



class Circle():
    def __init__(self, r):
        self.r = r
    def get_p(self):
        return 2 * 3.14 * self.r
    def get_s(self):
        return self.r ** 2 * 3.14
    
kr = Circle(5)
#print(kr.get_s())


class Triange():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_p(self):
        return (self.a + self.b + self.c)
    def get_s(self):
        return (self.a * self.b) * 0.5

tr = Triange(13, 21, 15)
print(tr.get_p())
