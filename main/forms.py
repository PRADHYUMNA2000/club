from django import forms
from main import models

class Studentform(forms.ModelForm):
    class Meta:
        model = models.addstudent
        fields = '__all__'
