from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView

from expenses.models import Category, Entry, Income

# Create your views here.
def TodoList(request):
    return render(request,'person_expenses.html')

class PersonData(View):
    model = Entry
    template_name = 'expenses/summary.html'

    def post(self, request):
        print("Data in this part of the project")
        pass

    def get(self, request, user):
        categories= Category.objects.filter(user__id=user)
        expenses = Entry.objects.filter(user_id=user)
        income = Income.objects.filter(user_id=user)
        data = {
            'categories':categories,
            'expenses':expenses,
            'income':income
        }
        return render(request, self.template_name, data)

class CreateCategory(CreateView):
    model = Category
    template_name = 'expenses/create_category.html'
    fields = ['expense','circle_repetition','user','name']
    # def url

class AddEntry(CreateView):
    model = Entry
    template_name = 'expenses/add.html'
    fields = ('user','category','description','price')

    def form_valid(self, form):
        print('********')
        print(form)
        print('********')
        return super().form_valid(form)

class AddIncome(CreateView):
    model = Income
    template_name ='income/add.html'
    fields = ('user', 'circle_repetition', 'repition', 'description', 'amount')
