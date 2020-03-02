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
        users = signup.objects.all().annotate(follow = Count("following"))
        around = signup.objects.filter(location = signup.objects.get(username = request.session['username']).location).annotate(follow = Count("following"))

        return render(request , "discover/discover.html" , context = {"users":users , "around": around})



def followBot(request , fid):
    try:
        uuid = signup.objects.get(username = request.session['username']).uid

    except Exception as e:
        return redirect("/login/")

    else:
        print(fid)
        Followers.objects.create(follower_id = uuid,following_id = fid)
        return redirect("/discover/")
