from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import user_profile_form
from .models import user_profile
from django.contrib.auth import get_user_model

# Create your views here.
from django.contrib.auth.models import User


def register(request):
    User = get_user_model()
    user = User.objects.get(username=request.user.username)
    main_user = user_profile(user=user)
    form = user_profile_form(request.POST or None, instance=main_user)
    if request.method == "POST":
        if form.is_valid():
            f = form.save()
            f.save()
            return redirect("/")
    return render(request, "profile_reg.html", {"form": form})


def edit_profile(request):
    User = get_user_model()
    user = User.objects.get(username=request.user.username)
    main_user = get_object_or_404(user_profile, user=user)
    form = user_profile_form(request.POST or None, instance=main_user)
    if request.method == "POST":
        if form.is_valid():
            f = form.save()
            f.save()
        return redirect("/")

    return render(request, "edit_profile.html", {"form": form})
