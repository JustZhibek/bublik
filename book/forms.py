from django import forms
from . import models

class LostForm(forms.ModelForm):

    class Meta:
        model = models.book
        fields = '__all__'