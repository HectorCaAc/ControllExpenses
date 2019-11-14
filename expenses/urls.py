from django.urls import re_path
from expenses.views import PersonExpenses, CreateCategory

app_name='expenses'
'''
    TODO: add class base views, and add urls to it.
    - add templates, add authentication and authorization
'''
urlpatterns = [
    re_path(r'category$',CreateCategory.as_view()),
    re_path(r'$', PersonExpenses.as_view(), name='person_expenses'),
]
