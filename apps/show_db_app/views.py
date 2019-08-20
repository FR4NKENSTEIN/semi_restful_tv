from django.shortcuts import render, redirect
from time import strftime
from .models import *

def root(request):
    return redirect('/shows')

def table(request):
    context = {
        'shows_in_db' : Shows.objects.all()
    }
    return render(request, 'show_db_app/table.html', context)#/shows

def new(request):
    return render(request, 'show_db_app/create_form.html')

def details(request, id):
    context = {
        'single_show' : Shows.objects.get(id=id)
    }
    return render(request, 'show_db_app/details.html', context)#/shows/<id>

def edit(request, id):
    context = {
        'this_show' : Shows.objects.get(id=id)
    }
    return render(request, 'show_db_app/edit_form.html', context)

def create(request):
    new_show = Shows.objects.create(
        title = request.POST['title_input'], network = request.POST['network_input'],
        release_date = request.POST['release_date_input'], desc = request.POST['description_input']
    )
    return redirect(f'/shows/{new_show.id}')

def update(request, id):
    editing = Shows.objects.get(id=id)
    editing.title = request.POST['new_title']
    editing.network = request.POST['new_network']
    editing.desc = request.POST['new_description']
    editing.save()
    return redirect(f'/shows/{editing.id}')

def delete(request, id):
    undesired = Shows.objects.get(id=id)
    undesired.delete()
    return redirect('/')
