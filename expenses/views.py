from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView

from expenses.models import Category, Expenses

# Create your views here.
class PersonExpenses(View):
    models=Expenses
    template_name='person_expenses.html'

    def post(self, request):
        print("Data in this part of the project")
        pass

    def get(self, request):
        return render(request, self.template_name)
        pass

class CreateCategory(CreateView):
    model=Category
    template_name='create_category.html'
    fields=['expense','circle_repetition']

    def form_valid(self, form):
        print('*************')
        pass
