from typing import List

from django.contrib import admin
from supplier.models import *


@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display: List = ['title']
