from django.views.generic import ListView
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import TaskCreationForm
from django.views.generic import DetailView

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreationForm 
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreationForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html' 
    success_url = reverse_lazy('tasks:task_list')
class TaskConfirmDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')
