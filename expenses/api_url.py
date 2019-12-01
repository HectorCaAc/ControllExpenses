from django.urls import re_path
from expenses import api_views

urlpatterns = [
    re_path(r'delete/$', api_views.delete_category)
]
