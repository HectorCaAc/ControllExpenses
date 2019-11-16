from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone

from datetime import timedelta

from django.contrib.auth import get_user_model
User = get_user_model()

#There are some categories that are the same expense ex insurance
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    circle_repetition = models.IntegerField()
    name=models.CharField(max_length=255)
    current_circle = models.IntegerField(default=0)
    surplus = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse(
            'expenses:person_expenses',
            kwargs={
                'user':self.user.id
            }
        )
    def __str__(self):
        return self.name

    def next_cycle(self):
        days_left = self.current_circle -1
        if days_left == -1:
            days_left = self.circle_repetition
        self.current_circle = days_left
        self.save()

    def update_status(self):
        current_start_circle = self.circle_repetition - self.current_circle
        start_circle = timezone.now()-timedelta(days=current_start_circle)
        expenses = Expenses.objects.filter(user=self.user, data__gte=start_circle )
        total_expense = 0
        surplus = True
        for expense in expenses:
            total_expense += expense.price
        if total_expense > self.expense:
            surplus = False
        self.surplus = surplus
        self.save()

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
    def save(self, *args, **kwargs):
        self.categories.update_status()
        super(Expenses,self).save()
