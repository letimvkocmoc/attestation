from typing import List

from django.contrib import admin
from sole_trader.models import *


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display: List = ['email', 'country', 'city', 'street', 'house_number']
    list_filter: List = ['country', 'city']
    search_fields: List = ['email', 'country', 'city', 'street', 'house_number']
    list_per_page = 10
    list_max_show_all = 50


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display: List = ['title', 'model', 'release_date']
    list_filter: List = ['title', 'model', 'release_date']
    search_fields: List = ['title', 'model', 'release_date']
    list_per_page = 10
    list_max_show_all = 50


@admin.register(SoleTrader)
class SoleTraderModelAdmin(admin.ModelAdmin):
    list_display: List = ['title', 'contacts', 'products', 'supplier', 'debt', 'created']
