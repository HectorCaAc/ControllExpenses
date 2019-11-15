from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView

from expenses.models import Category, Expenses

# Create your views here.
class PersonData(View):
    models=Expenses
    template_name='expenses/summary.html'

    def post(self, request):
        print("Data in this part of the project")
        pass

    def get(self, request, user):
        categories= Category.objects.filter(user__id=user)
        expenses = Expenses.objects.filter(user_id=user)
        data ={
            'categories':categories,
            'expenses':expenses
        }
        return render(request, self.template_name, data)

class CreateCategory(CreateView):
    model=Category
    template_name='expenses/create_category.html'
    fields=['expense','circle_repetition','user','name']
    # def url

class AddExpense(CreateView):
    model=Expenses
    template_name='expenses/add.html'
    fields=('user','categories','description','price')
