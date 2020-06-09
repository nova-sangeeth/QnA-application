from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from main.models import Question, Answer
from main.forms import Question_form, Answer_form

# updating a vote when given.
# added upvote and downvote funcs.


def update_vote(user, question, vote_type):
    user.upvoted_questions.remove(question)
    user.downvoted_questions.remove(question)
    # figure out the vote is a 'up or down vote'
    if vote_type == "upvote":
        user.upvoted_question.add(question)
    elif vote_type == "downvote":
        user.downvoted_question.add(question)
    question.update_points()


def vote(request, id):
    current_user = request.user
    question = Question.objects.get(pk=id)
    if not current_user.is_authenticated:
        return HttpResponseRedirect(reverse("account_signup"))
    if current_user.id == question.user_id:
        return HttpResponseRedirect(f"/question/{id}")
    if request.method != "POST":
        return HttpResponseRedirect(f"/question/{id}")
    vote_type = request.POST.get("vote_type")
    update_vote(current_user, question, vote_type)
    return HttpResponseRedirect(f"/question/{id}")


def question(request, id):
    current_user = request.user
    question = Question.objects.get(pk=id)
    answers = Answer.objects.filter(question_id=id).order_by("created")
    upvoted = None
    downvoted = None
    asked_by_user = False

    if not current_user.is_authenticated:
        pass
    elif current_user.upvoted_questions.filter(id=question.id).count() > 0:
        upvoted = "done"
    elif current_user.downvoted_questions.filter(id=question.id).count() > 0:
        downvoted = "done"
    elif current_user.id == question.user_id:
        asked_by_user = True

    return render(
        request,
        "question.html",
        {
            "question": question,
            "answers": answers,
            "current_user": current_user,
            "upvoted": upvoted,
            "downvoted": downvoted,
            "asked_by_user": asked_by_user,
        },
    )


def new(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return HttpResponseRedirect(reverse("account_signup"))

    if request.method != "POST":
        render(request, "new.html", {"current_user": current_user})

    form = Question_form(request.POST)
    if not form.is_valid():
        return render(request, "new.html", {"current_user": current_user})

    q = Question(
        user_id=current_user.id,
        title=form.cleaned_data["title"],
        body=form.cleaned_data["body"],
    )

    q.save()
    return HttpResponseRedirect("/")


def answer(request, id):
    current_user = request.user
    if not current_user.is_authenticated:
        return HttpResponseRedirect("/accounts/login")
    if not request.method == "POST":
        return HttpResponseRedirect(f"/question/{id}")
    form = Answer_form(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect(f"/question/{id}")

    a = Answer(user_id=current_user.id, question_id=id, text=form.cleaned_data["text"])
    a.save()
    return HttpResponseRedirect(f"/question/{id}")


def my_answer(request):
    current_user = request.user
    answers = Answer.objects.filter(user_id=current_user.id).order_by("-created")
    answers_exist = len(answers) > 0
    return render(
        request,
        "my_answer.html",
        {
            "current_user": current_user,
            "answers": answers,
            "answers_exists": answers_exist,
        },
    )


def my_question(request):
    current_user = request.user
    questions = Question.objects.filter(user_id=current_user).order_by("-created")
    questions_exist = len(questions) > 0
    return render(
        request,
        "my_question.html",
        {
            "current_user": current_user,
            "questions": questions,
            "questions_exist": questions_exist,
        },
    )
