from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'home.html'

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskdetail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')    
