from datetime import datetime

# Словарь 'dict' {} set()

def main():
    var_1= {}                                         # первая вариация словаря через {}
    # var_2 = set()                                   # вторая вариация словаря через set()

    var_1['One'] = 1                                  # где One - это ключ, а 1 - значение
    var_1['Two'] = 2                                  # где Two - это ключ, а 2 - значение
    var_1[3] = []                                     # где 3 - это ключ, а [] - значение
    var_1["Four"] = (1, 3, 6, 'blah')                 # где Four - это ключ, а (1, 3, 6, 'blah') - значение

# В ключ и в значение можно добавить все типы данных (var[3] = [])

    print(type(var_1), var_1)
    print()

# Чтобы узнать значение ключа пишем:

    print(var_1['One'])
    print(var_1['Two'])
    print(var_1[3])
    print(var_1["Four"])
    print()
    
# Чтобы узнать какие ключи находятся в словаре:

    print(var_1.keys())
    print()

# Чтобы узнать какие значения ключей находятся в словаре:

    print(var_1.values())
    print()

# Что бы пробежаться по каждому элементу:

    for key, value in var_1.items():                                 # items() возвращает пары (ключ, значение) для каждого элемента словаря.
        print(f'{key=}, {value=}')

    print()    


# Что бы обратиться к определенному значению (например 6) необходимо:

    var_1["Four"] = (1, 3, 6, 'blah')
    print(var_1['Four'][2])
    print()

if __name__ == '__main__':
    main()


# Работа с текстовыми документами (txt) (P.S. вверх лучше закоментить)


def value_line(line):
    print(line)

def text():
    file = open('c:/Python/Уроки TeachMeSkill/Lessons/Lessons 9/data/data.txt')     # открытие файла open()
    # print(file.readline())                                                        # прочитать первую строку
    # print(file.readline())                                                        # прочитать вторую строчку
    # print(file.readlines())                                                       # прочитать все строчки
    print()

    for line in file:                                                               # Пройдет по каждой строчке документа data.txt      
        value_line(line)    

    file.close()                                                                    # Закрыие файла и выход с программы  

if __name__ == '__main__':

    text()


# Что бы не контролировать когда файл открты или когда закрыт можно воспользоваться:
def open_close():
    with open('c:/Python/Уроки TeachMeSkill/Lessons/Lessons 9/data/data.txt') as files:     # контекстный менеджер 
        for line in files:
            print(line)

# Как он работает:
    # files = open('c:/Python/Уроки TeachMeSkill/Lessons/Lessons 9/data/data.txt')
    # try:
    #     for line in files:
    #      print(line)
    # finally:
    #     files.close()
    # print('read file finish')
print()

if __name__ == '__main__':

    open_close()


# Открытие фалов для редактирования 
def write():
    with open('c:/Python/Уроки TeachMeSkill/Lessons/Lessons 9/data/data1.txt', 'w') as files:     # 'w' - корректировка(редактирование) 
        for i in range(10):
            files.writelines(str(i) + '\n')                     # + '\n' - задаем как будет записываться данные (с новой строки в данном случае). Если + '\n' убрать то слитно будет.
    print('write file finish')
    print()
if __name__ == '__main__':

    write() 

# Пример:

def authorized():
    with open('c:/Python/Уроки TeachMeSkill/Lessons/Lessons 9/data/data1.txt') as files:
        login = files.readline().strip()
        password = files.readline().strip()

    user_input_login = input('Enter your login: ')                                          # 0 (т.к. ввели в прошлой функции список 1 - 10)
    user_input_password = input('Enter your password: ')                                    # 1 (т.к. ввели в прошлой функции список 1 - 10) 

    if login == user_input_login and password == user_input_password:
        print('You authorized')
        return
    print('Wrong login or password')

if __name__ == '__main__':
    authorized()

# При скопировании относительного пути 
test1 = open('Уроки TeachMeSkill\Lessons\Lessons 9\data\data1.txt')
print(test1.readlines()) 

# При скопировании пути (полный) 
test1 = open('C:\Python\Уроки TeachMeSkill\Lessons\Lessons 9\data\data1.txt')
print(test1.readlines()) 


# Чтобы можно записать дополнительно в файл (время авторитизации) не удаляя старые нужно:

def read_and_save():
    with open('Уроки TeachMeSkill\Lessons\Lessons 9\data\data1.txt', 'r+') as files:        # 'r+' -позволяет не перезаписывать файл, а только добавить запись дополнительно.
        login = files.readline().strip()
        password = files.readline().strip()
        files.write(datetime.utcnow().isoformat())                                          # время записывается в текущий файл не удаляя предыдущие

    user_input_login = input('Enter your login: ')                                          # 0 (т.к. ввели в прошлой функции список 1 - 10)
    user_input_password = input('Enter your password: ')                                    # 1 (т.к. ввели в прошлой функции список 1 - 10) 

    if login == user_input_login and password == user_input_password:
        print('You authorized')
        return
    print('Wrong login or password')

if __name__ == '__main__':
    read_and_save()