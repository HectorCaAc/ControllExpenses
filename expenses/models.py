from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import get_user_model
User = get_user_model()

from account.models import CustomUser

#There are some categories that are the same expense ex insurance
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    circle_repetition = models.IntegerField()
    name=models.CharField(max_length=255)
    current_circle = models.IntegerField(default=0)
    deficit = models.BooleanField(default=True)
    spend_available = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def get_absolute_url(self):
        return reverse(
            'expenses:person_expenses'
        )

    def __str__(self):
        return self.name

    def next_cycle(self):
        days_left = self.current_circle -1
        if days_left == -1:
            days_left = self.circle_repetition
            self.spend_available = self.expense
            self.deficit = False
        self.current_circle = days_left
        self.save()

    def new_spend(self):
        current_start_circle = self.circle_repetition - self.current_circle
        start_circle = timezone.now()-timedelta(days=current_start_circle)
        expenses = Entry.objects.filter(user=self.user,
                                            date__gte=start_circle,
                                            category=  self.pk)
        spend_circle = 0
        surplus = False
        for expense in expenses:
            spend_circle += expense.price
        print('{} and expense {} total {}'.format(self.name, self.expense,spend_circle))
        if spend_circle > self.expense:
            surplus = True
        self.deficit = surplus
        self.spend_available = self.expense - spend_circle
        self.save()

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse(
            'expenses:person_expenses'
        )

    def save(self, *args, **kwargs):
        super(Entry,self).save()
        customerUser = CustomUser.objects.get(user=self.user)
        customerUser.current_balance -= self.price
        customerUser.save()
        self.category.new_spend()

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    circle_repetition = models.IntegerField()
    current_circle = models.IntegerField(default=0)
    repition = models.BooleanField(null=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def next_cycle(self):
        if self.repition:
            days_left = self.current_circle -1
            if days_left == -1:
                days_left = self.circle_repetition
            self.current_circle = days_left
            self.save()

    def get_absolute_url(self):
        return reverse(
            'expenses:person_expenses',
        )

    def save(self, *args, **kwargs):
        super(Income, self).save()
        customerUser = CustomUser.objects.get(user=self.user)
        customerUser.current_balance += self.amount
        customerUser.save()
