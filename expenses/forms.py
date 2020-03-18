from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from expenses.models import Category, Entry, Income

class EntryForm (forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['category','description','price']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=self.user)

class CategoryForm(forms.ModelForm):
    class Meta:
        model  = Category
        fields = ['expense', 'circle_repetition', 'name']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['description', 'amount', 'repition', 'circle_repetition']
