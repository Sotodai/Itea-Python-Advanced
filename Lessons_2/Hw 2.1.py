# 1. Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Реализовать метод для user-friendly вывода информации об автомобиле.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_method(self):
        print('Скорость: ', self.speed, '\nЦвет: ', self.color, '\nИмя: ', self.name, '\nПолицейская: ',self.is_police)

    def go(self):
        print('Машина едет вперёд')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def turn_left(self):
        print('Машина повернула налево')

    def turn_right(self):
        print('Машина повернула направо')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_method(self):
        super().show_method()
        if(self.speed > 60):
            print('Превышение скорости\n')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_method(self):
        super().show_method()
        if(self.speed > 40):
            print('Превышение скорости\n')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

mycar0 = TownCar(70, 'Red', 'Yaroslav', False)
mycar1 = WorkCar(55, 'Yelow', 'Maksim', True)

mycar0.show_method()
mycar1.show_method()