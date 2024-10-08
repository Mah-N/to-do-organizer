from django.urls import path
from . import views

urlpatterns = [
     path('', views.HomePage.as_view(), name='home'),
     path('tasks/', views.TaskListView.as_view(), name='task_list'),  # Add task list view path
     path('tasks/add/', views.TaskCreateView.as_view(), name='task_add'),  # Add task create view path
     path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),  # Add task detail view path
     path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),  # Add task edit view path 
     path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),  # Add task delete view path   
]