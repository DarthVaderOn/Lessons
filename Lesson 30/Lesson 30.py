# Авторизация через API через Simple JWT
# Настройки Simple JWT
# Регистрация через API


"""
Авторизация через API


    Устанавливаем djangorestframework-simplejwt не забываем про requirements.txt:

        pip install djangorestframework-simplejwt


    Добавим в settings.py в REST_FRAMEWORK:

        REST_FRAMEWORK = {
            ...
            'DEFAULT_AUTHENTICATION_CLASSES': (
                ...
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            )
            ...
        }



    Добавим в urls.py в urlpatterns:

        from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


        urlpatterns = [
            ...
            path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
            ...
        ]


    Добавим в settings.py в INSTALLED_APPS:

        INSTALLED_APPS = [
            ...
            'rest_framework_simplejwt',
            ...
        ]


Настройки Simple JWT


    Добавим в settings.py следующий код:

        from datetime import timedelta
        ...

        SIMPLE_JWT = {
            'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
            'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
            'ROTATE_REFRESH_TOKENS': False,
            'BLACKLIST_AFTER_ROTATION': False,
            'UPDATE_LAST_LOGIN': False,

            'ALGORITHM': 'HS256',
            'SIGNING_KEY': SECRET_KEY,
            'VERIFYING_KEY': None,
            'AUDIENCE': None,
            'ISSUER': None,
            'JWK_URL': None,
            'LEEWAY': 0,

            'AUTH_HEADER_TYPES': ('Bearer',),
            'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
            'USER_ID_FIELD': 'id',
            'USER_ID_CLAIM': 'user_id',
            'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

            'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
            'TOKEN_TYPE_CLAIM': 'token_type',
            'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

            'JTI_CLAIM': 'jti',

            'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
            'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
            'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
        }

    ACCESS_TOKEN_LIFETIME
        Объект datetime.timedelta, который указывает, как долго токены доступа действительны. Это timedeltaзначение добавляется к текущему времени UTC во время создания маркера, чтобы получить значение утверждения маркера по
        умолчанию «exp».

    REFRESH_TOKEN_LIFETIME
        Объект datetime.timedelta, указывающий, как долго токены обновления действительны. Это timedeltaзначение добавляется к текущему времени UTC во время создания маркера, чтобы получить значение утверждения маркера по
        умолчанию «exp».

    ROTATE_REFRESH_TOKENS
        При значении True, если токен обновления отправляется в TokenRefreshView, новый токен обновления будет возвращен вместе с новым токеном доступа. Этот новый токен обновления будет предоставлен через ключ «обновить» в
        ответе JSON. Новые токены обновления будут иметь обновленное время истечения срока действия, которое определяется добавлением дельты времени в REFRESH_TOKEN_LIFETIME параметре к текущему времени на момент выполнения запроса.
        Если приложение черного списка используется и для BLACKLIST_AFTER_ROTATIONпараметра установлено значение True, токены обновления, отправленные в представление обновления, будут добавлены в черный список.

    BLACKLIST_AFTER_ROTATION
        Если установлено значение True, маркеры обновления, отправленные в TokenRefreshView, добавляются в черный список, если приложение черного списка используется и для ROTATE_REFRESH_TOKENSпараметра установлено значение True.
        Вам нужно добавить 'rest_framework_simplejwt.token_blacklist',в свой INSTALLED_APPSфайл настроек, чтобы использовать этот параметр.

    UPDATE_LAST_LOGIN
        Если установлено значение True, поле last_login в таблице auth_user обновляется при входе в систему (TokenObtainPairView).
        Предупреждение: обновление last_login резко увеличит количество транзакций базы данных. Люди, злоупотребляющие представлениями, могут замедлить работу сервера, и это может быть уязвимостью системы безопасности. Если вы действительно этого хотите, по крайней мере, задушите конечную точку с помощью DRF.

    ALGORITHM
        Алгоритм из библиотеки PyJWT, который будет использоваться для выполнения операций подписи/проверки токенов. Для использования симметричной подписи и проверки HMAC могут использоваться следующие алгоритмы: 'HS256', 'HS384',
        'HS512'. Если выбран алгоритм HMAC, этот SIGNING_KEYпараметр будет использоваться как в качестве ключа подписи, так и в качестве ключа проверки. В этом случае VERIFYING_KEYнастройка будет проигнорирована. Для использования
        асимметричной подписи и проверки RSA могут использоваться следующие алгоритмы: 'RS256', 'RS384', 'RS512'. Если выбран алгоритм RSA, для SIGNING_KEYпараметра должна быть задана строка, содержащая закрытый ключ RSA.
        Аналогичным образом для VERIFYING_KEYпараметра должна быть задана строка, содержащая открытый ключ RSA.

    SIGNING_KEY
        Ключ подписи, который используется для подписи содержимого сгенерированных токенов. Для подписи HMAC это должна быть случайная строка, по крайней мере, с таким количеством битов данных, которое требуется протоколом подписи.
        Для подписи RSA это должна быть строка, содержащая закрытый ключ RSA длиной 2048 бит или более. Так как Simple JWT по умолчанию использует 256-битную подпись HMAC, SIGNING_KEYзначение параметра по умолчанию равно значению
        SECRET_KEY параметра для вашего проекта django. Хотя это наиболее разумное значение по умолчанию, которое может предоставить Simple JWT, разработчикам рекомендуется изменить этот параметр на значение, не зависящее от
        секретного ключа проекта django. Это упростит изменение ключа подписи, используемого для токенов, в случае его взлома.

    VERIFYING_KEY
        Ключ проверки, который используется для проверки содержимого сгенерированных токенов. Если в настройке указан алгоритм HMAC ALGORITHM, VERIFYING_KEYнастройка будет проигнорирована и SIGNING_KEY будет использоваться значение
        настройки. Если в параметре указан алгоритм RSA ALGORITHM, для VERIFYING_KEYпараметра должна быть задана строка, содержащая открытый ключ RSA.

    AUDIENCE
        Аудитория утверждает, что включена в сгенерированные токены и/или проверена в декодированных токенах. Если установлено значение None, это поле исключается из токенов и не проверяется.

    ISSUER
        Эмитент утверждает, что он включен в сгенерированные токены и/или проверен в декодированных токенах. Если установлено значение None, это поле исключается из токенов и не проверяется.

    JWK_URL
        JWK_URL используется для динамического разрешения открытых ключей, необходимых для проверки подписи токенов. Например, при использовании Auth0 вы можете установить значение « https://yourdomain.auth0.com/.well-known/jwks.json ».
        Если установлено значение None, это поле исключается из серверной части токена и не используется во время проверки.

    LEEWAY
        Лиуэй используется, чтобы дать некоторый запас по времени экспирации. Это может быть целое число секунд или datetime.timedelta. Пожалуйста, обратитесь к https://pyjwt.readthedocs.io/en/latest/usage.html#expiration-time-claim-exp
        для получения дополнительной информации.

    AUTH_HEADER_TYPES
        Типы заголовков авторизации, которые будут приниматься для представлений, требующих аутентификации. Например, значение 'Bearer'означает, что представления, требующие аутентификации, будут искать заголовок в следующем формате: .
        Этот параметр также может содержать список или кортеж возможных типов заголовков (например, ). Если таким образом используется список или кортеж, а аутентификация не удалась, первый элемент в коллекции будет использоваться
        для создания заголовка «WWW-Authenticate» в ответе.Authorization: Bearer <token>('Bearer', 'JWT')

    AUTH_HEADER_NAME
        Имя заголовка авторизации, которое будет использоваться для аутентификации. По умолчанию HTTP_AUTHORIZATIONпринимается Authorizationзаголовок в запросе. Например, если вы хотите использовать X_Access_Tokenв заголовке ваших
        запросов, пожалуйста, укажите AUTH_HEADER_NAMEв HTTP_X_ACCESS_TOKENнастройках.

    USER_ID_FIELD
        Поле базы данных из пользовательской модели, которое будет включено в сгенерированные токены для идентификации пользователей. Рекомендуется, чтобы значение этого параметра задавало поле, которое обычно не изменяется после
        выбора его начального значения. Например, указание поля «имя пользователя» или «электронная почта» было бы плохим выбором, поскольку имя пользователя или адрес электронной почты учетной записи могут меняться в зависимости
        от того, как разработано управление учетной записью в данной службе. Это может позволить создать новую учетную запись со старым именем пользователя, в то время как существующий токен все еще действителен, который использует
        это имя пользователя в качестве идентификатора пользователя.

    USER_ID_CLAIM
        Утверждение в сгенерированных токенах, которые будут использоваться для хранения идентификаторов пользователей. Например, значение параметра 'user_id'будет означать, что сгенерированные токены включают утверждение «user_id»,
        которое содержит идентификатор пользователя.

    USER_AUTHENTICATION_RULE
        Вызывается, чтобы определить, разрешено ли пользователю аутентифицироваться. Это правило применяется после обработки действительного токена. Пользовательский объект передается вызываемому объекту в качестве аргумента. Правило
        по умолчанию — проверять, что is_active флаг по-прежнему True. Вызываемый объект должен возвращать логическое значение, Trueесли оно авторизовано, Falseв противном случае это приводит к коду состояния 401.

    AUTH_TOKEN_CLASSES
        Список точечных путей к классам, указывающим типы маркеров, разрешенных для проверки подлинности. Подробнее об этом в разделе «Типы токенов» ниже.

    TOKEN_TYPE_CLAIM
        Имя утверждения, которое используется для хранения типа токена. Подробнее об этом в разделе «Типы токенов» ниже.

    JTI_CLAIM
        Имя утверждения, которое используется для хранения уникального идентификатора токена. Этот идентификатор используется для идентификации отозванных токенов в приложении черного списка. В некоторых случаях может быть необходимо
        использовать другое утверждение, кроме утверждения «jti» по умолчанию, для хранения такого значения.

    TOKEN_USER_CLASS
        Пользовательский объект без сохранения состояния, поддерживаемый проверенным токеном. Используется только для серверной части аутентификации JWTStatelessUserAuthentication. Значение представляет собой пунктирный путь к вашему
        подклассу rest_framework_simplejwt.models.TokenUser, который также является значением по умолчанию.

    SLIDING_TOKEN_LIFETIME
        Объект datetime.timedelta, указывающий, как долго скользящие токены действительны для подтверждения аутентификации. Это timedeltaзначение добавляется к текущему времени UTC во время создания маркера, чтобы получить значение
        утверждения маркера по умолчанию «exp». Подробнее об этом в разделе «Скользящие токены» ниже.

    SLIDING_TOKEN_REFRESH_LIFETIME
        Объект datetime.timedelta, указывающий, как долго скользящие токены действительны для обновления. Это timedeltaзначение добавляется к текущему времени UTC во время создания маркера, чтобы получить значение утверждения маркера
        по умолчанию «exp». Подробнее об этом в разделе «Скользящие токены» ниже.

    SLIDING_TOKEN_REFRESH_EXP_CLAIM
        Имя утверждения, которое используется для хранения времени истечения периода обновления скользящего маркера.


Регистрация через API (Обязательно делать когда нет Users и все User наследуется только от модели которую мы создадим ниже)


    Создаём новый APP:

        python manage.py startapp user_app


    Добавляем модель:

        from django.db import models
        from django.contrib.auth.models import AbstractUser


        # Create your models here.


        class User(AbstractUser):                                                       # AbstractBaseUser - это родительский класс, а AbstractUser - это дочерний класс и он наследуется от AbstractBaseUser
            email = models.EmailField(unique=True)


    В settings.py добавляем :

        INSTALLED_APPS = [
            ...
            'user_app',
            ...
        ]


        И добавляем строчку:

        AUTH_USER_MODEL = 'user_app.User'


    Создаем папку api

    Внутри создаём папки serializers и views

    Создаём в данных папках фалы user.py

    В serializers/user.py пишем код:

        from rest_framework import serializers
        from ...models import User


        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
                read_only_fields = ('id',)

            username = serializers.CharField(min_length=3, required=True)
            password = serializers.CharField(min_length=8, required=True, write_only=True)          # write_only - скрывает введенные данные при регистрации в API
            email = serializers.EmailField(required=True, write_only=True)


             def validate_password(self, value: str) -> str:                                        # Хэш-значение, переданное пользователем

                 return make_password(value)


    В views/user.py пишем код:

        from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
        from rest_framework.viewsets import GenericViewSet
        from user_app.api.serializers.users import UserSerializer
        from ...models import User


        class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
            serializer_class = UserSerializer
            queryset = User.objects.all()


    В views/router.py пишем код:

        from rest_framework import routers
        from .users import UserViewSet


        api_router = routers.DefaultRouter()
        api_router.register('users', UserViewSet)

    В user_app создаем файл urls.py и пишем код:

        from django.conf import settings
        from django.conf.urls.static import static
        from django.contrib.staticfiles.urls import staticfiles_urlpatterns
        from django.urls import path, include
        from user_app.api.views.router import api_router


        urlpatterns = [
            path('api/', include(api_router.urls)),
        ]


        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += staticfiles_urlpatterns()


    В глобальных urls.py добавим строчку:

        path('', include('user_app.urls')),


    Создаём файл registration.py в serializers и views:

        В serializers/registration.py пишем код:

            from rest_framework import serializers
            from ...models import User


            class RegistrationSerializer(serializers.ModelSerializer):
                class Meta:
                    model = User
                    fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
                    read_only_fields = ('id',)


                username = serializers.CharField(min_length=3, required=True)                           # выставляем минимальную длинну ника
                password = serializers.CharField(min_length=8, required=True, write_only=True)          # выставляем минимальную длинну пароля


        В views/registration.py пишем код:

            from rest_framework.mixins import CreateModelMixin
            from rest_framework.viewsets import GenericViewSet
            from rest_framework.permissions import AllowAny
            from ..serializers.users import UserSerializer
            from user_app.models import User


            class RegistrationViewSet(GenericViewSet, CreateModelMixin):
                serializer_class = UserSerializer
                queryset = User.objects.all()
                permission_classes = [AllowAny]


        Редактируем router.py:

            from rest_framework import routers
            from .registration import RegistrationViewSet                                               # добавили строчку
            from .users import UserViewSet


            api_router = routers.DefaultRouter()
            api_router.register('users', UserViewSet)
            api_router.register('registration', RegistrationViewSet)            # добавили строчку
"""