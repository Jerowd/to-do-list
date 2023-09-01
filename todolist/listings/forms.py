from django import forms
from listings.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
      model = Task
      fields = '__all__'
      exclude = ['finie']
