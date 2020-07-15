from django.forms import ModelForm
from .models import user_profile


class user_profile_form(ModelForm):
    class Meta:
        model = user_profile
        fields = "__all__"
        exclude = ("user",)
