from django.urls import re_path
from account import views
app_name='accounts'
'''
    TODO: add class base views, and add urls to it.
    - add templates, add authentication and authorization
'''
urlpatterns = [
    re_path(r'singup', views.CreateUser,name='sign_up'),
    re_path(r'login', views.LogIn,name='log_in'),
    re_path(r'logout',views.LogOut, name="log_out")
]
