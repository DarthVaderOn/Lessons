# Создание Menu
# Отображение Menu
# Отображение Menu пользователя в зависимости авторизован или не авторизован User.
# Оптимизация базы данных (уникальные данные(индексы))

"""
Создание Menu

    Создаем новую app:

        python manage.py startapp menu_app

    В models.py пишем код:

        from django.db import models

        # Create your models here.


        class Menu(models.Model):
            menu_label = models.CharField(max_length=256, null=False, blank=False, unique=True)

            def __str__(self):
                return f'{self.id}: {self.menu_label}'

        class MenuItem(models.Model):
            menu = models.ForeignKey(Menu, null=False, blank=False, on_delete=models.PROTECT, related_name='links')
            title = models.CharField(max_length=32, null=False, blank=False)
            url = models.CharField(max_length=256, null=False, blank=False)
            icon = models.ImageField(null=True, blank=True)
            priority = models.SmallIntegerField(validators=[MinValueValidator(-100), MaxValueValidator(100)], default=0)

            def __str__(self):
                return f'{self.id}: {self.title}'

    В admin.py пишем код:

        from django.contrib import admin
        from menu_app.models import Menu, MenuItem


        # Register your models here.


        @admin.register(Menu)
        class MenuAdmin(admin.ModelAdmin):
            model = Menu


        @admin.register(MenuItem)
        class MenuItemAdmin(admin.ModelAdmin):
            model = MenuItem

    Применяем миграцию:

        python manage.py makemigrations
        python manage.py migrate


    Теперь в админке можем создать Menu во вкладке MenuItem:


            Menu:             main_menu
            Title:            Главная
            Url:              /
            Icon:             Файл не выбран
            Priority:         0


Отображение Menu

    Создаем в menu_app две папки:

        templates
        templatetags

    В папке templates создаем файл menu.html и пишем код:

        {% for item in menu %}
        <a href="{{ item.url }}">{{ item.title }}</a>
        {% endfor %}

    В папке templatetags создаем файл menu_tags.py пишем код:

        from django import template
        from menu_app.models import Menu

        register = template.Library()

        @register.inclusion_tag('menu.html')
        def main_menu():
            menu = Menu.objects.get(menu_label='main_menu')
            return {'menu': menu.links.order_by('priority').all()}

    Теперь в publication_app в папке templates редактируем файл main_page.html:

        {% load menu_tags %}                                                                                                     #изменения
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            {% if user.is_authenticated %}
            <div id="main_menu">{% main_menu %}</div>                                                                            #изменения
            <div>С возвращением {{user.username}}, {{user.first_name}} {{user.last_name}}!</div>{% endif %}
            {% for post in posts %}
            <h3>{{ post.title}}</h3>
            {% if post.image %}<div><img src="{{ post.image.url }}" alt="" width="350px" height="350px"></div>{% endif %}
            <div>{{ post.text}}</div>
            {% endfor %}
        </body>
        </html>


Отображение Menu пользователя в зависимости авторизован или не авторизован User.

    В файле menu_tags.py дополняем код:

        from django import template
        from menu_app.models import Menu

        register = template.Library()

        @register.inclusion_tag('menu.html')
        def main_menu():
            menu = Menu.objects.get(menu_label='main_menu')
            return {'menu': menu.links.order_by('priority').all()}

        @register.inclusion_tag('menu.html', takes_context=True)                                                                   #изменения
        def user_menu(context):
            if context.request.user.is_authenticated:
                menu = [
                    {
                        'title': context.request.user.username,
                        'url': '/profile',
                    },
                    {
                        'title': 'Выйти',
                        'url': '/logout',
                    },
                ]
            else:
                menu = [
                    {
                        'title': 'Войти',
                        'url': '/authorization',

                    },
                    {
                        'title': 'Регистрация',
                        'url': '/registration'
                    },
                ]
            return {'menu': menu}

    Редактируем файл main_page.html:

        {% load menu_tags %}
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{{ title }}</title>
        </head>
        <body>
            <div id="main_menu">{% main_menu %}</div>
            <div id="user_menu">{% user_menu %}</div>                                                                               #изменения
            <div>С возвращением {{user.username}}, {{user.first_name}} {{user.last_name}}!</div>
            {% for post in posts %}
            <h3>{{ post.title}}</h3>
            {% if post.image %}<div><img src="{{ post.image.url }}" alt="" width="350px" height="350px"></div>{% endif %}
            <div>{{ post.text}}</div>
            {% endfor %}
        </body>
</html>


Оптимизация базы данных (уникальные данные(индексы))

    Открываем файл models.py вносим дополнения:

        from django.core.validators import MinValueValidator, MaxValueValidator
        from django.db import models

        # Create your models here.


        class Menu(models.Model):
            menu_label = models.CharField(max_length=256, null=False, blank=False, unique=True)

            def __str__(self):
                return f'{self.id}: {self.menu_label}'

        class MenuItem(models.Model):
            menu = models.ForeignKey(Menu, null=False, blank=False, on_delete=models.PROTECT, related_name='links')
            title = models.CharField(max_length=32, null=False, blank=False)
            url = models.CharField(max_length=256, null=False, blank=False)
            icon = models.ImageField(null=True, blank=True)
            priority = models.SmallIntegerField(validators=[MinValueValidator(-100), MaxValueValidator(100)], default=0)

            def __str__(self):
                return f'{self.id}: {self.title}'

            class Meta:                                                                                                             # дополняем
                indexes = [
                    models.Index(fields=('menu',)),
                    models.Index(fields=('menu', 'url')),
                ]
                unique_together =[('menu', 'title')]

    Применяем миграцию:

        python manage.py makemigrations
        python manage.py migrate
"""