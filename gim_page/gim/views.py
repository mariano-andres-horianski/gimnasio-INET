from multiprocessing import context
from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import GimLesson, GimClient, GimRoom, GimTeacher
from .forms import ClientForm, LessonForm, RoomForm, TeacherForm

def index(request):
    """The home page for the gim page."""
    return render(request, 'gim_page/base.html')

def lessons(request):
    """Show list of available lessons."""
    Lessons = GimLesson.objects.all()
    context = {'gimlessons': Lessons}
    return render(request, 'gim_page/lessons.html', context)

def rooms(request):
    """Show list of rooms, their type, size and location."""
    Rooms = GimRoom.objects.filter()
    context = {'rooms': Rooms}
    return render(request, 'gim_page/rooms.html', context)

def teachers(request):
    """Show list of rooms, their type, size and location."""
    Teachers = GimTeacher.objects.filter()
    context = {'teachers': Teachers}
    return render(request, 'gim_page/teachers.html', context)

#Only the gim staff can see the clients.
@login_required
def clients(request):
    """Show all clients of the gym, only accesible to gym staff."""
    Clients = GimClient.objects.all()
    context = {'clients': Clients}
    return render(request, 'gim_page/clients.html', context)
    
#Only the gim staff can add a new lesson to de database.
@login_required
def new_lesson(request):
    """Insert lesson data"""
    form = LessonForm()
    
    if request.method == 'POST':
        #Post data submitted; process data.
        form = LessonForm(data=request.POST)
        if form.is_valid():
            """Add a new lesson to 'lessons' table."""
            form.save()

        return redirect('gim:lessons')

    context = {'form': form}
    return render(request, 'gim_page/new_lesson.html', context)

@login_required
def new_room(request):
    """Insert room data when a room is built."""
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(data=request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('gim:rooms')

    context = {'form': form}
    return render(request, 'gim_page/new_room.html', context)

@login_required
def new_teacher(request):
    """Insert teacher data."""
    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(data=request.POST)
        if form.is_valid():
            form.save()

        return redirect('gim:teachers')

    context = {'form': form}

    return render(request, 'gim_page/new_teacher.html', context)

@login_required
def new_client(request):
    """Save client data."""
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(data=request.POST)
        if form.is_valid():
            form.save()

        return redirect('gim:clients')

    context = {'form': form}

    return render(request, 'gim_page/new_client.html', context)

@login_required
def edit_lesson(request, lesson_id):
    """Edit a tuple of the lesson table."""
    lesson = GimLesson.objects.get(id=lesson_id)

    if request.method == 'POST':
        form = LessonForm(instance=lesson, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('gim:lessons')
    else:
        #Inicial request, simply show the data to the user
        form = LessonForm(instance=lesson)

    context =  {'gimlesson':lesson, 'form':form}

    return render(request, 'gim_page/edit_lesson.html', context)
    
@login_required
def edit_room(request, room_id):
    """Edit a tuple of the room table."""
    room = GimRoom.objects.get(id=room_id)

    if request.method == 'POST':
        form = RoomForm(instance=room, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('gim:rooms')
    else:
        #Inicial request, simply show the data to the user
        form = RoomForm(instance=room)

    context =  {'gimroom':room, 'form':form}

    return render(request, 'gim_page/edit_room.html', context)

@login_required
def edit_teacher(request, teacher_id):
    """Edit a tuple of the teacher table."""
    teacher = GimTeacher.objects.get(dni=teacher_id)

    if request.method == 'POST':
        form = TeacherForm(instance=teacher, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('gim:teachers')
    else:
        #Inicial request, simply show the data to the user
        form = TeacherForm(instance=teacher)

    context =  {'gimteacher':teacher, 'form':form}

    return render(request, 'gim_page/edit_teacher.html', context)

@login_required
def edit_client(request, client_id):
    """Edit a tuple of the client table."""
    client = GimClient.objects.get(affiliate_number=client_id)

    if request.method == 'POST':
        form = ClientForm(instance=client, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('gim:clients')
    else:
        #Inicial request, simply show the data to the user
        form = ClientForm(instance=client)

    context =  {'gimclient':client, 'form':form}

    return render(request, 'gim_page/edit_client.html', context)