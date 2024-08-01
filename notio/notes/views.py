from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Note
from .forms import NoteForm


def index(request):
    return render(request, 'notes/index.html')


def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return HttpResponseRedirect(note.get_absolute_url())
    else:
        form = NoteForm()
    return render(request, 'notes/note_create.html', {'form': form})
