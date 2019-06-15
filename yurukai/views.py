from django.shortcuts import render


def index(request):
    return render(request, "yurukai/index.html")

def about(request):
    return render(request, "yurukai/about.html")

def join_s(request):
    return render(request, "yurukai/join_s.html")

def join_t(request):
    return render(request, "yurukai/join_t.html")

def join_s_conf(request):
    return render(request, "yurukai/join_s_conf.html")

def join_t_conf(request):
    return render(request, "yurukai/join_t_conf.html")


def reg_s(request):
    return render(request, "yurukai/reg_s.html")

def reg_t(request):
    return render(request, "yurukai/reg_t.html")

def reg_s_conf(request):
    return render(request, "yurukai/reg_s_conf.html")

def reg_t_conf(request):
    return render(request, "yurukai/reg_t_conf.html")
