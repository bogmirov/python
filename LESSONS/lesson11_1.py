class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
 
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        self.__age = new_age
         
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
pip = Person('Каменьщик', 20)
pip.set_age(20)


class Field():
    __pos_hare = 0
    __pos_tort = 0
    def __init__(self,h,m,x):
        if h <= m:
            print('Неверные данные')
            return
        self.__step_hare = h
        self.__step_tort = m
        self.__length = x
    def get__pos_hare(self):
        return self.__pos_hare
    def get_pos_tort(self):
        return self.__pos_tort
    def step(self):
        hare_new_pos = self.__pos_hare + self.__step_hare
        if hare_new_pos > self.__length:
            hare_new_pos -= self.__length
        self.__pos_hare = hare_new_pos

        tort_new_pos = self.__pos_tort + self.__step_tort
        if tort_new_pos > self.__length:
            tort_new_pos -= self.__length
        self.__pos_tort = tort_new_pos
f = Field(5, 2, 11)
i = 0
first_meet = 0
while(i < 100):
    f.step()
    i += 1
    if f.get__pos_hare() == f.get_pos_tort():
        print('Они встретились через',i - first_meet)
        first_meet = i
    

