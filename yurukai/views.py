from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Yurukai, User, Entry, Schedule
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

    def form_valid(self, form):
        redirect_url = super(YurukaiCreateView, self).form_valid(form)
        if self.request.user.is_authenticated:
            user_instance = self.request.user
        else:
            user_name = form.cleaned_data["user_name"]
            user_instance = User.objects.create(username=user_name)
        yurukai_instance = Yurukai.objects.last()
        print(yurukai_instance)
        schedule_query = Schedule.objects.filter(yurukai=yurukai_instance)
        print(schedule_query)
        for schedule_instance in schedule_query:
            Entry.objects.create(
                user=user_instance,
                schedule=schedule_instance,
                is_join=True,
                is_teacher=False,
            )
        return redirect_url

    def get_form_kwargs(self):
        kwargs = super(YurukaiCreateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


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
