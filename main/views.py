from django.shortcuts import render
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from main import (
    forms,
    models
)

def index(request):
    context = {}
    return render(request,'main/index.html',context)

def register(request):
    studentform = forms.Studentform()

    if request.method == "POST":
        studentform = forms.Studentform(request.POST)
        if studentform.is_valid():
            student = studentform.save() 
            messages.success(request,'CONGRATS !! You have been Registered Successfully.')
            return HttpResponseRedirect('/register/')

    context = {
        "studentform": studentform
    }
    return render(request,'main/register.html',context)


def team(request):
    context = {}
    return render(request,'main/team.html',context)


def events(request):
    context = {}
    return render (request,'main/events.html',context)    