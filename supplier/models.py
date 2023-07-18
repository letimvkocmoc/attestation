from django.db import models


class Supplier(models.Model):

    class Choice(models.IntegerChoices):
        factory = 0, 'Завод'
        retail_network = 1, 'Розничная сеть'
        sole_trader = 2, 'Индивидуальный предприниматель'

    class Meta:
        verbose_name: str = 'Поставщик'
        verbose_name_plural: str = 'Поставщики'

    editable_choices = Choice.choices
    editable_choices.pop(0)

    title = models.PositiveIntegerField(verbose_name='Поставщик', choices=Choice.choices)
