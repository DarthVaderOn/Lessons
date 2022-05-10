# SQL: Подзапросы. Функции. JOIN. Транзакции.
# Django: Регистрация.


"""
Подзапросы.

    Подзапросы - запрос внутри другого запроса SQL, который вложен в условие WHERE.
    Например:

        SELECT * FROM Product
        WHERE Price > (SELECT AVG(Price) FROM Product)

    где: AVG - функция возвращает среднее значение среди всех значений столбца.


Функии SQL:

    Функция SUM - возвращает сумму значений столбца таблицы базы данных.

        Например:
                SELECT SUM(*) FROM comments WHERE Price;

    Функция MIN - возвращает минимальное среди всех значений столбца.

        Например:
                SELECT MIN(*) FROM comments WHERE Price;

    Функция MAX - применяется, когда требуется определить максимальное значение среди всех значений столбца.

        Например:
                SELECT MAX(*) FROM comments WHERE Price;

    Функция AVG - возвращает среднее значение среди всех значений столбца.

        Например:
                SELECT AVG(*) FROM comments WHERE Price;

    Функция COUNT - возвращает количество записей таблицы базы данных.

        Например:
            SELECT COUNT(*) FROM comments WHERE text LIKE '%a%';                                                         выведет количество слов с буквой а


JOIN.

        JOIN - оператор языка SQL, который является реализацией операции соединения реляционной алгебры. Входит в предложение FROM операторов SELECT, UPDATE и DELETE.
    Операция соединения, предназначена для обеспечения выборки данных из двух таблиц и включения этих данных в один результирующий набор.

    INNER JOIN

    Внутреннее присоединение. Равносильно просто JOIN или CROSS JOIN (верно для MYSQL, в стандарте SQL INNER JOIN не эквивалентен синтаксически CROSS JOIN, т.к. используется с выражением ON).
    Полное соответствие в двух таблицах.

        Например:

            SELECT * FROM INNER JOIN "user" ON likes.user_id = "user";

    LEFT JOIN

    Оператор левого внешнего соединения LEFT JOIN соединяет две таблицы. Выводит полностью таблицу A, и общие таблицы (данные) A у таблицы Б.

        Например:

            SELECT * FROM likes LEFT JOIN "user" ON likes.user_id = "user"

    RIGHT JOIN

    Оператор правого внешнего соединения RIGHT JOIN соединяет две таблицы. Выводит полностью таблицу Б, и общие таблицы (данные) Б у таблицы A.

        Например:

            SELECT * FROM likes RIGHT JOIN "user" ON likes.user_id = "user"

    FULL OUTER JOIN

    Оператор полного внешнего соединения FULL OUTER JOIN соединяет две таблицы. Выводит полностью таблицу A и Б.

        Например:

            SELECT * FROM likes FULL OUTER JOIN "user" ON likes.user_id = "user"


Транзакции.

        Транзакция является рабочей единицей работы с базой данных (далее – БД). Это последовательность операций, выполняемых в логическом порядке пользователем, либо программой, которая работает с БД.
    Мы можем сказать, что транзакция – это распространение изменений в БД. Например, если мы создаём, изменяем или удаляем запись, то мы выполняем транзакцию. Крайне важно контролировать транзакции для
    гарантирования.
    Для управления транзакциями используются следующие команды:

                                                BEGIN TRANSACTION - Начало транзакции
                                                COMMIT            - Сохраняет изменения
                                                ROLLBACK          - Откатывает (отменяет) изменения
                                                SAVEPOINT         - Создаёт точку к которой группа транзакций может откатиться
                                                SET TRANSACTION   - Размещает имя транзакции.

    Команды управление транзакциями используются только для DML команд: INSERT, UPDATE, DELETE. Они не могут быть использованы во время создания, изменения или удаления таблицы.

        Пример:
        Предположим, что у нас есть таблица developers, которая содержит следующие записи:

                                                +----+-------------------+-----------+------------+--------+
                                                | ID | NAME              | SPECIALTY | EXPERIENCE | SALARY |
                                                +----+-------------------+-----------+------------+--------+
                                                |  1 | Eugene Suleimanov | Java      |          2 |   2500 |
                                                |  2 | Peter Romanenko   | Java      |          3 |   3500 |
                                                |  3 | Andrei Komarov    | C++       |          3 |   2500 |
                                                |  4 | Konstantin Geiko  | C#        |          2 |   2000 |
                                                |  5 | Asya Suleimanova  | UI/UX     |          2 |   1800 |
                                                |  7 | Ivan Ivanov       | C#        |          1 |    900 |
                                                |  8 | Ludmila Geiko     | UI/UX     |          2 |   1800 |
                                                +----+-------------------+-----------+------------+--------+

        Удалим всех С++ разработчиков с помощью следующей команды:

            DELETE FROM developers WHERE SPECIALTY = 'C++';
            COMMIT;

        В результате выполнения данного запроса наша таблица будет содержать следующие записи:

                                                +----+-------------------+-----------+------------+--------+
                                                | ID | NAME              | SPECIALTY | EXPERIENCE | SALARY |
                                                +----+-------------------+-----------+------------+--------+
                                                |  1 | Eugene Suleimanov | Java      |          2 |   2500 |
                                                |  2 | Peter Romanenko   | Java      |          3 |   3500 |
                                                |  4 | Konstantin Geiko  | C#        |          2 |   2000 |
                                                |  5 | Asya Suleimanova  | UI/UX     |          2 |   1800 |
                                                |  7 | Ivan Ivanov       | C#        |          1 |    900 |
                                                |  8 | Ludmila Geiko     | UI/UX     |          2 |   1800 |
                                                +----+-------------------+-----------+------------+--------+

        Добавление записи осуществляется команды:

            BEGIN TRANSACTION;
            INSERT INTO developers (SPECIALTY) VALUES ('Andrei Komarov');
            COMMIT;

        В результате выполнения данного запроса наша таблица будет содержать следующие записи:

                                                +----+-------------------+-----------+------------+--------+
                                                | ID | NAME              | SPECIALTY | EXPERIENCE | SALARY |
                                                +----+-------------------+-----------+------------+--------+
                                                |  1 | Eugene Suleimanov | Java      |          2 |   2500 |
                                                |  2 | Peter Romanenko   | Java      |          3 |   3500 |
                                                |  4 | Konstantin Geiko  | C#        |          2 |   2000 |
                                                |  5 | Asya Suleimanova  | UI/UX     |          2 |   1800 |
                                                |  7 | Ivan Ivanov       | C#        |          1 |    900 |
                                                |  8 | Ludmila Geiko     | UI/UX     |          2 |   1800 |
                                                |  9 | Andrei Komarov    |           |            |        |
                                                +----+-------------------+-----------+------------+--------+

        Транзакция либо выполняется вся, либо ничего не выполняется. Но для таблиц меняется id (автоинкремент) в любом случае т.к. работа с таблицей происходит, даже в случае ошибки.
        Например:
                                                +----+-------------------+-----------+------------+--------+
                                                |  1 | Eugene Suleimanov | Java      |          2 |   2500 |
                                                |  2 | Peter Romanenko   | Java      |          3 |   3500 |
                                                |  3 | Andrei Komarov    | C++       |          3 |   2500 |
                                                |  4 | Konstantin Geiko  | C#        |          2 |   2000 |
                                                |  5 | Asya Suleimanova  | UI/UX     |          2 |   1800 |
                                                |  7 | Ivan Ivanov       | C#        |          1 |    900 |
                                                |  8 | Ludmila Geiko     | UI/UX     |          2 |   1800 |
                                                +----+-------------------+-----------+------------+--------+

        Допустим мы пытаемся добавить транзакцию (одну строку). У нас произошла ошибка (отмена транзакции), после исправления ошибки и добавления строки у нас id будет не 9 а 10.

                                                +----+-------------------+-----------+------------+--------+
                                                | ID | NAME              | SPECIALTY | EXPERIENCE | SALARY |
                                                +----+-------------------+-----------+------------+--------+
                                                |  1 | Eugene Suleimanov | Java      |          2 |   2500 |
                                                |  2 | Peter Romanenko   | Java      |          3 |   3500 |
                                                |  3 | Andrei Komarov    | C++       |          3 |   2500 |
                                                |  4 | Konstantin Geiko  | C#        |          2 |   2000 |
                                                |  5 | Asya Suleimanova  | UI/UX     |          2 |   1800 |
                                                |  7 | Ivan Ivanov       | C#        |          1 |    900 |
                                                |  8 | Ludmila Geiko     | UI/UX     |          2 |   1800 |
                                                |  10| Alex Vinokurov    | Python    |          2 |   1800 |
                                                +----+-------------------+-----------+------------+--------+


Django: Регистрация.

    Создаем модуль в папке publication_app с двумя файлами:

        __init__.py
        registration.py.

        В  registration.py пишем:

            from django.contrib.auth.models import User
            from django.forms import ModelForm

            class RegistrationForm(ModelForm):
                class Meta:
                    model = User
                    fields = ('username', 'email', 'password')                                         # вводим что нужно запрашивать у пользователя при регистрации

    Создаем файл в папке templates:

        registration_page.html

        В registration_page.html пишем:

            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <title>Регистрация</title>
            </head>
            <body>
                <form method="post" action="/registration">
                      {% csrf_token %}
                      {{ reg_form }}
                      <input type="submit" value="Зарегистрироваться">
                </form>
            </body>
            </html>

    В файле views.py:

        from django.shortcuts import render, redirect
        from .models import Post
        from .forms.registration import RegistrationForm                                                # импортируем модуль

        # Create your views here.
        def main_page(request):
            posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
            contex = {'title': 'Hello World', 'posts': posts }
            return render(request, 'main_page.html', contex)


        def registration_page(request):                                                                 # добавили функцию регистрации
            if request.method == "POST":
                form = RegistrationForm(request.POST)
                if form.is_valid():                                                                     # проверка ввода данных на валидность
                    form.save()
                    return redirect('/')


            context = {
                'reg_form': RegistrationForm(),
            }
            return render(request, 'registration_page.html', context)

    Создаем файл urls.py в publication_app

        В файле urls.py пишем:

            from django.conf import settings
            from django.conf.urls.static import static
            from django.contrib import admin
            from django.contrib.staticfiles.urls import staticfiles_urlpatterns

            from django.urls import path
            from publication_app.views import registration_page, main_page

            urlpatterns = [
                path('', main_page, name='main_page'),
                path('registration', registration_page, name='reg_page'),                                   # добавили url
            ]


            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            urlpatterns += staticfiles_urlpatterns()

    Хэширование пароля

        В фале registration.py пишем:

            from django.contrib.auth.models import User
            from django import forms


            class RegistrationForm(forms.ModelForm):
                class Meta:
                    model = User
                    fields = ('username', 'email', 'password',)

                def save(self, commit=True):                                                               # добавили функцию save
                    user = super(RegistrationForm, self).save(commit=False)
                    user.set_password(self.cleaned_data['password'])

                    if commit:
                        user.save()

                    return user
"""