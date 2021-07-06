from django import forms
from .models import Celebrity, Media


class AddCelebrity(forms.Form):
    name = forms.CharField(max_length=30, help_text='enter celebrity name')
    class Meta:
        model = Celebrity
        fields = ['name', 'age']
