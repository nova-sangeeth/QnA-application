from django.shortcuts import render
from .models import Question, Answer
# from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request, 'index.html')


def home_feed(request):
    current_user = request.user
    questions = Question.objects.filter(points_gt=-2).order_by('-created')
    paginator = Paginator(questions, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html')


def listing(request):
    return render(request, 'list.html', {'page_obj': page_obj})


def test_view(request):
    current_user = request.user

    return render(request, 'test.html', {'username': current_user.username})
