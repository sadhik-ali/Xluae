from django.urls import path

from . import views


app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("football_academy/", views.football_academy, name="football_academy"),
    path("programs/<slug>/", views.programs, name="programs"),
    path("contact", views.contact, name="contact"),
    path("magazine", views.magazine, name="magazine"),
    path("magazine_detail", views.magazine_detail, name="magazine_detail"),
]
