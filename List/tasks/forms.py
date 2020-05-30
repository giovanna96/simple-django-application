from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from datetime import date

class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(format = '%m/%d/%Y'), input_formats=('%m/%d/%Y',))
    class Meta:
        model = Task
        fields = ('title', 'description','deadline')

    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
    

        if (deadline < date.today()):
            raise forms.ValidationError("Deadline date cannot be in the past")

        return deadline


