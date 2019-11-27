from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.forms import CreateUserForm, LogInForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from account.models import CustomUser

def CreateUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            current_balance = form.cleaned_data['currentMoneyAmount']
            user = User.objects.create_user(user_name,password=password)
            add_customer = CustomUser(user=user, current_balance=current_balance)
            add_customer.save()
            return redirect('accounts:log_in')
    else:
        print('Create new user')
        form = CreateUserForm()
    return render(request, 'account/add_user.html', {'form':form})

def LogIn(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            print(form)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('expenses:person_expenses')
        else:
            print('The form is not valid')
    else:
        form = LogInForm()
    return render(request, 'account/login.html',{'form':form})

def LogOut(request):
    logout(request)
    return render(request, 'person_expenses.html')
