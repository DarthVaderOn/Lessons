# View класс
# ListView
# Django Rest Framework (API)
# Создание публикаций через API

"""
View класс.


    1 Вариант написания через функцию registration.py:


        from django.shortcuts import redirect, render
        from django.views import View

        from publication_app.forms.registration import RegistrationForm


        def registration:
            if request.method == 'GET':
                form = RegistrationForm()
                context = {
                    'reg_form': form,
                }
                return render(request, 'registration_page.html', context)

            elif request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/')

                context = {
                    'reg_form': form,
                }
                return render(request, 'registration_page.html', context)



    2 Вариант написания через View (более проще и читабельно) registration.py:


        from django.shortcuts import redirect, render
        from django.views import View

        from publication_app.forms.registration import RegistrationForm


        class RegistrationView(View):
            @staticmethod
            def get(request):
                form = RegistrationForm()
                context = {
                    'reg_form': form,
                }
                return render(request, 'registration_page.html', context)

            @staticmethod
            def post(request):
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/')

                context = {
                    'reg_form': form,
                }
                return render(request, 'registration_page.html', context)


# ListView.

    1 Вариант написания main.py:

        class MainPageView(View):
            def get(self, request):
                posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
                image_post = ImagePost.objects.all()
                contex = {'title': 'Hello World',
                          'posts': posts,
                          'image_post': image_post,
                          }
                return render(request, 'main_page.html', contex)

    2 Вариант написания main.py:

        class PostListView(ListView):
            queryset = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
            template_name = 'main_page.html'
            context_object_name = 'posts'

            def get_context_data(self, *, object_list=None, **kwargs):
                contex = super().get_context_data(object_list=object_list, **kwargs)
                context = ['title'] = 'Посты через ListView'
                return context

            def get(self, request, *args, **kwargs):
                return super().get(request, *args, **kwargs)

            def post(self, request, *args, **kwargs):
                pass


Django Rest Framework.

    Django Rest Framework (DRF) — это библиотека, которая работает со стандартными моделями Django
    для создания гибкого и мощного API для проекта.

        Устанавливаем пакет:

            pip install djangorestframework (не забываем обновить requirements.txt)

        Создам в publication_app папку api c двумя папками внутри:

            serializers
            views

        В папках serializers и views создаем файл publications.py

        В файле serializers пишем код:


            from rest_framework import serializers
            from ...models import Post


            class PostSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Post
                    fields = '__all__'                          # вывод всех полей
                    # exclude = ('is_public',)                  # исключения


            # fields и exclude - должно быть одно из них, два вместе не допускается


        В файле views пишем код:


            from rest_framework.mixins import ListModelMixin
            from rest_framework.viewsets import GenericViewSet
            from ..serializers.publications import PostSerializer
            from ...models import Post


            class PostsView(GenericViewSet, ListModelMixin):
                serializer_class = PostSerializer
                queryset = Post.objects.filter(is_public=True)


        В файле urls.py пишем код:


            from django.conf import settings
            from django.conf.urls.static import static
            from django.contrib.staticfiles.urls import staticfiles_urlpatterns
            from django.urls import path

            from publication_app.api.views.publications import PostsView
            from publication_app.views.logout import LogoutUser
            from publication_app.views.registration import RegistrationView
            from publication_app.views.main import MainPageView
            from publication_app.views.authorization import Authorization
            from publication_app.views.profile import Profile_User
            from publication_app.views.posts import PostCreate
            from publication_app.views.update_profile import user_redaction

            urlpatterns = [
                path('', MainPageView.as_view(), name='main_page'),
                path('registration', RegistrationView.as_view(), name='reg_page'),
                path('authorization', Authorization.as_view(), name='auth_page'),
                path('logout', LogoutUser.as_view(), name='logout_page'),
                path('profile/', Profile_User.as_view(), name='profile_page'),
                path('profile/update/', user_redaction, name='update_profile_page'),
                path('post', PostCreate.as_view(), name='post_page'),
                path('api/posts', PostsView.as_view({'get': 'list'}), name='api-posts'),

            ]


            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            urlpatterns += staticfiles_urlpatterns()


        Устанавливаем drf-spectacular:

            pip install drf-spectacular (не забываем обновить requirements.txt)

        В файле settings.py:

            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'publication_app',
                'menu_app',
                'drf_spectacular',                                                  # добавили

            ... и в самом низу


            REST_FRAMEWORK = {                                                      # добавили
                #YOUR SETTINGS
                'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
            }

        Редактируем главный url.py:


            from django.conf import settings
            from django.conf.urls.static import static
            from django.contrib import admin
            from django.contrib.staticfiles.urls import staticfiles_urlpatterns
            from django.urls import path, include
            from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('publication_app.urls')),
                path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
            ]

            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            urlpatterns += staticfiles_urlpatterns()


        Заходим на http://127.0.0.1:8000/api/schema/swagger-ui/


Создание публикаций через API

    Редактируем код в файле models.py:

        from django.contrib.auth.models import User
        from django.core.validators import RegexValidator
        from django.db import models

        # Create your models here.

        class Post(models.Model):
            user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')              # добавили
            created_at = models.DateTimeField(auto_now_add=True)
            title = models.CharField(max_length=256, unique=False, blank=False, null=False)
            text = models.TextField(blank=False, null=False)
            is_public = models.BooleanField(default=True)


        class Profile(models.Model):
            user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
            avatar = models.ImageField(blank=True, null=True)
            phone = models.CharField(
                validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
                max_length=17,
                blank=True,
                null=True,
            )
            about = models.TextField(max_length=4096, blank=True, null=True)
            github_link = models.URLField(blank=True, null=True)


        class ImagePost(models.Model):
            post = models.ForeignKey(Post, on_delete=models.CASCADE)
            image_post = models.ImageField(null=True, blank=True)


    В терминале вводим команду:


        python manage.py makemigrations

    В терминале выведет запрос после миграции python manage.py makemigrations :


        It is impossible to add a non-nullable field 'user' to post without specifying a default. This is because the database needs something to populate existing rows.
        Please select a fix:
         1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
         2) Quit and manually define a default value in models.py.


            Выбираем :


                1 Enter
                1 Enter

    Применяем миграции:


        python manage.py migrate


    Редактируем файл publications.py в api(views):

        from rest_framework import filters
        from rest_framework.mixins import ListModelMixin, CreateModelMixin
        from rest_framework.viewsets import GenericViewSet
        from ..serializers.publications import PostSerializer
        from ...models import Post


        class PostsView(GenericViewSet, ListModelMixin, CreateModelMixin):
            serializer_class = PostSerializer
            queryset = Post.objects.filter(is_public=True)
            filter_backends = [filters.OrderingFilter]
            ordering_field = ['created_at', 'id']


    Редактируем файл urls.py:

        from django.conf import settings
        from django.conf.urls.static import static
        from django.contrib.staticfiles.urls import staticfiles_urlpatterns
        from django.urls import path

        from publication_app.api.views.publications import PostsView
        from publication_app.views.logout import LogoutUser
        from publication_app.views.registration import RegistrationView
        from publication_app.views.main import MainPageView
        from publication_app.views.authorization import Authorization
        from publication_app.views.profile import Profile_User
        from publication_app.views.posts import PostCreate
        from publication_app.views.update_profile import user_redaction

        urlpatterns = [
            path('', MainPageView.as_view(), name='main_page'),
            path('registration', RegistrationView.as_view(), name='reg_page'),
            path('authorization', Authorization.as_view(), name='auth_page'),
            path('logout', LogoutUser.as_view(), name='logout_page'),
            path('profile/', Profile_User.as_view(), name='profile_page'),
            path('profile/update/', user_redaction, name='update_profile_page'),
            path('post', PostCreate.as_view(), name='post_page'),
            path('api/posts', PostsView.as_view({'get': 'list', 'post': 'create'}), name='api-posts'),              # редактируем create - отвечает за создание пользователя

        ]


        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += staticfiles_urlpatterns()


    Редактируем файл publications.py в api(serializers):


        from rest_framework import serializers
        from ...models import Post


        class PostSerializer(serializers.ModelSerializer):
            class Meta:
                model = Post
                fields = '__all__'                                              # вывод всех полей
                read_only_fields = ('id', 'user', 'is_public')

               publisher_user = serializers.HiddenField(
                default=serializers.CurrentUserDefault(),
                source='user'
               )


    Переходим на страницу:

            http://127.0.0.1:8000/api/schema/swagger-ui/

            В Request body пишем код:

                {
                  "title": "API POST",
                  "text": "blabla"
                }

            Нажимаем Execute

        Запись создана.
"""