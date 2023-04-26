from django.shortcuts import render
from django.http import HttpResponse
from .models import Sleep

def main(request):
    sleep = Sleep.objects.all()

    return render(request, 'sleepapp/main.html', {'sleep': sleep})