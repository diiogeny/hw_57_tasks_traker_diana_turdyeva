from django.urls import path, include
from . import views
from .views import ProjectCreateView, ProjectMembersUpdateView

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),

    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('project/<int:pk>/members/', ProjectMembersUpdateView.as_view(), name='project_members_update'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),

]
