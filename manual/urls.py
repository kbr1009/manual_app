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

#EditList
    path('edit/', views.EditSectionListView.as_view(), name = 'edit_section_list'),
    path('edit/<str:section_id>/job_list', views.EditJobListView.as_view(), name = 'edit_job_list'),
    path('edit/<int:section_id>/<int:job_id>/item_list', views.EditItemListView.as_view(), name = 'edit_item_list'),
#create
    path('edit/section_create', views.CreateSectionView.as_view(), name = 'section_create'),
    path('edit/<int:section_id>/job_create', views.CreateJobView.as_view(), name = 'job_create'),
    path('edit/<int:section_id>/<int:job_id>/item_create', views.CreateItemView.as_view(), name = 'item_create'),

#update
    path('edit/<int:pk>/section_update', views.UpdateSectionView.as_view(), name = 'section_update'),
    path('edit/<int:pk>/job_update', views.UpdateJobView.as_view(), name = 'job_update'),
]
