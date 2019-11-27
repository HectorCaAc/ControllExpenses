from django import forms
from django.forms import ModelForm
from account.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    currentMoneyAmount = forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model=get_user_model()
        fields=('username','password1','password2','currentMoneyAmount')
        widgets ={
            'password':forms.PasswordInput()
        }

class LogInForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())
