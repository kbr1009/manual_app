from django.contrib import admin
from django.urls import path
from . import views

app_name ="manual"

urlpatterns = [
<<<<<<< HEAD
    path('top/', views.SectionListView.as_view(), name = 'top'),
=======
    path('top/',views.TopView.as_view(),name = 'top'),
    path('top/section', views.SectionListView.as_view(), name = 'section_list'),
>>>>>>> de25bed57219ea1c03c93357c020314a79647dd0
    path('top/<int:pk>/job', views.JobListView.as_view(), name = 'job_list'),
    path('top/<int:pk>/item', views.ItemListView.as_view(), name = 'item_list'),
    path('top/<int:pk>/method', views.MethodListView.as_view(), name = 'method_list'),
]
