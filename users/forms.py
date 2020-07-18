from django.forms import ModelForm
from .models import user_profile
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class user_profile_form(ModelForm):
    class Meta:
        model = user_profile
        fields = "__all__"
        exclude = ("user",)
        widgets = {"Date_of_Birth": DateInput()}
