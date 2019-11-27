from django.contrib import admin
from expenses.models import Category, Entry
# Register your models here.
admin.site.register(Category)
admin.site.register(Entry)
