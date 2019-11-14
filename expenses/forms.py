from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser

class ExpensesForm(forms.Form):
    description = forms.CharField(max_length=255,)
