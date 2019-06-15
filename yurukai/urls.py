from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("join_s/", views.join_s, name="join_s"),
    path("join_t/", views.about, name="join_t"),
    path("join_s_conf/", views.about, name="join_s_conf"),
    path("join_t_conf/", views.about, name="join_t_conf"),

    path("reg_s/", views.about, name="reg_s"),
    path("teg_t/", views.about, name="reg_t"),
    path("reg_s_conf/", views.about, name="reg_s_conf"),
    path("reg_t_conf/", views.about, name="reg_t_conf")

]
