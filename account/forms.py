from django import forms
from account.models import CustomUser
class CreateUser(UserCreationForm):

    class Meta:
        model=CustomUser
        fields=('username', 'email')
