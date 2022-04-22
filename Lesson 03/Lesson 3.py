 # div and mod

 # div - целое деление без остатка
print(5//2)
 # mod - выводит остаток после деления
print(100%30) 

print()


# Операторы присвоения

# ==
print(True == 1) 
# т.к. True = 1 а False = 0

# !=
print(5!=6)

# >
print(1>0)

# <
print(0<-0)

# >=
print(5>=10)

# <=
print(-9<=2)

print()


# Оператор присваивания

a = "Hello World"
a += " say Alex ! "
print(a)

number = 10
number -= 4
print(number)


a = 8
a *= 2
print(a)


b = 9
b /= 3
print(b)


c = 7
c //= 2 
print(c)


d = 10
d %= 3
print(d)

print()


# Форматировние строк

# name = input("Enter your name: ")
# print(f'Hello, {name}')

print(f'number = {number}; a = {a}')
# or
print(f'{number = }; {a = }')

print("number = {}; a = {}".format(number, a))
print("number = {1}; a = {0}".format(number, a))                  # где 1 и 0 порядок

print()

# If, elif, else

one_number = input("Enter your number: ") 

if one_number == "secret":                                        # секретное слово которое выходит с программы
    print("You won this game!")
    exit()
elif "46" in one_number:                                          # поиск 46 в тексте
    print("I found 46 in this text")
else:                                                             # если мы не ввели ничего
    print("You didn\'t enter anything")
    one_number = 0

print(type(one_number))


if one_number % 10 == 0:                                          # при делении на 10 без остатка и больше 0
    print("Number end with 0")                                    # отступ называется Табуляция
elif one_number % 5 == 0:                                         # кратное 5 
    print("Number end with 0 or 5")
else:
    print(f"Idk what the number, {one_number = }")