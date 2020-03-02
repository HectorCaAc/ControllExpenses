from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from expenses.models import Category, Income, Entry
# Create your views here.
class Report(View):
    template_name='reports/report.html'

    def get(self, request):
        print('getting the Report for certain user')
        return render(request, self.template_name)
