from django.contrib import admin
from django.urls import path
from . import views

app_name ="manual"

urlpatterns = [
    path('top/', views.SectionListView.as_view(), name = 'top'),
    path('top/<int:pk>/job', views.JobListView.as_view(), name = 'job_list'),
    path('top/<int:pk>/item', views.ItemListView.as_view(), name = 'item_list'),
    path('top/<int:pk>/method', views.MethodListView.as_view(), name = 'method_list'),

    path('top/users', views.UserListView.as_view(), name = 'user_list' ),
    path('top/users/<int:pk>', views.UserDetailView.as_view(), name = 'user_detail'),
    path('top/users/<int:pk>/delete', views.UserDeleteView.as_view(), name = 'user_delete'),
    path('top/users/useradd', views.UserCreateView.as_view(), name = 'user_add'),

    path('top/create/', views.CreateSectionListView.as_view(), name = 'create_section_list'),
    path('top/create/createsection', views.CreateSectionView.as_view(), name = 'section_create'),
    path('top/create/<int:pk>/job', views.CreateJobListView.as_view(), name = 'create_job_list'),
    path('top/create/job/createjob', views.CreateJobView.as_view(), name = 'job_create'),
]
