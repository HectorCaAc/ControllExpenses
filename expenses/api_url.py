from django.urls import re_path
from expenses import api_views

urlpatterns = [
    re_path(r'category/delete/$', api_views.delete_category),
    re_path(r'expenses/delete/$', api_views.delete_entries),
    # re_path(r'expenses/add/$', api_views.add_entry) ADD THIS ENTRY WHEN THE REACT IS ADDED TO THE PROGRAM OTHER WISE DO NOT USED THIS
]
