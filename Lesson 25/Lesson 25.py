# Отладка
# Отладка Django — добавление Django Debug Toolbar в проект



"""
Отладка

    Что такое отладка ?

    Независимо от профессионализма, каждый разработчик имеет дело с ошибками — это является частью работы. Отладка ошибок — непростая задача; изначально много времени занимает процесс обнаружения ошибки и ее устранения.
    Следовательно, каждый разработчик должен знать как устранять ошибки. В Django, процесс отладки можно сильно упростить. Вам только необходимо установить и подключить Django Debug Toolbar в приложение.


Отладка Django — добавление Django Debug Toolbar в проект


    Для установки django-debug-toolbar, используем команду pip install. Запустите следующий код в терминале/оболочке ОС:


        pip install django-debug-toolbar


    В settings.py добавьте следующую строку в раздел INSTALLED_APPS:


        INSTALLED_APPS = [
        ...
        'debug_toolbar',
        ]


    Также убедитесь, что в файле settings.py присутствует следующая строка STATIC_URL = '/static/'. Обычно она находится в конце модуля и не требует добавления.Если ее нет, просто добавьте в конец файла.
    Убедитесь, что DEBUG имеет значение TRUE в settings.py, чтобы все работало.


    Чтобы использовать Debug Toolbar, мы должны импортировать его пути. Следовательно, в urls.py добавьте код:


        from django.conf import settings
        from django.urls import path, include

        # urlpatterns = [....

        if settings.DEBUG:
            import debug_toolbar
            urlpatterns = [
                path('__debug__/', include('debug_toolbar.urls')),
            ] + urlpatterns


    Добавьте middleware панели инструментов debug_toolbar.middleware.DebugToolbarMiddleware, в список MIDDLEWARE в settings.py:


        ...
        MIDDLEWARE = [
            ...
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]
        ...


    Django Debug Toolbar отображается только в том случае, если в списке INTERNAL_IPS есть IP приложения. Для разработки на локальном компьютере добавьте в список IP 127.0.0.1.

        /settings.py
        ...
        INTERNAL_IPS = [
            '127.0.0.1',
        ]

    Если списка INTERNAL_IPS еще нет, добавьте его в конец settings.py.


    Теперь в браузере переходим на http://127.0.0.1:8000/


"""