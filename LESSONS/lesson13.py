
import random
class Person():
    def __init__(self,name,age,heigth,weight):
        self.name = name
        self.age = age
        self.height = heigth
        self.weight = weight
class Student(Person):
    def __init__(self, name, age, heigth, weight):
        super().__init__(name, age, heigth, weight)


'''
class Name():
    def __init__(self, name):
        self.__hidden_name = name
    def get_name(self):
        print('getter')
        return self.__hidden_name
    def set_name(self, name):
        print('setter')
        self.__hidden_name = name
    name = property(self.get_name, self.set_name)
n = Name('EGOR')
n.name = 'IGOR'
'''

'''
class Counter():
    __hidden_counter = 0
    def count(self):
        self.__hidden_counter += 1
    def counter_to_zero(self):
        self.__hidden_counter = 0
    def get(self):
        return self.__hidden_counter
    def set(self,n):
        self.__hidden_counter = n
n = Counter()
n.count()
print(n.get())
'''
'''
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Parent(Person):
    def __init__(self, name, age, hair, eyes, par_1, par_2):
        super().__init__(name, age)
        self.hair = hair
        self.eyes = eyes
class Child(Person):
    def __init__(self, name, age, par_1, par_2):
        super().__init__(name, age) 
        self.par_1 = par_1
        self.par_2 = par_2
    hair_1, eyes_1 = par_1.hair, par_1.eyes
    hair_2, eyes_2 = par_2.hair, par_2.eyes
    self.hair = random.choice([hair_1, hair_2])
    self.eyes = random.choice([eyes_1, eyes_2])
p1 = Parent('EGOR')
P2 = Parent('MASHA')
child = Child(age)
'''

class Car():
    type = 'Car'
    def __init__(self,speed):
        self.speed = speed
class Ferrari(Car):
    model = 'Ferrari'
    def __init__(self, speed):
        super().__init__(speed)
class Lada(Car):
    model = 'Lada'
    def __init__(self, speed):
        super().__init__(speed)
Lada = Lada(70)
Ferrari = Ferrari(90)
finish = 1000
pos_l = 0
pos_f = 0
while (pos_l < finish and pos_f < finish):
    pos_l = Lada.speed
    pos_f = Ferrari.speed
print('Ferrari') if pos_f > pos_l else print('Lada')

        
