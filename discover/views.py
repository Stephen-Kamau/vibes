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
<<<<<<< HEAD
        # print(request.session['username'])
        # users = Followers.objects.exclude(fid=signup.objects.get(username = request.session['username']).uid , is_following = True).annotate(follow = Count("follower_id"), follower = Count("following"))
        users = signup.objects.exclude(username = request.session['username'] ).annotate(follow = Count("followers"), follower = Count("following"))
        for user in users:
            print(user.follower)
            print("\n\n")
            print(user.following)
        print("\n\n\n\n\n\n")
=======
        print(request.session['username'])
        users = signup.objects.exclude(username = request.session['username']).annotate(follow = Count("followers"), follower = Count("following"))
>>>>>>> upstream/master
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
