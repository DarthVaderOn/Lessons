# Методы


import os.path
from dataclasses import asdict, dataclass, field
from time import sleep
from time import sleep, time
from unittest import result



class Authenticator:
    def __init__(self):
        self.login: str | None = None
        print(self.is_auth_file_exist('auth.txt'))
 
    @staticmethod                                                             # @staticmethod - это декоратор (статический метод)
    def is_auth_file_exist(filename: str) -> bool:                            # в статическом методе self не неужна
      
            return os.path.exists(filename)                                   # filename - название файла который мы ищем

    @classmethod                                                              # @classmethod -  это метод, который получает класс в качестве неявного первого аргумента
    def read_auth_file(cls):                                                  # cls - 
         return cls()

        
      
if __name__ == '__main__':
    print(Authenticator().is_auth_file_exist('auth,txt'))
    print()                       
    print(Authenticator.is_auth_file_exist('auth,txt'))                       # в статическом методе уже не нужно вызывать сам экземпляр класса а только его название
    print()
    Authenticator.read_auth_file()
    print()

# Пример @classmethod (подсчет экземпляров класса):

class TestCls:
    counter = 0                                                               # атрибут класса

    def __init__(self) -> None:
        self._increment_counter()
    
    @classmethod
    def _increment_counter(cls):
        cls.counter += 1


if __name__ == '__main__':
    for i in range(10):
        TestCls()

    print(TestCls.counter)    
    print()

# Пример 2

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def create_test_cls(cls, x):
        a = x // 10                                                            # кратность 10
        b = x % 2                                                              # выводит остаток после деления
        return cls(a,b)

if __name__ == '__main__':
    test_cls = Test.create_test_cls(55)
    print(test_cls.a, test_cls.b)
    print()


# property (свойства)


class Car:

    def __init__(self):
        self._vin_number = 123
    
    @property                                                                     # @property(свойства) - не дает отредактировать
    def vin_number(self) -> str:
        return  f'Vin number: {self._vin_number}' 
    
    @vin_number.setter                                                            # если нам все же нужно изменить ипользуем @'имя атрибута'.setter
    def vin_number(self, value):
        self._vin_number = value 

if __name__ == '__main__':
    car = Car()
    print(car.vin_number)
    print()

    car.vin_number = '99944664'
    print(car.vin_number)
    print()

# @dataclass 

@dataclass(order=True)                                                           # __init__ и __repr__ а так же другие медоды уже вшиты 
class Student:
    first_name: str = field(compare=False)                                       # field(compare=False) - не сравнивается
    last_name: str = field(compare=False)
    age: int = field(compare=True)                                               # field(compare=True) - сравнивается
    score: int = field(compare=True)

    # Раньше была бы запись без @dataclass:

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # def __repr__(self) -> str:
    #     return f'Data(name={self.name}, age={self.age})'

if __name__ == '__main__':
    student1 = Student('Alex','Vin', 29, 0)
    student2 = Student('Den','Angers', 25, 5)
    student3 = Student('Ben','Zin', 25, 4)

# сравниваем двоих студентов с одинаковым возрастом но с разными баллами

    if student2 > student3:
        print('student2')
    else:
        print('student3')

    print()
    print(student1, student2, student3, sep='\n')                           # в List
    print()
    print(asdict(student1))                                                 # в dict
    print()


# Декоратор (3 вложенности)

def work_time(text):

    def decorator(func):
        print('work_time был вызван')

        def wrapper(*args, **kwargs):                                                      # что бы добавить аргуметы ипользуем *args, **kwargs
            print(f'[{text}] Вызываю функцию {func.__name__}')
            start_time = time()

            result = func(*args, **kwargs)
            print(f'[{text}] Получил результат из функции {func.__name__}:{result} ')

            end_time = time()
            # Время выполнения функции:
            print(f'[{text}] Время выполения функции: {end_time - start_time}\n')

            return result
        return wrapper
    return decorator

# Теперь нам не нужно дублировать код а просто указать условие:
@work_time('sleep')
def main(sleep_time):
    sleep(sleep_time)
    
@work_time('List(range)')
def main2():
    return list(range(2**3))

@work_time('range')
def main3():
    return range(2**7)

if __name__ == '__main__':
     main(0.1)
     main2()
     main3()