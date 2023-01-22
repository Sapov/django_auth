from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(max_length=20, verbose_name='Электронная почта')
    phone = models.CharField(max_length=17, verbose_name='Телефон')
    whatsapp = models.CharField(max_length=20, verbose_name='WhatsApp', help_text="Указать наличие")
    telegram = models.CharField(max_length=20, verbose_name='Telegram', help_text="Указать @ник")
    country = models.CharField(max_length=12, verbose_name='Страна')
    region = models.CharField(max_length=20, verbose_name='Регион, Область')
    city = models.CharField(max_length=12, verbose_name='Город')
    category = models.CharField(max_length=12, verbose_name='Категория')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update


    class Meta:
        verbose_name_plural = 'Профиль'
        verbose_name = 'Профили'
        ordering = ['name']

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


