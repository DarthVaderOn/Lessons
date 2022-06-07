# Likes
# Comments
# Поиск через фильтр в API
# Поиск через Admin


"""
Likes


    Создаем новое приложение через команду:


        python manage.py startapp likes_app


    Открываем файл models.py и пишем код:


        class LikePost(models.Model):
            post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='likes')
            user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='likes')

            class Meta:
                unique_together =(('post', 'user'),)


    Открываем файл likes_app/api/serializers/likes.py и пишем код:


        class LikePostSerializer(serializers.ModelSerializer):
            class Meta:
                model = LikePost
                fields = '__all__'                                 # вывод всех полей
                read_only_fields = ['user']


            publisher_user = serializers.HiddenField(              # для того чтобы мы не могли назначить пользователя
                default=serializers.CurrentUserDefault(),
                source='user'
            )


    Открываем файл likes_app/api/views/likes.py и пишем код:


        from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
        from rest_framework.viewsets import GenericViewSet
        from ..serializers.likes import LikePostSerializer, LikeCommentSerializer
        from likes_app.models import LikePost


        class LikePostsViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
            serializer_class = LikePostSerializer
            queryset = LikePost.objects.all()


    Открываем файл likes_app/api/views/router.py и пишем код:


        from rest_framework import routers
        from .likes import LikePostsViewSet

        api_router = routers.DefaultRouter()
        api_router.register('likes', LikePostsViewSet)


    В settings.py добавляем:


        INSTALLED_APPS = [
            'likes_app',
        ]


    В глобальный urls.py добавим:


        path('', include('likes_app.urls')),


    В терминале вводим команду:

        python manage.py makemigrations
        python manage.py migrate


    Для отображения likes переходим в publication_app/api/serializers/publications.py:


        from rest_framework import serializers
        from media_app.api.serializers.media import MediaFileSerializer
        from publication_app.models import Post
        from tags_app.api.serializers.tags import TagSerializer


        class PostSerializer(serializers.ModelSerializer):


            class Meta:
                model = Post
                exclude = ['is_public']
                read_only_fields = ('id', 'user', 'is_public',)
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


            likes_count = serializers.SerializerMethodField()           # добавили

            def get_likes_count(self, instance) -> int:                 # добавили
                return instance.likes.count()


Comments


    Создаем новое приложение через команду:


        python manage.py startapp comments_app


    Открываем файл models.py и пишем код:


        from django.db import models
        from publication_app.models import Post
        from profile_app.models import User


        # Create your models here.


        class Comments(models.Model):
            created_at = models.DateTimeField(auto_now_add=True)
            update_at = models.DateTimeField(auto_now=True)
            text = models.TextField(blank=False, null=False)
            post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
            user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')


    Открываем файл comments_app/api/serializers/comments.py и пишем код:


        from rest_framework import serializers
        from comments_app.models import Comments


        class CommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comments
                fields = '__all__'                                # вывод всех полей
                read_only_fields = ['user']


            publisher_user = serializers.HiddenField(
                default=serializers.CurrentUserDefault(),
                source='user'
            )


    Открываем файл comments_app/api/views/comments.py и пишем код:


        from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
        from rest_framework.viewsets import GenericViewSet
        from ..serializers.comments import CommentSerializer
        from comments_app.models import Comments


        class CommentsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
            serializer_class = CommentSerializer
            queryset = Comments.objects.all()


    Открываем файл comments_app/api/views/router.py и пишем код:


        from rest_framework import routers
        from .comments import CommentsViewSet


        api_router = routers.DefaultRouter()
        api_router.register('comments', CommentsViewSet)


    В settings.py добавляем:


        INSTALLED_APPS = [
            'comments_app',
        ]


    В глобальный urls.py добавим:


        path('', include('comments_app.urls')),


    В терминале вводим команду:

        python manage.py makemigrations
        python manage.py migrate


    Для отображения comments переходим в publication_app/api/serializers/publications.py:


        from rest_framework import serializers
        from media_app.api.serializers.media import MediaFileSerializer
        from publication_app.models import Post
        from tags_app.api.serializers.tags import TagSerializer


        class PostSerializer(serializers.ModelSerializer):


            class Meta:
                model = Post
                exclude = ['is_public']
                read_only_fields = ('id', 'user', 'is_public',)
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


            likes_count = serializers.SerializerMethodField()
            comments_count = serializers.SerializerMethodField()           # добавили

            def get_likes_count(self, instance) -> int:
                return instance.likes.count()

            def get_comments_count(self, instance) -> int:                 # добавили
                return instance.comments.count()


Поиск через фильтр в API


    Для добавления поиска переходим publication_app/api/views/publications.py:


            from rest_framework import filters
            from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
            from rest_framework.viewsets import GenericViewSet
            from ..serializers.publications import PostSerializer
            from publication_app.models import Post


            # CRUD
            class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
                serializer_class = PostSerializer
                queryset = Post.objects.filter(is_public=True)
                filter_backends = [filters.OrderingFilter, filters.SearchFilter]            # добавили
                ordering_field = ['created_at', 'id']
                search_fields = ['=id', 'title', 'text', 'user__username']                  # добавили '=' - полное совпадение


                def perform_destroy(self, instance):
                    instance.is_public = False
                    instance.save()


Поиск через Admin


    Для добавления поиска переходим publication_app/admin.py:


        from django.contrib import admin
        from django.utils.safestring import mark_safe
        from publication_app.models import Media, Post

        # Register your models here.


        class MenuItemAdmin(admin.StackedInline):
            model = Media
            list_display = ('image_post','preview')
            readonly_fields = ('image_post','preview')


            def preview(self, obj):
                if obj.image_post:
                    return mark_safe(
                        f'<a target=_blank href={obj.image_post.url}>'
                        f'<img src={obj.image_post.url} width="100" height="100">'
                        f'</a>'
                    )


        @admin.register(Post)
        class PostAdmin(admin.ModelAdmin):
            inlines = (
                MenuItemAdmin,
            )
            list_display = ('id', 'title', 'user', 'tag', 'created_at', 'is_public',)
            ordering = ('-created_at', '-id',)
            readonly_fields = ('created_at',)
            list_editable = ('is_public', 'tag', 'user',)
            search_fields = ('title', 'text')                                      # добавили

"""