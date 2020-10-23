from django.urls import re_path
from expenses import api_views

urlpatterns = [
    re_path(r'category/delete/$', api_views.delete_category),
    re_path(r'expenses/delete/$', api_views.delete_entries),
    re_path(r'expenses/add/$', api_views.add_entry),
    re_path(r'income/add/$', api_views.add_income),
    re_path(r'category/add/$', api_views.add_category),
    re_path(r'category/(?P<username>\w+)', api_views.categories),
    # re_path(r'category/(?P<username>\w+)/(?P<category_name>\w+)/$', api_views.category_description)
    # re_path(r'expenses/add/$', api_views.add_entry) ADD THIS ENTRY WHEN THE REACT IS ADDED TO THE PROGRAM OTHER WISE DO NOT USED THIS
]
