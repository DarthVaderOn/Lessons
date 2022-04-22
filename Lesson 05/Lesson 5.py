# Практика с циклами и функциями.

# Функция для умножения чисел в диапазоне

from functools import reduce


def factorial(number: int) -> int:
    """Вычисление факториала
    
    Input deta: 5
    result: 120
    1 * 2 * 3 * 4 * 5 = 120"""

    result = 1
    for i in range(1, number + 1):                    # number + 1 это нужно для того что бы включить 5 в список
        result *= i

    return result


print(factorial(5))
print()


# Функция для определения палиндрома

def is_palindrome(word: str) -> bool:
    
    """Вычисляем является ли слова палиндромом.
    
    Пример:
    - топот
    - Кирик
    - тут
    - ротатор
    - летел
    - радар
    - А роза упала на лапу Азора
    """
    # resersed_word = word[::-1]
    # if word == resersed_word:
    #     return True
    # else:
    #     return False

    i = 0
    j = len(word) - 1  # мы делаем -1 потому что:
    # word = 'mom'
    # word[0] = m
    # word[1] = o
    # word[2] = m
    # word[4] = error                                 

    while i <= j:
        print(f'{i=}; {j=}; {word[i]=}; {word[j]=}')        # показываем как идет сравнение
        if word[i] != word[j]:
            return False
        
        i += 1
        j -= 1

    return True

# Что бы заработало раскоменьть 
    
# while True:


#     palindrome_word = input("Enter any word: ").lower()     # lower() - выравнивает по нижнему регистру (т.е. все буквы меленькие)
#     print(is_palindrome(palindrome_word))


# Генераторы

def custom_range(stop_number: int):
    current_number = 0

    while current_number < stop_number:
        yield current_number                     # yield - возращает значение которое можно использовать в итерации
        current_number += 1


# for i in custom_range(8):                      # [0, 1, 2, 3, 4, 5, 6, 7]
#     print(i)

gen = custom_range(8)                            # генерирует числе указанные в диапазоне от 0
print(next(gen))                                 # 0
print(next(gen))                                 # 1
print(next(gen))                                 # 2
print(next(gen))                                 # 3
print()

# Не путать !

lst = [i for i in range(8)]                      # это лист он генирирует список, но не генирирует как в генераторе + отличие в скобках [] - list and () - generator
print(lst)
print()


unknown_rariadle = (i for i in range(8))         # () - generator
print(unknown_rariadle)                          # выведет что он является генератором "<generator object <genexpr> at 0x0000022EE9472180>"
print()

# set

a = {1, 2, 3, "a", 3, 1, 5, 4}                    # уникальные значения выявляет (большие бкувы, пробелы и символы)
print(a)                                          # <class 'set'>
print() 
a.update([1, 2, 3, "a", 3, 1, 5, 4, None,'А роза упала на лапу Азора', ()])
print(a)
print(type(a))
print() 

b = frozenset('А роза упала на лапу Азора')      # уникальные значения выявляет (большие бкувы, пробелы и символы) но функция update не работает
print(b)
print(type(b))                                   # <class 'frozenset'>
print()

# None

a = None                                         # None - ничего (возвращение ничего)
print(a)
print()

def test_func():
    return

print(test_func())
print()

# IS

print([] is [])                                   # is сравнивает 2 объекта - False (т.к. разные id ячеек)
print()

# Lambda 
# #map filter reduce

lambda x: x**2                                              # нужна для минимилизации функции, выводит то что будет после :
# map
result = list(map(lambda x: x**2, [1, 2, 3, 4]))            # map - применяется в функции к каждому элементу в списке (словаря)
print(result)
print()

# filter
result = list(filter(lambda x: x%2==0, [1, 2, 3, 4]))       # filter - отфильтровывает согласно условию в списке (словаря)
print(result)
print()

# reduce
result = reduce(lambda prev, curr: prev * curr, range(1, 6))   # reduce - принимает 2 аргумента: функцию и последовательность и применяет их в списке.
print(result)
print()