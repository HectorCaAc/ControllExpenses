from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView

from account.models import Category, Expenses

from account.models import Expenses

# Create your views here.
class PersonExpenses(View):
    models=Expenses
    template_name='person_expenses.html'

    def post(self, request):
        pass

    def get(self, request):
        return render(request, self.template_name)
        pass

class CreateCategory(CreateView):
    model=Category
    template_name='create_category.html'
    fields=['expense','circle_repetition']

    def form_valid(self, form):
        pass
