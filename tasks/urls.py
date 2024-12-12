from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),  # Главная страница
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),  # Страница детали задачи
    path('create/', views.TaskCreateView.as_view(), name='task_create'),  # Страница для создания задачи
]
