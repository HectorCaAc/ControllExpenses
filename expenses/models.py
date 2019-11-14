from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    circle_repetition = models.IntegerField()

# Create your models here.
class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey('Category',on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now=True)
