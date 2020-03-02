from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from expenses.models import Category, Entry, Income
from expenses.forms import EntryForm
from account.models import CustomUser

# Create your views here.
def TodoList(request):
    return render(request,'person_expenses.html')

class PersonData(LoginRequiredMixin, FormView):
    template_name = 'expenses/summary.html'
    log_in='user/login'
    success_url = 'expenses/user/'
    fields = ('circle_repetition', 'repition', 'description', 'amount')
    form_class = EntryForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, user=request.user)
        if self.form_valid(form):
                form.save()
        return self.get(request)

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
            'balance': balance,
            'form': self.form_class(user=user)
        }
        return render(request, self.template_name, data)

    def form_valid(self, form):
        print(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

class Summary(View):
    template_name = 'expenses/report.html'

    def get(self, request):
        user = request.user
        balance = CustomUser.objects.get(user=user).current_balance
        last_income = 'TODO'
        next_income = 'TODO'
        last_entry = Entry.objects.filter(user=user).order_by('-id').last()
        data={
            'last_entry':last_entry,
            'balance':balance,
            'last_income': 'TODO',
            'next_income': 'TODO',
            'last_expense': last_entry,
            'next_expense': 'TODO'
        }
        return render(request, self.template_name, data)

class CreateCategory(LoginRequiredMixin, CreateView):
    log_in='user/login'
    model = Category
    template_name = 'expenses/create_category.html'
    fields = ['expense','circle_repetition','name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.spend_available = form.instance.expense
        form.instance.current_circle = form.instance.circle_repetition
        return super().form_valid(form)

class AddEntry(LoginRequiredMixin, CreateView):
    form_class = EntryForm
    log_in='user/login'
    template_name = 'expenses/add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.category = Category.objects.filter(user= self.request.user)
        return super(CreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(AddEntry, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class AddIncome(LoginRequiredMixin, CreateView):
    model = Income
    template_name ='income/add.html'
    fields = ('circle_repetition', 'repition', 'description', 'amount')
    log_in='user/login'

    def get(self,*args, **kwargs):
        print(args)
        print(kwargs)
        return super().get(*args, **kwargs)

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.user = self.request.user
        form.instance.current_circle = form.instance.circle_repetition
        return super().form_valid(form)
