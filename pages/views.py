from django.shortcuts import render

# Create your views here.


def about_page(request):
    return render(request, "about.html")


def search_page(request):
    return render(request, "search.html")

