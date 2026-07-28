from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomeView, name="home"),
    path("index/",views.IndexView, name="index"),
    path("profile/", views.ProfileView, name="profile"),
]