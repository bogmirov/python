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