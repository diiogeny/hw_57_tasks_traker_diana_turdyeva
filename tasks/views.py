from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from .models import Task
from .forms import TaskForm

class TaskListView(TemplateView):
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

class TaskDetailView(TemplateView):
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

class TaskCreateView(TemplateView):
    template_name = 'tasks/task_form.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.template_name, {'form': form})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def closed_tasks_last_month(request):
    one_month_ago = timezone.now() - timedelta(days=30)
    tasks = Task.objects.filter(updated_at__gte=one_month_ago, status__name='Done')
    if not tasks:
        tasks = []
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def tasks_by_status_and_type(request):
    tasks = Task.objects.filter(
        status__name__in=['New', 'In Progress'],
        type__name__in=['Bug', 'Enhancement']
    )
    if not tasks:
        tasks = []
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def tasks_without_bug(request):
    tasks = Task.objects.filter(~Q(title__icontains='bug'))
    if not tasks:
        tasks = []
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
