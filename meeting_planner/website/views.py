from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Meeting Planner website!')

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))