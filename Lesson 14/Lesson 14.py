# Приложение на Flask, базы данных


# Импортируем Web framework Flask
from flask import Flask

# Импортируем экранирование специальных символов в шаблоне
from markupsafe import escape


# Экземпляр приложения с переменной Flask
app = Flask(__name__)


# Декоратор главной страницы URL с обработчиком событий (функция представления)
@app.route('/')                                                                                      # В Flask декоратор route используется, чтобы связать URL адрес с функций.
# @app.route('/index') - вверися 2 начальной страницы                                                  / -  начальная страница (главная) http://127.0.0.1:5000/
def hello_world():
    """При нахождении на главной странице будет выводиться указанная строка"""
    return 'Hello World!'


# Декоратор с дополнительным URL с обработчиком событий (функция представления)
@app.route('/user/<name>')                                                                           # <name> - переменная которую можно редактировать (шрифт, размер, тип и т.д.)
def user(name):
    """При указании имени после /user будет выведено приветственное сообщение"""
    return  f'Hello {escape(name)}!'                                                                 # escape - предназначена выполняет экранирование специальных символов в шаблоне.
    # return '<h>Hi %s!<h>' % name (устаревшая версия)

# Декоратор с дополнительным URL с обработчиком событий (функция представления)
@app.route('/now/year')
def now_year():
    """При нахождении по данной ссылке будет выводиться указанная строка"""
    return '2022!'


# Запуск сервера (для быстрого выбора напишем main + Tab), с режимом отладки debug=True
if __name__ == '__main__':
    app.run(debug=True)


""" 
Типы преобразования переменных(<name>):

    string     (по умолчанию) принимает любой текст без косой черты
    
    int        принимает положительные целые числа
    
    float      принимает положительные значения с плавающей запятой
    
    path       нравится, string но также принимает косую черту
    
    uuid       принимает строки UUID



# requirements.txt (информация о версиях модулей, программ, пакетов и т.д.)

    requirements.txt — это список внешних зависимостей. Сообщество Python исповедует идеологию "простое лучше, чем сложное". 
Наверное, поэтому для хранения списка зависимостей сообщество выбрало самый простой из возможных форматов — текстовый файл,
где на каждой строке перечислено ровно по одной зависимости.

    Стоит отметить, что requirements.txt не является стандартом, т.е. нет документа, который описывал бы требования к этому файлу.
Скорее, это просто распространённая практика в сообществе, которая, наверное, возникла спонтанно и хорошо прижилась.
Не обязательно называть файл именно requirements.txt, можно назвать его как угодно, лишь бы его назначение оставалось понятно.

Как пользоваться:
Команда pip install умеет читать такие файлы, если передать специальный флаг:

    $ pip install -r requirements.txt

Как создать:
Есть два подхода:

    создавать этот файл вручную;
    генерировать автоматически.
    
Команда pip freeze выводит все установленные в интерпретатор сторонние пакеты. Заметьте, что в список попали не только прямые зависимости
(pyowm), но и подзависимости — это даже лучше, потому что вы сможете более точно воссоздать окружение по этому файлу.
Можно перенаправить вывод этой команды в файл при помощи стандартного консольного приема (работает и на Windows), и получить валидный файл
requirements.txt:

    $ pip freeze > requirements.txt    

    Пример: 
        pytest==7.1.1
        flask==2.1.1
        flask_sqlalchemy==2.5.1
"""