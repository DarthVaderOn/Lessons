# Debugger
# ctrl + shift + D (VS Code) либо нажимаем слева клавишу 'Запуск и отладка'

''' Выбираем нужную строку и ставим слева от строчки красную точку. Запускаем Debugger.
    Переключаемся с помощью F7 (пошаговая отладка) F8 (глобальная отладка(по отметкам)).
    Alt + F9 - запуск программы до расположения курсора
    Alt + F8 - запуск редактора и поиска
    F9 - возобновить программу '''
import pdb


class Validator:
    name = 'Alex'
    age = 23

    def __init__(self):
        self.data_history: list[Validator] = []


    def _validate_name(self):

        name = self.data_history[-1].name
        return name

    def _validate_age(self):

        age = self.data_history[-1].age
        return age

    def validate(self):

        name = self._validate_name()

        age = self._validate_age()
        return name, age

    print(age, name)
    print()


# Работа отладчика через консоль

b = 10
print(b)
# breakpoint()                                                    # breakpoint() - Функция остановки кода (код выполняется пока не дойдет до этого места)
# pdb.set_trace()                                                 # pdb.set_trace() - работа отладчика через консоль (чтобы заработала раскоменть)
# Команды в консоли отладчика:
# w - выводит место остановки кода
# ll - выводит весь код с отметкой остановки кода
# l - сокращенный вывод 5 строк вверх 5 строк вниз
# n - переход к следующей строке
# j 55 - переход к строчке 55
# help - список всех команд

a = "hello world"
b = a + ", everyone"
print(a)
print()

print("id(a) = " + str(id(a)))
print()


# json (словарь)

import json

data = {
    'name': 'Alex',
    'age' : 23,
    'login' : 'admin',
    'password' : 'admin',
    'extra_data' : [
        'Admin',
        'Moderator',
        'User'
    ],
}

print(data['name'])                         # обращение к ключу name
print(data['age'])                          # обращение к ключу age
print(data['extra_data'])                   # обращение к ключу extra_data
print()

print(json.dumps(data))                     # для вывода всего используем json
print()

with open('user.json', 'wt') as f:
    f.write(json.dumps(data))               # создаем json


# обращение к login через json

with open('user.json') as f:
    parsed_data = json.load(f)
    # parsed_data = json.loads(f, read())   # вторая версия записи

    # json.load - метод считывает файл в формате JSON и возвращает объекты Python
    # json.loads - метод считывает строку в формате JSON и возвращает объекты Python

    print(type(parsed_data), parsed_data)   # убеждаемся что является по типу str
    print()

print(parsed_data['login'])
print()

# with open('user.json', 'wt') as f:        # wt(write text) - запись в тексте
#     f.write(json.dumps(data))

# with open('user.json', 'wb') as f:        # wb(write byte) - запись в байтах
#     f.write(json.dumps(data))


# Регулярные выражения

import re


def regex_example():
    email = '@my_emailmail. ru@my_emailmailru. m@y_emailmail.ru. my_email@mail.ru'

# Проверка была бы раньше без регулярки:

    # if '@' not in email:                    # если нет @ - Ошибка
    #     return False
    #
    # if '.' not in email:                    # если нет . - Ошибка
    #     return False
    #
    # if email.index('@') != 0:               # @ не идет нулевым индексом
    #     return False

# Проверка с регуляркой:

    # для проверки почты используем \w+@\w+\.\w+
    ''' где:
            \w - Любая буква (то, что может быть частью слова), а также цифры и _
            . - Один любой символ, кроме новой строки \n.
            ^ - Начало всего текста или начало строчки текста
            $ - Конец всего текста или конец строчки текста '''

    print(re.match(r'\w+@\w+\.\w+', email))

# Пример 2:

    text = '123g'
    print(re.match(r'\d+', text))             # \d - поиск числа, \d+ поиск всех чисел. Если бы мы поставили D - то это поиск только букв.
    # < re.Match object;span = (0, 1), match = '1' > - где  1 это True
    print()


if __name__ == '__main__':
    regex_example()