from django.contrib import admin
from django.urls import path
from . import views

app_name ="manual"

urlpatterns = [
    path('top/', views.SectionListView.as_view(), name = 'top'),
    path('top/<int:pk>/job', views.JobListView.as_view(), name = 'job_list'),
    path('top/<int:pk>/item', views.ItemListView.as_view(), name = 'item_list'),
    path('top/<int:pk>/method', views.MethodListView.as_view(), name = 'method_list'),
]
