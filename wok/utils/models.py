from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseSeo(models.Model): 
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    keywords = models.TextField(verbose_name='Ключевые слова')

    class Meta:
        abstract = True


class Client(models.Model):
    user = models.Model(User, on_delete=models.CASCADE)