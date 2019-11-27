from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from expenses.models import Category, Entry, Income
from account.models import CustomUser

# Create your views here.
def TodoList(request):
    return render(request,'person_expenses.html')

class PersonData(LoginRequiredMixin, View):
    model = Entry
    template_name = 'expenses/summary.html'
    log_in='user/login'

    def post(self, request):
        print("Data in this part of the project")
        pass

    def get(self, request):
        user = request.user
        balance = CustomUser.objects.get(user=user).current_balance
        categories= Category.objects.filter(user=user)
        expenses = Entry.objects.filter(user=user)
        income = Income.objects.filter(user=user)
        data = {
            'categories':categories,
            'expenses':expenses,
            'income':income,
            'balance': balance
        }
        return render(request, self.template_name, data)

class CreateCategory(LoginRequiredMixin, CreateView):
    log_in='user/login'
    model = Category
    template_name = 'expenses/create_category.html'
    fields = ['expense','circle_repetition','user','name']

class AddEntry(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'expenses/add.html'
    fields = ('user','category','description','price')
    log_in='user/login'

    def form_valid(self, form):
        print('********')
        print(form)
        print('********')
        return super().form_valid(form)

class AddIncome(LoginRequiredMixin, CreateView):
    model = Income
    template_name ='income/add.html'
    fields = ('user', 'circle_repetition', 'repition', 'description', 'amount')
    log_in='user/login'
