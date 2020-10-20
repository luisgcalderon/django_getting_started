from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This data was sent from the view to the template."})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    msg = "Mi nombre es Luis Calderon, tengo muchos años y soy programador"
    return HttpResponse(msg)