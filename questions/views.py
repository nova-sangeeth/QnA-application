from django.shortcuts import (
    render,
    HttpResponseRedirect,
    get_object_or_404,
)
from django.http import (
    HttpResponseBadRequest,
    JsonResponse,
    HttpResponse,
)
from django.urls import reverse
from main.models import Question, Answer
from main.forms import Question_form, Answer_form
from main.serializers import QuestionSerializer, AnswerSerializer


# vote_type could be 'upvote', 'downvote', or 'cancel_vote'
def updateVote(user, target, vote_type, question_or_answer):
    if question_or_answer == "question":
        upvoted_targets = user.upvoted_questions
        downvoted_targets = user.downvoted_questions
    else:
        upvoted_targets = user.upvoted_answers
        downvoted_targets = user.downvoted_answers

    upvoted_targets.remove(target)
    downvoted_targets.remove(target)

    # if this is an upvote, add an upvote. otherwise, add a downvote.
    if vote_type == "upvote":
        upvoted_targets.add(target)
    elif vote_type == "downvote":
        downvoted_targets.add(target)

    target.update_points()
    return target.points


def answerVoteView(request, id):
    return voteView(request, id, "answer")


def questionVoteView(request, id):
    return voteView(request, id, "question")


def voteView(request, id, question_or_answer):
    current_user = request.user
    if question_or_answer == "question":
        target = Question.objects.get(pk=id)
    else:
        target = Answer.objects.get(pk=id)

    if not current_user.is_authenticated:
        return HttpResponse("Not logged in", status=401)
    if current_user.id == target.user_id:
        return HttpResponseBadRequest("Same user")
    if request.method != "POST":
        return HttpResponseBadRequest("The request is not POST")
    vote_type = request.POST.get("vote_type")
    points = updateVote(current_user, target, vote_type, question_or_answer)
    if question_or_answer == "answer":
        target.user.update_points()
    return JsonResponse({"vote_type": vote_type, "points": points})


def questionView(request, id):
    current_user = request.user
    question = Question.objects.get(pk=id)
    answers = Answer.objects.filter(question_id=id).order_by("created")
    answers_serialized = AnswerSerializer(answers, many=True).data
    for answer in answers_serialized:
        answer["upvoted"] = False
        answer["downvoted"] = False
        if not current_user.is_authenticated:
            pass
        elif current_user.upvoted_answers.filter(id=answer["id"]).count() > 0:
            answer["upvoted"] = True
        elif current_user.downvoted_answers.filter(id=answer["id"]).count() > 0:
            answer["downvoted"] = True

    # For the question
    upvoted = False
    downvoted = False
    asked_by_user = False

    if not current_user.is_authenticated:
        pass
    elif current_user.upvoted_questions.filter(id=question.id).count() > 0:
        upvoted = True
    elif current_user.downvoted_questions.filter(id=question.id).count() > 0:
        downvoted = True
    elif current_user.id == question.user_id:
        asked_by_user = True

    context = {
        "question": question,
        "answers": answers,
        "current_user": current_user,
        "points": question.points,
        "upvoted": upvoted,
        "downvoted": downvoted,
        "asked_by_user": asked_by_user,
        "upvoted": upvoted,
        "downvoted": downvoted,
        "answers_serialized": answers_serialized,
    }
    return render(request, "question.html", context)


def newView(request):
    current_user = request.user

    if not current_user.is_authenticated:
        return HttpResponseRedirect(reverse("account_signup"))

    if request.method != "POST":
        render(request, "new.html", {"current_user": current_user})

    form = Question_form(request.POST)
    if not form.is_valid() or current_user.points < 0:
        return render(request, "new.html", {"current_user": current_user})

    q = Question(
        user_id=current_user.id,
        title=form.cleaned_data["title"],
        body=form.cleaned_data["body"],
    )
    q.save()
    return HttpResponseRedirect("/")


def answerView(request, id):
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


def myAnswers(request):
    current_user = request.user
    answers = Answer.objects.filter(user_id=current_user.id).order_by("-created")
    answers_exist = len(answers) > 0
    return render(
        request,
        "my_answer.html",
        {
            "current_user": current_user,
            "answers_exist": answers_exist,
            "answers": answers,
        },
    )


def myQuestions(request):
    current_user = request.user
    questions = Question.objects.filter(user_id=current_user.id).order_by("-created")
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
