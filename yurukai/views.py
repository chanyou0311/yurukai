from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Yurukai, User, Entry, Schedule
from .forms import YurukaiForm, EntryForm


class IndexView(ListView):
    model = Yurukai
    template_name = "yurukai/yurukai/list.html"


class YurukaiDetailView(DetailView):
    model = Yurukai
    template_name = "yurukai/yurukai/detail.html"


class YurukaiJoinView(TemplateView):
    template_name = "yurukai/yurukai/join.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        yurukai_instance = Yurukai.objects.get(pk=pk)
        context["dataset"] = []
        schedule_query = Schedule.objects.filter(yurukai=yurukai_instance)
        for schedule_instance in schedule_query:
            form = EntryForm(
                user=self.request.user, schedule_instance=schedule_instance
            )
            context["dataset"].append({"form": form, "schedule": schedule_instance})
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        pk = self.kwargs["pk"]
        yurukai_instance = Yurukai.objects.get(pk=pk)
        schedule_query = Schedule.objects.filter(yurukai=yurukai_instance)
        data = request.POST
        user = request.user
        is_teacher = data.get("is_teacher") == "on"
        for count, schedule_instance in enumerate(schedule_query):
            is_join = data.get(f"is_join_{count}") == "on"
            Entry.objects.create(
                user=user, schedule=schedule_instance, is_join=is_join, is_teacher=is_teacher
            )
        return redirect("yurukai:yurukai_detail", pk=pk)


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
        schedule_query = Schedule.objects.filter(yurukai=yurukai_instance)
        is_teacher = self.request.POST.get("is_teacher") == "on"
        for schedule_instance in schedule_query:
            Entry.objects.create(
                user=user_instance,
                schedule=schedule_instance,
                is_join=True,
                is_teacher=is_teacher,
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
