from django.urls import re_path
from expenses import views

app_name='expenses'
urlpatterns = [
    re_path(r'category/add/$', views.AddCategory.as_view(), name='add_category'), 
    re_path(r'category/$', views.CategoryListView.as_view(), name='category'),
    re_path(r'add/$', views.AddEntryAPI.as_view(), name="add"),
    # re_path(r'add/$', views.AddEntry.as_view(), name="add"),
    # re_path(r'user/(?P<user>\d+)/$', views.PersonData.as_view(), name='person_expenses'),
    re_path(r'user/', views.PersonData.as_view(), name='person_expenses'),
    re_path(r'income/',views.AddIncome.as_view(), name='add_income'),
    re_path(r'report/', views.Summary.as_view(), name='report'),
]
