from django.shortcuts import render, redirect
from . import models, forms
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.

def all(request):
    all = models.Note.objects.all()
    template_name = "all.html"
    context = {
        "all": all,
    }
    return render(request, template_name, context)

def detail(request, id):
    detail = models.Note.objects.get(id=id)
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
            new_form = form.save(commit=False) # commit = Fales > don't commit or save it in dB now
            new_form.user = request.user
            new_form.save()
        return redirect('/notes')

    else:
        form = forms.NoteForm()
    template_name = "add.html"
    context = {'form': form,}
    return render(request,template_name, context)


@csrf_protect
def edit(request, id):
    note = get_object_or_404(models.Note, id=id)
    if request.method == "POST":
        form = forms.NoteForm(request.POST, instance = note)
        form.save()
        return redirect('/notes')
    else:
        form = forms.NoteForm(instance = note)
    template_name = 'edit.html'
    context = {'form': form,}
    return render(request, template_name, context)
