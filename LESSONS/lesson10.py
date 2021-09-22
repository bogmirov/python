

'''
class Summator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def return_sum(self):
        return self.a + self.b
s = Summator(1,3)
s.return_sum()
print(Summator) 
'''


'''
class Car():
    def __init__(self):
        pass
    def what_is_this(self):
        print('I am a car')
class Pink_car(Car):
    def what_color(self):
        print('Pink')
Pink_car = Pink_car()
Pink_car.what_is_this()
Pink_car.what_color()
print(Car)
'''

class Person():
    def __init__(self,name):
        self.name = name
    def exclaim(self):
        print('Я человек',self.name)
class Student(Person):
    def exclaim(self):
        print('Я человек',self.name, 'Но я хочу спать больше')


class Person():
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print('Удалён объект', self)
p = Person('Egor')
p.__del__()

class Student(Person):
    homework = 0
    kn = 0
    def get_kn (self):
        self.kn += 1
    def get_homework(self,n):
        self.homework += n
    def do_homework(self):
        if self.homework > 0:
            self.homework -= 1
            self.homework += 1
        else:
            print('Нечего делать')

class Teacher(Person):
    work = 0
    
    def give_kn(self,*pupils):
        for pupil in pupils:
            pupil.get_kn()
            self.work += 1
    def give_homework(self,*pupils,n):
        for pupil in pupils:
            pupil.get_homework(n)
            self.work += 1
t = Teacher(' ')
p = Student[Student(' ') for _ in range(n)]
p = Student('Masha')
t.give_kn(p)
print(p,kn)
                


