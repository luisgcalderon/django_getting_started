from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory

from .models import Meeting, Room

# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

# Please add a nre page that shows a list of all room objects
# Just text, no links)

# Create a:
# - view
# - template
# - url mapping

def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms_list.html", {"rooms":rooms})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, 'meetings/new.html', {"form":form})