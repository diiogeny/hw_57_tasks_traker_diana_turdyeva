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
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=False, default=1)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
