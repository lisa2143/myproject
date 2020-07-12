from django import forms
from .models import BoardModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = BoardModel
        fields = ['content', 'images']
