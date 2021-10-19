'''class Name():
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        sels.__n= new_name
st = Name("Ivan")
try:
    print(st.__name)
except AttributeError:
    print("---ОШИБКА---")
print(st.get_name())
class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,new_name):
        self.__name = new_name
    def set_age(self,new_age):
        self.__age = new_age
name = str(input("Как зовут человека? "))
age = int(input("сколько ему/ей лет? "))
print(name.get_name())
print(age.get_age())
'''


#игра
class Pol:
    __pos_h = 0
    __pos_t = 0
    def __init__(self, n, m, x):
        if n <=m:
            print("неверный данные")
            return "break"
        self.__step_h = n
        self.__step_t= m
        self.__lenth = x
    def get_place_h(self):
        return self.__pos_h
    def get_place_t(self):
        return self.__pos_t
    def value(self):
        self.__pos_h += self.__step_h
        self.__pos_t +=self.__step_t
        if self.__pos_h >= self.__lenth:
            while self.__pos_h > self.__lenth:
                self.__pos_h = self.__pos_h - self.__lenth -1
        if self.__pos_t >= self.__lenth:
            while self.__pos_t > self.__lenth:
                self.__pos_t = self.__pos_t - self.__lenth - 1            
    def set_places(self,new_step_t):
        self.new_step_t = new_step_t
        return self.new_step_t



n = int(input('сколько клеток пробегает кролик за 1 ход? '))
m = int(input('сколько клеток пробегает черепаха за 1 ход(меньше чем кролик)'))
x = int(input('сколько клеток в круговом поле? '))
c = 0 #сколько раз встретяться кролик и черепаха
kol_xod = repeat = 0
field = Pol(n,m,x)
while True:
    prt = input("новый ход? ('q'чтобы прекрастить)/(смена ходов) ")
    if prt == "смена ходов":
        n = field.set_places(int(input('сколько клеток пробегает кролик за 1 ход? ')))
        m = field.set_places(int(input('сколько клеток пробегает черепаха за 1 ход(меньше чем кролик)')))
        kol_xod = 0
    if prt == "q":
        break
    else:
        kol_xod +=1
        field.value()
        print(field.get_place_h())
        print(field.get_place_t())
        if field.get_place_h() == field.get_place_t():
            repeat_xod = kol_xod
            repeat +=1
            print('они встретились через ', repeat_xod, "ход")
            c+=1
print('всего ходов: ', kol_xod)
print("сколько раз встретились соперники: ", c)
print('сопреники встречаються в одной точке каждый', repeat_xod/repeat, 'ход')