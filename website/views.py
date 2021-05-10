from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    #return HttpResponse("Welcome to Meeting Planner") # at first setting up
    #return  render(request,"website/welcome.html")
   # return render(request, "website/welcome.html", {"message": "This data sent from the view to the template",
    #              "x": 89 , "num_meetings": Meeting.objects.count()})
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})
def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))
def about(request):
    return HttpResponse("For more info contact with using  'github.com/aykutmayali' ")