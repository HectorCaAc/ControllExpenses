from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class Report(View):
    template_name='reports/report.html'

    def get(self, request):
        print('getting the Report for certain user')
        return render(request, self.template_name)
