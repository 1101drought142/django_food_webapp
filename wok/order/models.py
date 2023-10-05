from django.db import models

class Promocode(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код')
    discount = models.FloatField(verbose_name='Скидка', null=True, blank=True)
    percent_discount = models.IntegerField(verbose_name='Процент скидки', null=True, blank=True)
    pass

class CartItem(models.Model):
    pass

class Order(models.Model):
    pass

class Cart(models.Model):
    pass