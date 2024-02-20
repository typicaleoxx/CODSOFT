from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2, "cols": 40}),
        }
