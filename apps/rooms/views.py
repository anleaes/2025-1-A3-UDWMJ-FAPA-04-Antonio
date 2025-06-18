from django.shortcuts import render, get_object_or_404, redirect
from .forms import RoomForm
from .models import Room

# Create your views here.

def add_room(request):
    template_name = 'rooms/add_room.html'
    context = {}
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.save()
            form.save_m2m()
            return redirect('rooms:list_rooms')
    form = RoomForm()
    context['form'] = form
    return render(request, template_name, context)

def list_rooms(request):
    template_name = 'rooms/list_rooms.html'
    rooms = Room.objects.filter()
    context = {
        'rooms': rooms
    }
    return render(request, template_name, context)

def edit_room(request, id_room):
    template_name = 'rooms/add_room.html'
    context = {}
    room = get_object_or_404(Room, id = id_room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('rooms:list_rooms')
    form = RoomForm(instance = room)
    context['form'] = form
    return render(request, template_name, context)

def delete_room(request, id_room):
    room = Room.objects.get(id = id_room)
    room.delete()
    return redirect('rooms:list_rooms')
