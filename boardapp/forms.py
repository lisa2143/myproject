from django import forms
from .models import SubComment

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = SubComment
        fields = ('text',)
