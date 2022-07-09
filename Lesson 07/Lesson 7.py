# Классы


class Car:                                                    # класс начинается с class и с большой буквы имя класса Car 
    """Классы машины"""
    color = "red"
    max_speed = 240                                           # color, vin_number и max_speed - свойства класса 
    vin_number = 'q1w2e3r4'

    def drive(self, speed: int):                              # self(аргумент) - это обращение к экземпляру класса. speed - это аргумент
        """Метод движения"""
        print(f'Машина едет со скоростью {speed} км/ч')
        self.info                                             # даже если info  ниже мы можем вызвать этот метод 

    def info(self):                                           # drive b info - это объекты(методы)
        """Информация о машине"""
        print(self)                                           # ячейка памяти будет одна и таже пока мы будем обращаться к Car, но если мы обратимся например Car2 - другая
        print(
            f'Я машина мой цвет {self.color}.'
            f' Максимальная скорость {self.max_speed} км/ч'
            )
        self.drive

    def _private_info(self):                                  # нижнее подчеркивание говорит о том что метод нельзя использовать извне. 
        """Приватная информация"""
        print(f'VIN: {self.vin_number}')                      # Программа все равно выведет его но выведет информацию что это приватный метод.
                                                              # def __private_info(self): -если мы добавим еще одно подчеркивание то выведет ошибку 


car = Car()                                                   # что бы обратиться к объектам класса сначала нужно вызвать сам класс.
car.drive(10)
car.info()
print()

print(car.color)                                              # что бы изменить цвет машины (свойство переменной)
car.color = 'green'
car.info()
print()

# Ячейка памяти не соответствует первоначальной т.к. Car2
car2 = Car()
car2.info()
car2.max_speed = 390                                          # изменяем максимальную скорость данной машины
car2.info()
print()

# Наследование
"""
Наследование позволяет создавать новый класс на основе уже существующего класса. 
Наряду с инкапсуляцией наследование является одним из краеугольных камней объектно-ориентированного программирования.
Ключевыми понятиями наследования являются подкласс и суперкласс. Подкласс наследует от суперкласса все публичные атрибуты и методы. 
Суперкласс еще называется базовым (base class) или родительским (parent class), 
а подкласс - производным (derived class) или дочерним (child class).
"""

class Mercedes(Car):                                          # mercedes - это дочерний класс, родительским является Car. Указывается дочерний(родительский)
    color = "black"                                      
    max_speed = 320

    def __init__(self, color: str = 'black'):                 # по умолчанию будет black но мы можем указать другой цвет  - называется "магическим" методом. __init__ - конструктор.
        self.color = color

    def drive(self, speed: int = 0):
        print(f'Машина едет со скоростью {speed} км/ч')
        self.info

    def __gt__(self, other):                                  # метод сравнения
        return self.max_speed > other.max_speed                                            

"""Нам не нужно заново указывать их объекты (методы), а вот свойства мы их можем указать новые"""
# Изменение методов

print("mercedes")
mercedes = Mercedes()
mercedes.info()
print() 
    
# Полиморфизм
"""
Полиморфизм — очень важная идея в программировании. 
Она заключается в использовании единственной сущности(метод, оператор или объект) 
для представления различных типов в различных сценариях использования.
"""
class Lada:

    def drive(self, speed: int = 0):
        raise Exception(f'Ты что она совсем не едет! Вот скорость {speed}')

# cars = [
#         mercedes,
#         car,
#         Lada()
#     ]

# for car in cars:
#     car.drive()

# Приватные методы (Инкапсуляция) 
"""
Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным). 
Инкапсуляция делает некоторые из компонент доступными только внутри класса.
"""

# def _private_info(self):


# Приватные методы нужно только для информирования о том что их изменять не нужно

mercedes._private_info()                                        # вызов приватного метода
print()


# Магический метод
mercedes = Mercedes(color='white')                              # указываем цвет с помощью __init__ в методе (стандарт = black)
mercedes.info()
print()

# Метод сравнения
print(mercedes>car)                                             # return self.max_speed > other.max_speed  - тут other - car
print()