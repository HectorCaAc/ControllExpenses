from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

#There are some categories that are the same expense ex insurance
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    circle_repetition = models.IntegerField()
    name=models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse(
            'expenses:person_expenses',
            kwargs={
                'user':self.user.id
            }
        )

    def __str__(self):
        return self.name


class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey('Category',on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse(
            'expenses:person_expenses',
            kwargs={
                'user':self.user.id
            }
        )
