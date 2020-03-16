from datetime import timedelta, datetime

from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from expenses.models import Category, Entry, Income
from expenses.forms import EntryForm
from account.models import CustomUser

# Create your views here.
def TodoList(request):
    return render(request,'index.html')

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
        balance = CustomUser.objects.filter(user=user)
        if not balance.exists():
            return redirect('/')
        balance = balance.first().current_balance
        categories = Category.objects.filter(user=user)
        expenses = Entry.objects.filter(user=user)
        income = Income.objects.filter(user=user)
        data = {
            # 'categories':categories,
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

class Summary(LoginRequiredMixin, View):
    template_name = 'expenses/report.html'

    def get_last_income(self, user):
        income = Income.objects.filter(user=user)
        if income.exists():
            income = income.order_by('-date').first()
            date = timezone.now()+timedelta(days=income.current_circle)
            date_format = datetime.strftime(date, '%B %d, %Y')
            return '{}|{}|{}'.format(date_format, income.description, income.amount)
        return 'NO INCOME YET'

    def get_next_income(self, user):
        income = Income.objects.filter(user=user, repition=True).order_by('current_circle')
        if income.exists():
            income = income.first()
            date = timezone.now()+timedelta(days=income.current_circle)
            date_format = datetime.strftime(date, '%B %d, %Y')
            return '{}|{}|{}'.format(date_format, income.description, income.amount)
        else:
            return 'No income yet'

    def get(self, request):
        user = request.user
        balance = CustomUser.objects.get(user=user).current_balance
        last_income = self.get_last_income(user)
        next_income = self.get_next_income(user)
        last_entry = Entry.objects.filter(user=user).order_by('-id')
        if last_entry.exists():
            date_format =datetime.strftime(last_entry.last().date, '%B %d, %Y')
            last_entry = '{}|{}|{}'.format(date_format, last_entry.description, last_entry.price)
        else:
            last_entry = 'No Entry yet'
        data={
            'last_entry':last_entry,
            'balance':balance,
            'last_income': last_income,
            'next_income': next_income,
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

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'expenses/category.html'

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.filter(user=self.request.user)
        return query_set

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

class AddEntryAPI(LoginRequiredMixin, View):
    
    def post(self, request):
        form = EntryForm(request.POST, user=request.user)
        form.instance.user = request.user
        if form.is_valid():
            print('The entry is a valid entry')
            form.save()
        else:
            print('It was not possible to store the entry')
        return redirect('/expenses/user/')

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

