from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("about/", views.about, name="about"),
    path("join_s/", views.join_s, name="join_s"),
    # path("join_t/", views.join_t, name="join_t"),
    path("join_s_conf/", views.join_s_conf, name="join_s_conf"),
    # path("join_t_conf/", views.join_t_conf, name="join_t_conf"),
    path("reg_s/", views.reg_s, name="reg_s"),
    # path("teg_t/", views.reg_t, name="reg_t"),
    path("reg_s_conf/", views.reg_s_conf, name="reg_s_conf")
    # path("reg_t_conf/", views.reg_t_conf, name="reg_t_conf")
]
