from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from expenses.models import Category, Entry

class EntryForm (forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['category','description','price']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
