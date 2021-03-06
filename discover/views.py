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
        print(request.session['username'])
        users = signup.objects.exclude(username = request.session['username']).annotate(follow = Count("followers"), follower = Count("following"))
        around = signup.objects.filter(location = signup.objects.get(username = request.session['username']).location).exclude(username = request.session['username']).annotate(follow = Count("followers") , follower = Count("following"))
        print(Followers.objects.all())

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



def unfollowBot(request):
    pass
