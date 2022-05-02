# Введение в Django
# Паттерны проектирования, MTV
# Django
# Панель администратора
# Django apps
# Manage команды
# Переменные окружения и настройки


"""
Установка Django:

    Создаем новый проект:
        Open (PyCharm)
        Выбираем/создаем новую папку для проекта

    Настраиваем интерпретатор:
        Внизу нажимаем на Python (в PyCharm)
        Add Interpreter
        Virtualenv Environment (виртуальное окружение)
        Python 3.10

    Инициализировать репозиторий:
        git init

    Рядом с папкой (не в папке venv) создаем файлы:
        .gitignore
        requirements.txt (пишем django==4.0.4 и другие зависимости pip install -r requirements.txt)

    Обновляем pip:
        pip install --upgrade pip


Создание/запуск проекта Django (полная документация https://www.djangoproject.com) :

    Создаем встроенные инструментарий:
        django admin startproject название нашего проекта .(точка обязательно обозначает что нужно создать в текущей директории)

    Запуск проекта:
            python manage.py runserver
            Что бы зайти нажимаем на ссылку в строке: Starting development server at http://127.0.0.1:8000/
            Если проект запущен правильно то при переходе на ссылку выведет: The install worked successfully! Congratulations!
            Чтобы зайти как админ http://127.0.0.1:8000/admin/. Редактирование админки происходит в файле urls.py (urlpatterns (можем изменить
            стандартного адрес админки admin/)):
                Запрос Username и Password, чтобы создать пользователя: python manage.py migrate (создание таблиц или заполнение таблиц):
                    python manage.py createsuperuser
                    Вводим данные:
                        Username
                        Email address(необязательно)
                        Password
            python manage.py startapp указываем название приложения


Работа с запросами:

    Создаем функцию в файле views.py принимающую один аргумент

    Пример:
        from django.http import HttpResponse

        def main_page(request):
            return HttpResponse('Hello Word')

    Далее в файле urls.py создаем url адрес:

        from publication_app.views import main_page

        path('', main_page, name='main_page'),

    Далее в папке publication_app создаем папку templates и внутри этой папки создаем файл main_page.html и вносим:

        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Hello World</title>
        </head>
        <body>
            <h1>Привет мир!</h1>
        </body>
        </html>

    Далее в файле views.py вносим изменения:

        from django.shortcuts import render

        def main_page(request):
            return render(request, 'main_page.html')

    Далее в файле settings.py дополняем в INSTALLED_APPS 'publication_app':

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'publication_app',

Работа с базами данных (db.sqlite3):

    Запускаем файл db.sqlite3
    Проверить пользователей и их данные можно в файле auth_user


Работа с моделями:

    Открываем файл models.py
    Создаем модель:

        from django.db import models

        class Post(models.Model):
            title = models.CharField(max_length=256, unique=False, blank=False, null=False)
            text = models.TextField(blank=False, null=False)

    где max_length - длинна поста, unique(False) - уникальность(не уникальный), blank(False) - нельзя оставлять пустым,
    null(False) - заполненность обязательная.

    Далее в файле views.py вносим изменения:

        from django.shortcuts import render
        from .models import Post


        def main_page(request):
            posts = Post.objects.all()
            contex = {'title': 'ПРИВЕТ МИР', 'posts': posts }
            return render(request, 'main_page.html', contex)

    Далее в файле main_page.html вносим измененияЖ

        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            {% for post in posts %}
            <h3>{{ post.title}}</h3>
            <div>{{ post.text}}</div>
            {% endfor %}
        </body>
        </html>

    Далее создаем миграцию (редактировать их строго запрещено):
        python manage.py makemigrations

    Далее запускаем миграцию:
        python manage.py migrate

    Теперь в базе данных есть таблица publication_app_post.

    Далее регистрируем модель в админке:
        Открываем файл admin.py

        from django.contrib import admin

        from .models import Post
        admin.site.register(Post)

    Теперь зайдя http://127.0.0.1:8000/admin/ появится вкладка Post где мы можем создавать и редактировать посты.


Редактирование постов через админки:

    Предположим мы хотим создать список постов и их фильтрацию по id, а так же заголовок поста:

        from django.contrib import admin


        from .models import Post

        @admin.register(Post)
        class PostAdmin(admin.ModelAdmin):
            list_display = ('id', 'title') # Вывод списка со столбцами id и Заголовка
            ordering = ('-id',)            # Фильтрация по id (от большего к меньшему, id - от меньшего к большему)


Время редактирования/создания постов:

    В файле models.py

        from django.db import models

        # Create your models here.
        class Post(models.Model):
            created_at = models.DateTimeField(auto_now_add=True)
            title = models.CharField(max_length=256, unique=False, blank=False, null=False)
            text = models.TextField(blank=False, null=False)

    Создаем миграцию:
        python manage.py makemigrations
        Вводим 1
        Enter

    Запускаем миграцию:
        python manage.py migrate

    Редактируем админку admin.py:

        from django.contrib import admin

        # Register your models here.
        from .models import Post

        @admin.register(Post)
        class PostAdmin(admin.ModelAdmin):
            list_display = ('id', 'title', 'created_at')        добавили 'created_at'
            ordering = ('-created_at', '-id',)                  добавили '-created_at' (по убыванию)
            readonly_fields = ('created_at',)                   добавили строку для вывода при создании файла


Сортировка записей на главной странице (не админка):

    В файле views.py

        from django.shortcuts import render
        from .models import Post

        # Create your views here.
        def main_page(request):
            posts = Post.objects.order_by('-created_at', '-id').all()        добавили order_by('-created_at', '-id')
            contex = {'title': 'ПРИВЕТ МИР', 'posts': posts }
            return render(request, 'main_page.html', contex)


Публичные записи и скрытые:

    В файле models.py

        from django.db import models

        # Create your models here.
        class Post(models.Model):
            created_at = models.DateTimeField(auto_now_add=True)
            title = models.CharField(max_length=256, unique=False, blank=False, null=False)
            text = models.TextField(blank=False, null=False)
            is_public = models.BooleanField(default=True)                                        добавили строку

    Создаем миграцию:
        python manage.py makemigrations

    Запускаем миграцию:
        python manage.py migrate

    В файле views.py

        from django.shortcuts import render
        from .models import Post

        # Create your views here.
        def main_page(request):
            posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()    добавили filter(is_public=True)
            contex = {'title': 'ПРИВЕТ МИР', 'posts': posts }
            return render(request, 'main_page.html', contex)


Загрузка картинок(требуется установка библиотеки Pillow):

    Устанавливаем библиотеку Pillow:
        pip install pillow

    В файле models.py

        from django.db import models

        # Create your models here.
        class Post(models.Model):
            created_at = models.DateTimeField(auto_now_add=True)
            title = models.CharField(max_length=256, unique=False, blank=False, null=False)
            text = models.TextField(blank=False, null=False)
            is_public = models.BooleanField(default=True)
            image = models.ImageField(null=True, blank=True)                                                       добавили строку

    Создаем миграцию:
        python manage.py makemigrations
        Вводим 1
        None
        Enter

    Запускаем миграцию:
        python manage.py migrate

    В файле urls.py

        from django.conf import settings
        from django.conf.urls.static import static
        from django.contrib import admin
        from django.contrib.staticfiles.urls import staticfiles_urlpatterns
        from django.urls import path
        from publication_app.views import main_page

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', main_page, name='main_page'),
        ]

        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)        добавили строку
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)          добавили строку
        urlpatterns += staticfiles_urlpatterns()                                              добавили строку

    В файле settings.py

        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/4.0/howto/static-files/

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        STATIC_URL = 'static/'

        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        MEDIA_URL = 'media/'

    Создаем запись через админку и выбираем файл.


Чтобы отобразить картинку на главной странице:

    В файле main_page.html

        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            {% for post in posts %}
            <h3>{{ post.title}}</h3>
            {% if post.image %}<div><img src="{{ post.image.url }}" alt=""></div>{% endif %}      добавили строку
            <div>{{ post.text}}</div>
            {% endfor %}
        </body>
        </html>


Изменение размера картинки:

    В файле main_page.html

        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            {% for post in posts %}
            <h3>{{ post.title}}</h3>
            {% if post.image %}<div><img src="{{ post.image.url }}" alt="" width="350px" height="350px"></div>{% endif %}      дополнили строку
            <div>{{ post.text}}</div>
            {% endfor %}
        </body>
        </html>

    """