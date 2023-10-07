from django.db import models
from utils.models import Client
from items.models import Item

class Promocode(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код')
    discount = models.FloatField(verbose_name='Скидка', null=True, blank=True)
    percent_discount = models.IntegerField(verbose_name='Процент скидки', null=True, blank=True)
    pass

class CartItem(models.Model):
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    pass

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    pass

class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    pass