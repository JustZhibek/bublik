from django import forms
from . import models

class LostForm(forms.ModelForm):

    class Meta:
        model = models.Lost
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.RatingLost
        fields = '__all__'