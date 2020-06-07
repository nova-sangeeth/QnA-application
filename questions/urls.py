from django.conf.urls import url
from .views import question, answer, my_question, my_answer, new, update_vote, vote, new


urlpatterns = [
    url(r"^new$", new, name="new"),
    url(r"^my_question$", my_question, name="my_question"),
    url(r"^my_answer$", my_answer, name="my_answer"),
    url(r"^question/(?P<pk>\d+)$", question, name="question"),
    url(r"^answer/(?P<pk>\d+)$", answer, name="answer"),
    url(r"^vote/(?P<pk>\d+)$", vote, name="vote"),
    url(r"^update_vote$", update_vote, name="update_vote"),
]
