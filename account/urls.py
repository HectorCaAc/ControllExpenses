from django.urls import re_path
from account.views import CreateUser
app_name='accounts'
'''
    TODO: add class base views, and add urls to it.
    - add templates, add authentication and authorization
'''
urlpatterns = [
    re_path(r'', CreateUser.as_view()),
]
