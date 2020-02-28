from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from signup.models import signup
from django.db.models import Count
from .models import Followers


def discover(request):

    try:
        request.session['username']

    except KeyError as e:
        return redirect("/login/")

    else:
        users = signup.objects.all()
        around = signup.objects.filter(location = signup.objects.get(username = request.session['username']).location)

        return render(request , "discover/discover.html" , context = {"users":users , "around": around})
