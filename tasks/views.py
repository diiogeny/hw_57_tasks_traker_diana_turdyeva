from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from .models import Task, Project
from .forms import TaskForm
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

class ProjectListView(ListView):
    model = Project
    template_name = 'tasks/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tasks/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'tasks/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'tasks/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'tasks/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
