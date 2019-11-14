from django.shortcuts import render
from django.views.generic.edit import CreateView

from account.models import CustomUser

class CreateUser(CreateView):
    template_name='account/add_user.html'
    model = CustomUser
    fields=['user']

    def form_valid(self, form):
        print('The new user')
        print(form)
        pass
