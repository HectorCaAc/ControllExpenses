from django.urls import re_path
from reports import views

app_name='reports'
'''
    TODO: add class base views, and add urls to it.
    - add templates, add authentication and authorization
'''
urlpatterns = [
    re_path(r'', views.Report.as_view(), name='report'),
]
