from django import forms
from user.models import Closet

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Closet
        fields = ['subject', 'mainphoto']