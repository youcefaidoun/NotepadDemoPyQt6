from django.conf.urls import url
from django.urls import path
from . import views

app_name = "notesapp"
urlpatterns = [
    path("", views.all, name="all"),
    path("<id>/detail/", views.detail, name="detail"),
    path("add/", views.add, name="add"),
    path("<id>/detail/edit", views.edit, name="edit"),
]
