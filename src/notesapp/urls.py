from django.conf.urls import url
from django.urls import path
from . import views

app_name = "notesapp"
urlpatterns = [
    path("", views.all_notes, name="all_notes"),
    path("<slug>/detail/", views.detail_notes, name="detail_notes")
]
