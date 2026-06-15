from django.shortcuts import render
from .models import Room, GalleryImage, Announcement, MenuItem, HistoryEvent
from .forms import ContactForm

from .models import (
    Room, GalleryImage, Announcement, MenuItem,
    HistoryEvent, RoomImage, ContactMessage, HomePageContent
)

def index(request):
    rooms = Room.objects.all()[:3]
    gallery = GalleryImage.objects.all()
    announcements = Announcement.objects.all()[:3]
    mains = MenuItem.objects.filter(category='mains')
    desserts = MenuItem.objects.filter(category='desserts')
    drinks = MenuItem.objects.filter(category='drinks')
    homepage = HomePageContent.objects.first()
    return render(request, 'myapp/index.html', {
        'rooms': rooms,
        'gallery': gallery,
        'announcements': announcements,
        'mains': mains,
        'desserts': desserts,
        'drinks': drinks,
        'homepage': homepage,
    })

def about(request):
    gallery = GalleryImage.objects.all()
    history = HistoryEvent.objects.all()
    return render(request, 'myapp/about.html', {'gallery': gallery, 'history': history})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'myapp/rooms.html', {'rooms': rooms})

def room_detail(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, 'myapp/room_detail.html', {'room': room})