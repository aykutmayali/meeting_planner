from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
#from django.forms import modelform_factory
from .forms import MeetingForm
# Create your views here.

def detail(request,id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk =id)
    return render(request,"meetings/detail.html", {"meeting":meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})

#MeetingForm = modelform_factory(Meeting, exclude=[])
# meetingform is a class modelform_factoryhelps create new class called ModelForm
# -->it creates and process html forms, based on Meeting class


def new(request):
    if request.method == "POST":
        # form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        #
        form = MeetingForm()
    return render(request, 'meetings/new.html', {"form":form})