from django.db import models
from django.utils import timezone

from supplier.models import Supplier


class Contact(models.Model):

    class Meta:
        verbose_name: str = 'Контакт ИП'
        verbose_name_plural: str = 'Контакты ИП'

    email = models.EmailField(max_length=255, unique=True, verbose_name='Эл. почта')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=255, verbose_name='Номер дома')


class Product(models.Model):

    class Meta:
        verbose_name: str = 'Продукт ИП'
        verbose_name_plural: str = 'Продукты ИП'

    title = models.CharField(max_length=255, unique=True, verbose_name='Продукт')
    model = models.CharField(max_length=255, blank=True, null=True, verbose_name='Модель')
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата выхода товара')


class SoleTrader(models.Model):

    class Meta:
        verbose_name: str = 'Индивидуальный предприниматель'
        verbose_name_plural: str = 'Индивидуальные предприниматели'

    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    contacts = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name='Контакты')
    products = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукты')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=30, decimal_places=2, default=0, verbose_name='Задолженность перед поставщиком')
    created = models.DateTimeField(verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
