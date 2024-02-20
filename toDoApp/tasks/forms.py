from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Add new task..."})
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Add description here"})
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2, "cols": 40}),
        }
