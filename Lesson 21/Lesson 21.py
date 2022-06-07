# Медиа (загрузка картинок и файлов)
# Router


"""
Медиа (загрузка картинок и файлов)


    В файле settings.py добавляем:

        SPECTACULAR_SETTINGS = {
            'COMPONENT_SPLIT_REQUEST': True
        }

    Создаем новый APP:

         python manage.py startapp media_app


    В файле models.py создаем модель:

        from django.contrib.auth.models import User
        from django.db import models


        class Media(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
            file = models.ImageField(blank=True,null=False)
            uploaded_at = models.DateTimeField(auto_now_add=True)


    В файле settings.py редактируем INSTALLED_APPS:


            INSTALLED_APPS = [
                '#############',
                'media_app',
            ]


    В терминале вводим команду:

        python manage.py makemigrations
        python manage.py migrate


    Создам в media_app папку api c двумя папками внутри:

            serializers
            views

    В папках serializers и views создаем файл media.py

        В файле serializers пишем код:


            from rest_framework import serializers
            from ...models import Media

            class MediaSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Media
                    fields = '__all__'
                    read_only_fields = ['user']


                publisher_user = serializers.HiddenField(
                    default=serializers.CurrentUserDefault(),
                    source='user'
                )


        В файле views пишем код:


            from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
            from rest_framework.viewsets import GenericViewSet
            from ...media_app.api.serializers.media import MediaSerializer
            from ...media_app.models import Media


            class MedaViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin)
                serializer_class = MediaSerializer
                queryset = Media.objects.all()


        В файле urls.py (а так же редактирование главного urls.py ( path('', include('media_app.urls')), )):


            from django.urls import path
            from media_app.api.views.media import MedaViewSet

            urlpatterns = [
                path('api/media/', MedaViewSet.as_view{'get': 'retrieve', 'post': 'create', 'delete': 'destroy'), name='api_media')
            ]

        В файле models.py редактируем Post:


            class Post(models.Model):
                user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts', null=True)
                created_at = models.DateTimeField(auto_now_add=True)
                title = models.CharField(max_length=256, unique=False, blank=False, null=False)
                text = models.TextField(blank=False, null=False)
                is_public = models.BooleanField(default=True)
                tag = models.ForeignKey(Tag, on_delete=models.PROTECT, verbose_name='Tags')
                file = models.ForeignKey(Media, on_delete=models.SET_NUll, null=True, blank=True)


        В терминале вводим команду:

            python manage.py makemigrations
            python manage.py migrate


        В файле publications.py редактируем код:


            from rest_framework import serializers
            from media_app.models import Post


            class PostSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Post
                    exclude = ['is_public']                                                     # добавили
                    read_only_fields = ('id', 'user', 'is_public')
                    extra_kwargs = {
                        'file': {
                            'required': True,
                            'write_only': True,
                            'help_text': 'ID медиа файла',
                        },
                    }


                publisher_user = serializers.HiddenField(
                    default=serializers.CurrentUserDefault(),
                    source='user'
                )
                media = serializers.URLField(source='file.file.url', read_only = True)          # добавили


Router


    В папке publication_app/api/views создаем файл route.py и пишем код:


        from rest_framework import routers
        from .publications import PostsViewSet


        api_router = router.DefaultRouter()
        api_router.register('posts', PostsViewSet)


    Редактируем файл urls.py:


        from django.urls import path
        from publication_app.api.views.router import api_router
        from publication_app.views.main import MainPageView, PostListView


        urlpatterns = [
            path('api', include(api_router.urls)),
        ]
"""