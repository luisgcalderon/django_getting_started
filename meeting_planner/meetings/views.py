from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room

# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

# Please add a nre page that shows a list of all room objects
def rooms(request):
    rooms = Room.objects.all()
    return render(request, "meetings/room.html", rooms)