from django.urls import re_path
from account.views import PersonExpenses

app_name='expenses'
'''
    TODO: add class base views, and add urls to it.
    - add templates, add authentication and authorization
'''
urlpatterns = [
    re_path(r'$', PersonExpenses.as_view(), name='person_expenses')
]
