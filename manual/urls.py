from django.contrib import admin
from django.urls import path
from . import views

app_name ="manual"

urlpatterns = [
#manual
    path('top/', views.SectionListView.as_view(), name = 'top'),
    path('<int:section_id>/job_list', views.JobListView.as_view(), name = 'job_list'),
    path('<int:section_id>/<int:job_id>/item_list', views.ItemListView.as_view(), name = 'item_list'),
    path('<int:section_id>/<int:job_id>/<int:pk>/method_list', views.MethodListView.as_view(), name = 'method_list'),
#auth
    path('top/users', views.UserListView.as_view(), name = 'user_list' ),
    path('top/users/<int:pk>', views.UserDetailView.as_view(), name = 'user_detail'),
    path('top/users/<int:pk>/delete', views.UserDeleteView.as_view(), name = 'user_delete'),
    path('top/users/useradd', views.UserCreateView.as_view(), name = 'user_add'),
#create
    path('top/create/', views.CreateSectionListView.as_view(), name = 'create_section_list'),
    path('top/create/createsection', views.CreateSectionView.as_view(), name = 'section_create'),
    path('top/create/<int:pk>/job', views.CreateJobListView.as_view(), name = 'create_job_list'),
    path('top/create/job/createjob', views.CreateJobView.as_view(), name = 'job_create'),
]
