from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Yurukai, User
from .forms import YurukaiForm


class IndexView(ListView):
    model = Yurukai
    template_name = "yurukai/yurukai/list.html"


class YurukaiDetailView(DetailView):
    model = Yurukai
    template_name = "yurukai/yurukai/detail.html"


class YurukaiCreateView(CreateView):
    model = Yurukai
    template_name = "yurukai/yurukai/create.html"
    form_class = YurukaiForm


class UserDetailView(DetailView):
    model = User
    template_name = "yurukai/users/detail.html"


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
