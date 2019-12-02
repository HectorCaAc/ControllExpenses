from django.urls import re_path
from expenses import api_views

urlpatterns = [
    re_path(r'category/delete/$', api_views.delete_category),
    re_path(r'expenses/delete/$', api_views.delete_entries),
]
