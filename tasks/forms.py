from django import forms
from .models import Task, Status, Type, Project
from django.core.exceptions import ValidationError

def validate_title(value):
    if len(value) < 5:
        raise ValidationError("Заголовок задачи должен содержать не менее 5 символов.")

def validate_description(value):
    if "bug" in value.lower():
        raise ValidationError("Описание не должно содержать слово 'bug'.")

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'type', 'project']

    title = forms.CharField(validators=[validate_title])
    description = forms.CharField(validators=[validate_description])
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all())

class ProjectMembersForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['members']
        widgets = {
            'members': forms.CheckboxSelectMultiple(),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

    def save(self, commit=True):
        project = super().save(commit=False)
        if commit:
            project.save()
            project.members.add(self.instance.user)
        return project
