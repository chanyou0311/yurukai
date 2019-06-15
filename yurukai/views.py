from django.shortcuts import render


def index(request):
    return render(request, "yurukai/index.html")


def about(request):
    return render(request, "yurukai/about.html")
