from django.shortcuts import render
from . import models
# Create your views here.

def all_notes(request):
    all_notes = models.Note.objects.all()
    template_name = "all_notes.html"
    context = {
        "all_notes": all_notes,
    }
    return render(request, template_name, context)

def detail_notes(request, slug):
    detail_notes = models.Note.objects.get(slug=slug)
    template_name = "detail_notes.html"
    context = {
        "detail_notes": detail_notes,
    }
    return render(request,template_name, context)
