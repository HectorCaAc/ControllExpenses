from django.urls import re_path
from reports import views

app_name='reports'
urlpatterns = [
    re_path(r'', views.Report.as_view(), name='report'),
]
