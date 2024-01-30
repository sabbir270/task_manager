from django.urls import path
from .views import TaskListView, TaskCreateView
from .views import TaskDetailView, TaskUpdateView, TaskDeleteView, TaskConfirmDeleteView
from django.urls import path
from .views import (
    TaskListAPIView,
    TaskRetrieveAPIView,
    TaskCreateAPIView,
    TaskUpdateAPIView,
    TaskDeleteAPIView,
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'), 
    path('<int:pk>/confirm_delete/', TaskConfirmDeleteView.as_view(), name='task_confirm_delete'),

    #API URL
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskDeleteAPIView.as_view(), name='task-delete'), # Add this line
]