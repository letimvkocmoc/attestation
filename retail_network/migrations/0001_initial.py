# Generated by Django 4.2.3 on 2023-07-18 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Эл. почта')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=255, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Продукт')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выхода товара')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Задолженность перед поставщиком')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='retail_network.contact', verbose_name='Контакты')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='retail_network.product', verbose_name='Продукты')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
        ),
    ]
