from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from signup.models import signup
from django.db.models import Count
from .models import Followers


def discover(request):

    users = signup.objects.filter(location = "Nairobi/Kenya").annotate(Count("Followers__follower"))

    return render(request , "discover/discover.html" , context = {"users":users})
