from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        "title": "Главная"
    }
    return render(request, 'notes/index.html', context)


@login_required
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'notes/category_list.html', {'categories': categories})


@login_required
def notes_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    notes = Note.objects.filter(category=category, user=request.user).order_by('-created_at')
    return render(request, 'notes/notes_by_category.html', {'category': category, 'notes': notes})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
def note_create(request):
    if request.method == 'POST':
        try:
            form = NoteForm(request.POST)
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            return redirect('note_list')
        except ValueError:
            return render(request, 'notes/note_form.html', {
                "form": NoteForm(),
                "error": "Переданы неверные данные. Попробуйте еще раз"})
    else:
        return render(request, 'notes/note_form.html', {'form': NoteForm()})


@login_required
def note_update(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_update.html', {'form': form})


@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
