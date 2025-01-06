from django.contrib.auth.models import User
from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    members = models.ManyToManyField(User, related_name="projects")

    def __str__(self):
        return self.name

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("Дата окончания проекта не может быть раньше даты начала.")

class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=False, default=1)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = TaskManager()

    def __str__(self):
        return self.title

    def clean(self):
        if len(self.title) < 5:
            raise ValidationError("Заголовок задачи должен содержать не менее 5 символов.")


