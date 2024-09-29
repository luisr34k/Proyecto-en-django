from django.forms import ModelForm
from .models import Task, Pais
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        
class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }