from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:place>", views.general, name="general"),
]
