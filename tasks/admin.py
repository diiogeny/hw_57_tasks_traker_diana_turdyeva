from django.contrib import admin
from .models import Task, Project, Type, Status

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'type', 'project', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('status', 'type', 'is_deleted')
    search_fields = ('title', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'description')
    search_fields = ('name', 'description')


admin.site.register(Type)
admin.site.register(Status)
