from django import forms
from .models import Task, Status, Type
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
        fields = ['title', 'description', 'status', 'type']

    title = forms.CharField(validators=[validate_title])
    description = forms.CharField(validators=[validate_description])
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all())
