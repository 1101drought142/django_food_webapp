from django.db import models

# Create your models here.
class BaseSeo(models.Model): 
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    keywords = models.TextField(verbose_name='Ключевые слова')

    class Meta:
        abstract = True