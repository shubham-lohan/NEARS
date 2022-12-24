from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        print(request.POST)
        # do something
    return render(request, "index.html")


def show_details(request):
    return render(request, "show_profile.html")
