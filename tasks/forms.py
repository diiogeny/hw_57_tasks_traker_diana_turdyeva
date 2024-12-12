from django import forms
from .models import Task, Status, Type

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'type']

    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all())  
