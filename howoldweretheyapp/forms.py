from django import forms
from .models import Celebrity, Media


class AddCelebrity(forms.ModelForm):
    class Meta:
        model = Celebrity
        fields = ['name', 'age']
