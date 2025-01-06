from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, Project
from .forms import TaskForm, ProjectMembersForm
from django.urls import reverse_lazy

class ProjectAccessMixin(UserPassesTestMixin):
    def test_func(self):
        project = self.get_object()
        return self.request.user in project.members.all()

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.select_related('status', 'type', 'project').all()

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        task.is_deleted = True
        task.save()
        return redirect(self.success_url)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'tasks/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)

class ProjectDetailView(ProjectAccessMixin, DetailView):
    model = Project
    template_name = 'tasks/project_detail.html'

class ProjectCreateView(ProjectAccessMixin, LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'tasks/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(ProjectAccessMixin, LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'tasks/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(ProjectAccessMixin, LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'tasks/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

class ProjectMembersUpdateView(UpdateView):
    model = Project
    form_class = ProjectMembersForm
    template_name = 'tasks/project_members_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


