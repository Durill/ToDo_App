from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse

from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        else:
            messages.error(request, "Błąd formularza, spróbuj ponownie")
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Zadanie zostało pomyślnie usunięte z Twojej listy zadań!")
    return redirect('todo')


def update_is_done_field(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        item = get_object_or_404(Todo, id=record_id)
        item.is_done = not item.is_done
        item.save()
    return redirect('todo')
