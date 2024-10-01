from django import forms
from .models.students import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'