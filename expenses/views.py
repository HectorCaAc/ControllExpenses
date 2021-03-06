from datetime import timedelta, datetime

from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum, Count

from expenses.models import Category, Entry, Income
from expenses.forms import EntryForm, CategoryForm, IncomeForm
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
                print('*'*10)
                print('FORM VALID')
        else:
            print('*'*10)
            print('There is an error with the entry enter')
        return self.get(request)

    def get(self, request):
        user = request.user
        balance = CustomUser.objects.filter(user=user)
        if not balance.exists():
            return redirect('/')
        balance = balance.first().current_balance
        categories = Category.objects.filter(user=user).order_by('expense')
        expenses = Entry.objects.filter(user=user).order_by('-price')
        income = Income.objects.filter(user=user)
        user_income = income.aggregate(Sum('amount'))
        user_expense = expenses.aggregate(Sum('price'))
        print('*'*10+'Getting Data '+'*'*10)
        print(user_expense)
        numbers_income = income.count()
        categories_order = [categories.first(), categories.last()]
        data = {
            'categories':categories_order,
            'expenses':expenses[:10],
            'numbers_income':numbers_income,
            'user_income':user_income['amount__sum'],
            'user_expense': user_expense['price__sum'],
            'balance': balance,
            'form': self.form_class(user=user),
            'biggest_expense': expenses.first(),
            'smallest_expense': expenses.last(),
        }
        print('data sent to the template {}'.format(str(data)))
        return render(request, self.template_name, data)

    def form_valid(self, form):
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

    def previous_expenses(self, querySet, days=None):
        if days is None:
            days = 30
        now = timezone.now()-timedelta(days=days)
        previous_expenses = querySet.filter(date__gte=now).aggregate(Sum('price'))
        return previous_expenses['price__sum']
    
    def get_income_requirements(self, user, days=None):
        if days is None:
            days = 30
        query = Income.objects.filter(user=user)
        data = {}
        if query.exists():
            print('*'*10+'Income data'+'*'*10)
            start = timezone.now() - timedelta(days=days)
            data['total_income'] = query.aggregate(Sum('amount'))['amount__sum']
            frequent_income = query.filter(repition=True, circle_repetition__gt=0).order_by('circle_repetition')
            data['most_frequent'] = frequent_income.first()
            data['least_frequent'] = frequent_income.last()
        else:
            data['most_frequent'] = 'No income'
            data['least_frequent'] = 'No income'
            data['total_income'] = 'No income'
        print(data)
        return data

    def get(self, request):
        user = request.user
        balance = CustomUser.objects.get(user=user).current_balance
        last_income = self.get_last_income(user)
        next_income = self.get_next_income(user)
        query = Entry.objects.filter(user=user)
        if query.exists():
            entries = query.order_by('-id')
            last_entry = entries.first()
            date_format =datetime.strftime(last_entry.date, '%B %d, %Y')
            last_entry = '{}|{}|{}'.format(date_format, last_entry.description, last_entry.price)
            total_sum_entries = self.previous_expenses(query)
            order_expensives = query.order_by('price')
            smallest_entry= order_expensives.first()
            biggest_entry = order_expensives.last()
            most_frequent = query.values('description').annotate(count=Count('description')).order_by('-count').first()
            income_data = self.get_income_requirements(user)
        else:
            last_entry = 'No Entry yet'
            total_sum_entries = 0
            biggest_entry = 0
            smallest_entry = 0
            most_frequent = {'description': 'No entries yet',
                            'count': 0
                            }
            income_data = {}
            income_data['most_frequent'] = 'No income'
            income_data['least_frequent'] = 'No income'
            income_data['total_income'] = 'No income'
        data={
            'last_entry':last_entry,
            'balance':balance,
            'last_income': last_income,
            'next_income': next_income,
            'last_expense': last_entry,
            'next_expense': 'TODO',
            'income': Income.objects.filter(user=user)[:10],
            'expense': entries,
            'total_sum_entries': total_sum_entries,
            'biggest_entry': biggest_entry,
            'smallest_entry': smallest_entry,
            'most_frequent': most_frequent,
            'most_frequent_income':income_data['most_frequent'],
            'least_frequent_income': income_data['least_frequent'],
            'total_income': income_data['total_income']
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

class CategoryListView(LoginRequiredMixin, FormView):
    model = Category
    template_name = 'expenses/category.html'
    log_in='user/login'
    success_url = 'expenses/category/add/'
    fields = ('expense', 'circle_repetition', 'name')
    form_class = CategoryForm
    
    def get(self, request):
        user = request.user
        data ={
            'name': user.username
        }
        return render(request, self.template_name, data)

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

class AddCategory(LoginRequiredMixin, View):
    def post(self, request):
        form = CategoryForm(request.POST)
        print(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        else:
            print('It was not possible to store the entry')
        return redirect('/expenses/category/')

class AddEntryAPI(LoginRequiredMixin, View):
    
    def post(self, request):
        form = EntryForm(request.POST, user=request.user)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        else:
            print('It was not possible to store the entry')
        return redirect('/expenses/user/')

class AddIncome(LoginRequiredMixin, CreateView):
    model = Income
    template_name ='income/add.html'
    log_in='user/login'

    def post(self,request):
        form = IncomeForm(request.POST)
        if form.is_valid():
            new_income = form.save(commit=False)
            new_income.user = request.user
            new_income.save()
        return redirect('/expenses/user/')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.current_circle = form.instance.circle_repetition
        return super().form_valid(form)

