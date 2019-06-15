from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.YurukaiDetailView.as_view(), name="detail"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),
    path("reg_s/", views.reg_s, name="reg_s"),
    path("reg_s_conf/", views.reg_s_conf, name="reg_s_conf"),
]
