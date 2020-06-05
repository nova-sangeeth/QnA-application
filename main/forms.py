from django import forms
from .models import Question, Answer


class Question_form(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(
        max_length=5000, widget=forms.Textarea, required=False)


class Answer_form(forms.Form):
    text = forms.CharField(maxlenght=2500, widget=forms.Textarea)
