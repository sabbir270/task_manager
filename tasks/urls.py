from django.urls import path
from .views import TaskListView, TaskCreateView
from .views import TaskDetailView, TaskUpdateView, TaskDeleteView, TaskConfirmDeleteView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'), 
    path('<int:pk>/confirm_delete/', TaskConfirmDeleteView.as_view(), name='task_confirm_delete'), # Add this line
]