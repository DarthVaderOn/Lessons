#Классы

# Exception()                  # PascalCase классы пишутся с большой буквы
# print()                      # snake_case функции с маленькой

# def main():
#     age = None
#     # raise Exception("Test Error")
#     # raise ZeroDivisionError()                                                 # деление на 0
#     # raise ValueError()
#     # raise TypeError()
#     # raise IndexError()
#     # raise KeyError()
#     try:
#         age = int(input('Enter your age: '))
#     except Exception:                                                           # если мы введем вместо цифр буквы то выдаст ошибку  
#         print('Ой я словил ошибку')
#     else:                                                                       # else пропускает ошибки
#         print("Не было ошибок")                                             
#     finally:                                                                    # всегда выводится с ошибкой или без
#         print('Мы всегда доберемся до этого кода')
                                                       
#     name = (input('Enter your name: '))


#     print(age)

# main()

# Traceback (most recent call last):
#   File "c:\Python\Уроки TeachMeSkill\Lesson 6.py", line 11, in <module>       1 запускается модуль main
#     main()
#   File "c:\Python\Уроки TeachMeSkill\Lesson 6.py", line 7, in main            2 запускается строка raise Exception()
#     raise Exception()
# Exception




def main():
    age = None
   
    try:
        age = int(input('Enter your age: '))
    except Exception as exception:                                                           # если мы введем вместо цифр буквы то выдаст ошибку. Есть сокращения: except Exception as e:
        print(f'Ой я словил ошибку:{exception.__class__}')                                   # Класс ошибки 
    
    print(age) 

main()