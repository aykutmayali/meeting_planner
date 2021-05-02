from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to Meeting Planner")
def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))
def about(request):
    return HttpResponse("For more info contact with using  'github.com/aykutmayali' ")