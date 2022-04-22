
"""Представление переменных"""

#first_name = int(input("Enter first namber: "))
#second_number = int(input("Enter second number: "))
#print(first_name + second_number)                           # вывод суммы двух чисел


# Изменение строки
 
a = "hello world"
b = a + ", everyone"
print(a)
print()

print("id(a) = " + str(id(a)))
print("id(b) = " + str(id(b)))                                # разные id
print()


# Вызов листа
print(list())
print()

print([])
print()

print([1, 2, 3, 4, 5])
print()

# list() = [] - равнозначно

print([a, b])                                                 # выведет 2 элемента а имено "hello world", "hello world, everyone"
print()

test_list = [a, b]
print(test_list)
print("id(test_list) = " + str(id(test_list)))
print()

test_list.append(5)
print(test_list)
print("id(test_list) = " + str(id(test_list)))                # ячейка памяти не изменяется в листе даже при добавлении
print()


test_list.append([1, 2, 3,])
print(test_list)
print("id(test_list) = " + str(id(test_list)))
print()


# Type (тип данных)

print(type(a))                                                # <class 'str'>
print(type(2))                                                # <class 'int'>
print(type(True))                                             # <class 'bool'>
print(type([]))                                               # <class 'list'>
print()

# Изменение индикации листа

e = 32
d = 45
print("id(a) = " + str(id(a)))
print("id(b) = " + str(id(b)))  

# Комментарии

# что бы за коментировать весь код или часть нужно выделить и нажать Ctrl + / (возле ю (справа))


# TODO

# Эта заметка используется для быстрого поиска контента. Например:
# TODO провести рефакторинг

# Документация и правила оформления
# Пример:

def func_random():
    '''Функция для угадывания числа'''
    while True:
        if int(input('Enter number: ')):
            print("Lucky Boy")
            break
        else:
            print("No man!")

func_random()                                                    # при наведении курсора на фукцию мы увидим документацию """Функция для угадывания числа"""