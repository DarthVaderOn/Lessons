# Функции For and While. Вызов функии и понятие области видимости (глобальное и локальное).

# For
# Функция For выполняет основное условие заданное в range (начало диапазона, его предел, шаг).
 
sum_number = 0 
for number in range(5):          # выведет список начиная от 0 т.е. - 0, 1, 2, 3, 4
    sum_number += number         # суммирует кажое число заданное в списке 0 + 1 + 2 + 3 + 4
    
print(sum_number)                # индентично если бы мы записали print(sum([0, 1, 2, 3, 4]))
print()

# если мы зададим в range (1, 5) то нумерация будет с 1 т.е. - 1, 2, 3, 4
for number in range(1, 5):
    print(number)
print()

# если мы зададим в range (1, 5, 2) то нумерация будет с шагом 2 т.е. - 1, 3
for number in range (1, 5, 2):
    print(number)
print()

values_a = [0, 1, 2, 3, 4]
for number in values_a:
    if number == 2:              # при выводе, 2 мы исключаем
        continue                 # когда мы дойдем до двойки мы ее пропускам (не выводим) но продожам без нее список
    print(number)
print()

values_b = [0, 1, 2, 3, 4, 5, 6, 7]
for number in values_b:
    if number == 6:             
        break                   # когда мы дойдем до шестерки программа остановится и не выведет дальше список
# else:                         # после того как программа пройдет по списку выведет end 
#   print("end")  
    print(number)
print()


# While 
# While функция которая будет выполняться пока услвие заданное не выполнится

number = 0                      # первоначальное значение 0
while number < 5:               
    number += 1                 # добавляет +1 пока условие не выполнится
print(number)
print()


# Функции и их вызов

def summa(a, b):                # функция с двумя переменными a и b
    return a + b                # return - то что мы будем возвращать, а именно сумму a и b

print(summa(1, 6))
print()
print("Hello", " Alex")
print()


author = "Chester"              # author - это глобальная область видимости (в функции она будет неизменная) т.к. находится до вызова функции.
def welcome_message(name):      # name - это локальная область видимости (в функции она будет изменяемая) т.к. находится и вызвается в функции.
    value = f'Hello, {name} ! How are you ? \nThe program author is {author} !' 
    return value

print(welcome_message("Ben"))
print()
print(welcome_message("Chack".__add__(" Noris")))    # можем добавлять строку с помощью __add__() что равносильно + "Noris"
print()


def moda(a=0, b=0):              # мы можем задать любые стоковые значения в функции если мы не присвоим стоковые значения выдаст ошибку:    
    print(f'{a}; {b}')           # TypeError: moda() missing 2 required positional arguments: 'a' and 'b'
    return a + b                 

# def moda(a="yes", b="no")      # мы можем задать стандартное значение и строковое


print(moda())                    # не присваиваем ничего
print()
print(moda(b=50))                # присваем определенной переменной b значение
print()
print(moda(a=13))                # присваем определенной переменной a значение
print()
print(moda(77))                  # присвоется первой переменной значение
print()


# Подсказки в функциях

def primer(a: int = 1, b: float = 2, c: str = 3) -> int:       # в подсказке (при наведении курсора на переменную) будет высвечиваться определенный тип данных но присвоить можно любой
    return a + b + c 
# -> int - это говорит о том при выводе этой функции будет формат int
print(primer())
print()


# Немного о range


print(list(range(8)))
print(list(range(1, 8)))
print(list(range(1, 10, 1)))
print(list(range(-1, -10, -1)))
print(list(range(0)))
print(list(range(1, 0)))
