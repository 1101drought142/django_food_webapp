from django.db import models

# Create your models here.

class ModificatorGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    uniquecode = models.CharField(max_length=255, verbose_name='Уникальный код')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа модификаторов'
        verbose_name_plural = 'Группы модификаторов'

class Modificator(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    group = models.ForeignKey('ModificatorGroup', on_delete=models.CASCADE, verbose_name='Группа модификаторов')
    uniquecode = models.CharField(max_length=255, verbose_name='Уникальный код')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модификатор'
        verbose_name_plural = 'Модификаторы'

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(verbose_name='Изображение')

    def __str__(self): 
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    uniquecode = models.CharField(max_length=255, verbose_name='Уникальный код')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    sale_price = models.FloatField(verbose_name='Цена со скидкой', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')
    uniquecode = models.CharField(max_length=255, verbose_name='Уникальный код')
    modificators = models.ManyToManyField('ModificatorGroup', verbose_name='Группы модификаторов', null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'