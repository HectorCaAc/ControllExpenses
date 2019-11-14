from django.contrib import admin
from expenses.models import Category, Expenses
# Register your models here.
admin.site.register(Category)
admin.site.register(Expenses)
