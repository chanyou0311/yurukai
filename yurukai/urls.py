from django.urls import path

from . import views


app_name = "yurukai"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("yurukai/", views.IndexView.as_view(), name="yurukai_list"),
    path("yurukai/<int:pk>/", views.YurukaiDetailView.as_view(), name="yurukai_detail"),
    path("yurukai/create/", views.YurukaiCreateView.as_view(), name="yurukai_create"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),
    path("reg_s/", views.reg_s, name="reg_s"),
    path("reg_s_conf/", views.reg_s_conf, name="reg_s_conf"),
]
