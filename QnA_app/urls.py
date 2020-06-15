"""QnA_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from questions.views import (
    question,
    new,
    answer,
    myQuestions,
    myAnswers,
    vote,
)
from main.views import home_feed, index, listing, test_view, profile
from pages.views import about_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # path("", include("main.urls")),
    # path("pages/", include("pages.urls")),
    # # path("question/", include("questions.urls")),
    # path("", include("questions.urls")),
    path("", home_feed),
    path("test/", test_view),
    path("profile/", profile),
    path("about/", about_page),
    path("accounts/", include("allauth.urls")),
    path("question/<int:id>/", question),
    path("question/<int:id>/vote", vote),
    path("question/<int:id>/answer", answer),
    path("question/new/", new),
    path("question/my_answers/", myAnswers, name="my-answers"),
    path("question/my_questions/", myQuestions, name="my-questions"),
]
