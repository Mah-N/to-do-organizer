from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import AccessMixin

class CustomLoginRequiredMixin(LoginRequiredMixin, AccessMixin):
    """ Custom mixin to add a message when user is not logged in. """

    def handle_no_permission(self):
        messages.error(self.request, "You are not logged in. Please log in to continue.")
        return redirect('account_login')



class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('task_list')  # Redirect to task list if user is authenticated
        return super().get(request, *args, **kwargs)

# Create your views here.
class TaskListView(CustomLoginRequiredMixin, ListView):
    
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Filter tasks to only include those created by the logged-in user
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(CustomLoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)

class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    
    model = Task
    template_name = 'taskdetail.html'
    context_object_name = 'task'

class TaskUpdateView(CustomLoginRequiredMixin, UpdateView):
    
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)

class TaskDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
    success_message = "Task deleted successfully!"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response