from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def notifications(request):
    return HttpResponse("Hello notifs")
