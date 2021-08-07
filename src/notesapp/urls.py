from django.conf.urls import url
from django.urls import path
from . import views

app_name = "notesapp"
urlpatterns = [
    path("all/", views.all_notes, name="all_notes"),
    path("<id>/detail/", views.detail_notes, name="detail_notes")
]
