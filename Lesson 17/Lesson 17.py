# Создание Profile
# Вывод информации из Profile в User
# Сигналы (при регистрации создается Profile для User)
# Кастомная миграция(для тех пользователей которые регистрировались до создания Profile в Users, и отсутствовали в БД в таблице publication_app_profile )

"""
Создание Profile


    открываем файл models.py под Post пишем код:

        from django.contrib.auth.models import User
        from django.core.validators import RegexValidator
        from django.db import models

        # Create your models here.

        class Post(models.Model):
            created_at = models.DateTimeField(auto_now_add=True)
            title = models.CharField(max_length=256, unique=False, blank=False, null=False)
            text = models.TextField(blank=False, null=False)
            is_public = models.BooleanField(default=True)
            image = models.ImageField(null=True, blank=True)


        class Profile(models.Model):
            user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')     on_delete - в случае удаления User удалится и его данные
            avatar = models.ImageField(blank=True, null=True)
            phone = models.CharField(
                validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],                              проверка на правильность ввода номера (валидность)
                max_length=17,
                blank=True,
                null=True,
            )
            about = models.TextField(max_length=4096, blank=True, null=True)
            github_link = models.URLField(blank=True, null=True)


    открываем файл admin.py под @admin.register(Post) пишем код:

        @admin.register(Profile)
        class ProfileAdmin(admin.ModelAdmin):
            pass


    применяем миграцию:

        python manage.py makemigrations
        python manage.py migrate


    открываем файл form / registration.py редактируем код:

        from django.contrib.auth.models import User
        from django import forms

        from publication_app.models import Profile


        class RegistrationForm(forms.ModelForm):
            class Meta:
                model = User
                fields = ('username', 'email', 'password',)

            def save(self, commit=True):
                user = super(RegistrationForm, self).save(commit=False)
                user.set_password(self.cleaned_data['password'])

                if commit:                                                                  # добавляем изменения
                    user.save()

                    profile = Profile(user=user)
                    profile.save()

                return user


Вывод информации из Profile в User


    открываем admin.py и редактируем код:

        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin as UserAdminBase
        from django.contrib.auth.models import User

        from .models import Post, Profile


        # Register your models here.


        @admin.register(Post)
        class PostAdmin(admin.ModelAdmin):
            list_display = ('id', 'title', 'created_at',)
            ordering = ('-created_at', '-id',)
            readonly_fields = ('created_at',)


        admin.site.unregister(User)                                                         # отключаем админку и снова запускаем (в постах пропадут картинки)


        class ProfileInline(admin.StackedInline):
            model = Profile


        @admin.register(User)
        class UserAdmin(UserAdminBase):
            inlines = (
                ProfileInline,
            )


Сигналы (при регистрации создается Profile для User)


    Создаем папку signals в publication_app:

        В этой папке создаем файл __init__.py
        В этой папке создаем файл user.py


            В user.py пишем код:

                from django.contrib.auth.models import User
                from django.db.models.signals import post_save
                from django.dispatch import receiver

                from publication_app.models import Profile


                @receiver(post_save, sender=User)
                def create_profile(sender, instance, created, *args, **kwargs):
                    if not created:
                        return

                    profile = Profile(user=instance)
                    profile.save()


    Открываем файл apps.py и пишем код:


        from django.apps import AppConfig


        class PublicationAppConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'publication_app'

            def ready(self):                                                                            # дополнили
                from .signals import user


Кастомная миграция(для тех пользователей которые регистрировались до создания Profile в Users, и отсутствовали в БД в таблице publication_app_profile )


    Создаем файл в папке migrations в зависимости от номера последней миграции (например: у нас есть 2 миграции: 0001_initial.py и 0002_alter_profile_about_alter_profile_phone.py.
    То мы создаем файл с названием в начале 0003_#####):


        В файле 0003_##### пишем код:

            from django.db import migrations


            def create_profile_for_existing_users(apps, schemas_editors):
                user_model = apps.get_model('auth', 'User')
                profile_model = apps.get_model('publication_app', 'Profile')


                users = user_model.objects.filter(profile__isnull=True).all()
                for user in users:
                    profile = profile_model(user=user)
                    profile.save()


            class Migration(migrations.Migration):
                dependencies = (
                    ('publication_app', '0002_alter_profile_about_alter_profile_phone'),
                )

                operations = (
                    migrations.RunPython(create_profile_for_existing_users),
                )

        применяем миграцию:

        python manage.py makemigrations
        python manage.py migrate

    Теперь пользователи которые зарегистрировались ранее создания Profile появятся в БД в таблице publication_app_profile
"""