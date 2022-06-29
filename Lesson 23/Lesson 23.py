# Celery
# Celery в проекте (установка)
# Запуск Celery
# Redis


"""
Celery


    Celery нужен для запуска задач в отдельном рабочем процессе (worker), что позволяет немедленно отправить HTTP-ответ пользователю в веб-процессе (даже если задача в рабочем процессе все еще выполняется).
    Цикл обработки запроса не будет заблокирован, что повысит качество взаимодействия с пользователем.
    Ниже приведены некоторые примеры использования Celery:
        - Вы создали приложение с функцией отправки комментариев, в которых пользователь может использовать символ @, чтобы упомянуть другого пользователя, после чего последний получит уведомление по электронной почте.
          Если пользователь упоминает 10 человек в своем комментарии, веб-процессу необходимо обработать и отправить 10 электронных писем. Иногда это занимает много времени (сеть, сервер и другие факторы). В данном случае
          Celery может организовать отправку писем в фоновом режиме, что в свою очередь позволит вернуть HTTP-ответ пользователю без ожидания.
        - Нужно создать миниатюру загруженного пользователем изображения? Такую задачу стоит выполнить в рабочем процессе.
        - Вам необходимо делать что-то периодически, например, генерировать ежедневный отчет, очищать данные истекшей сессии. Используйте Celery для отправки задач рабочему процессу в назначенное время.


Celery в проекте (установка)

    Как делать не нужно!:

        Создаем файл tasks.py внутри app и пишем код:


            from time import sleep


            def very_long_task():
                sleep(10)


        В views в posts вызываем данный метод:


            from django.shortcuts import redirect, render
            from django.views import View
            from profile_app.forms.registration import RegistrationForm


            class RegistrationView(View):
                def get(self, request):
                    reg_form = RegistrationForm()
                    contex = {
                        'title': 'Registration',
                        'reg_form': reg_form,
                    }
                    return render(request, 'registration_page.html', contex)


                def post(self, request):
                    very_long_task()                                                    # добавили
                    reg_form = RegistrationForm(request.POST)
                    if reg_form.is_valid():
                        reg_form.save()
                        return redirect('/authorization')
                    contex = {
                        'title': 'Registration',
                        'reg_form': reg_form,
                    }
                    return render(request, 'registration_page.html', contex)


    Как делать нужно через Celery:


        Установка Celery:


            Открываем requirements.txt :

                celery==5.2.7
                django-celery-results==2.2.0
                django-redis==5.2.0
                redis


            Вводим команду:


                pip install -r requirements.txt


        В корне проекта создаем файл celery.py и пишем код:


            import os

            from celery import Celery

            # Set the default Django settings module for the 'celery' program.
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

            app = Celery('Django')

            # Using a string here means the worker doesn't have to serialize
            # the configuration object to child processes.
            # - namespace='CELERY' means all celery-related configuration keys
            #   should have a `CELERY_` prefix.
            app.config_from_object('django.conf:settings', namespace='CELERY')

            # Load task modules from all registered Django apps.
            app.autodiscover_tasks()


        В корне проекта в файле __init__ пишем код:


            # This will make sure the app is always imported when
            # Django starts so that shared_task will use this app.
            from .celery import app as celery_app

            __all__ = ('celery_app',)


        Вводим команду:

            python manage.py migrate django_celery_results


        В settings.py дополняем код:

            CELERY_BROKER_URL = 'redis://localhost:6379'
            CELERY_RESULT_BACKEND = 'django-db'
            CELERY_CACHE_BACKEND = 'django-cache'


Запуск Celery:


        Создаем файл tasks.py внутри app и пишем код:


            import  requests
            from celery import shared_task


            @shared_task
            def very_long_task(user_id):
                r = requests.get('http://httpbin.org/delay/10')
                return r.status.code


                В views в posts вызываем данный метод:


            from django.shortcuts import redirect, render
            from django.views import View
            from profile_app.forms.registration import RegistrationForm


            class RegistrationView(View):
                def get(self, request):
                    reg_form = RegistrationForm()
                    contex = {
                        'title': 'Registration',
                        'reg_form': reg_form,
                    }
                    return render(request, 'registration_page.html', contex)


                def post(self, request):
                    very_long_task.delay(request.user.id)                                   # добавили
                    reg_form = RegistrationForm(request.POST)
                    if reg_form.is_valid():
                        reg_form.save()
                        return redirect('/authorization')
                    contex = {
                        'title': 'Registration',
                        'reg_form': reg_form,
                    }
                    return render(request, 'registration_page.html', contex)


        Запускаем Celery:

            celery -A Django worker -l INFO


Redis


    Что такое Redis и зачем его использовать?

            Redis (REmote DIctionary Server) - это хранилище структуры данных в памяти, которое можно использовать в качестве базы данных, кэша или брокера сообщений. Данные хранятся в Redis в форме ключ/значение,
        где ключи используются для поиска и извлечения данных, хранящихся в экземпляре Redis. Обычные базы данных хранят данные на диске, что влечет за собой дополнительные затраты с точки зрения времени и аппаратных ресурсов.
        Redis избегает этого, сохраняя все данные в памяти, что делает данные легкодоступными и увеличивает скорость доступа к данным и манипулирования ими по сравнению с обычными базами данных. Это причина, почему Redis известен
        своей исключительной высокой производительностью. Redis позволяет нам хранить данные в нескольких высокоуровневых структурах данных, включая строки, хэши, списки, наборы и отсортированные наборы.
        Это дает нам больше гибкости в отношении типа и объема информации, которую мы можем хранить в хранилище данных Redis. Написанный на ANSI C, Redis легок и не имеет внешних зависимостей. Он также довольно дружественен для
        разработчиков, поскольку поддерживает большинство языков высокого уровня, таких как Python, JavaScript, Java, C/C ++ и PHP.

    Когда следует использовать Redis?

         Типичные случаи использования Redis:

         - Кэширование. Учитывая его скорость по сравнению с традиционными базами данных, с точки зрения операций чтения и записи, Redis стал идеальным решением для временного хранения данных в кэш-памяти для ускорения доступа
           к данным в будущем.
         - Очередь сообщений. Благодаря возможности реализации парадигмы обмена сообщениями «публикация / подписка» Redis стал посредником в системах очередей сообщений.
         - Хранение данных: Redis может использоваться для хранения данных значения ключа в качестве базы данных NoSQL.

        Такие компании, как Twitter, Pinterest, Github, Snapchat и StackOverflow, используют Redis для хранения и обеспечения высокой доступности данных для своих пользователей.
        Например, Twitter хранит самые последние входящие твиты для пользователя в Redis, чтобы ускорить доставку твитов в клиентские приложения.
        Pinterest использует Redis для хранения списка пользователей и форумов, за которым следит пользователь, списка подписчиков пользователя, а также списка людей, которые следят за вашими досками, среди других списков,
        чтобы улучшить взаимодействие с платформой.
"""