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
from main.views import homeFeedView, testView

# from pages.views import aboutPageView, searchView
from questions.views import (
    questionView,
    newView,
    answerView,
    myQuestionsView,
    myAnswersView,
    questionVoteView,
    answerVoteView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeFeedView),
    path("test/", testView),
    # path("leaderboard/", leaderboardView),
    # path("search/", searchView, name="search"),
    # path("about/", aboutPageView),
    path("accounts/", include("allauth.urls")),
    path("question/<int:id>/", questionView),
    path("question/<int:id>/vote", questionVoteView),
    path("answer/<int:id>/vote", answerVoteView),
    path("question/<int:id>/answer", answerView),
    path("question/new/", newView),
    path("question/my_answers/", myAnswersView, name="my-answers"),
    path("question/my_questions/", myQuestionsView, name="my-questions"),
]

