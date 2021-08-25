from django.shortcuts import render
from . import models, forms
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def all(request):
    all = models.Note.objects.all()
    template_name = "all.html"
    context = {
        "all": all,
    }
    return render(request, template_name, context)

def detail(request, slug):
    detail = models.Note.objects.get(slug=slug)
    template_name = "detail.html"
    context = {
        "detail": detail,
    }
    return render(request,template_name, context)

@csrf_protect
def add(request):

    if request.method == "POST":
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            add_form = form.save(commit=False) # commit = Fales > don't commit or save it in dB now
            add_form.user = request.user
            add_form.save()

    else:
        form = forms.NoteForm()

    template_name = "add.html"
    context = {
        'form': form,
    }
    return render(request,template_name, context)
