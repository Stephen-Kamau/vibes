from django.shortcuts import render,redirect
from django.http import HttpResponse
from discover.models import Followers
from signup.models import signup
from .models import groups as g,members
from .forms import gform
# Create your views here.


def groups(request):
    try:
        request.session['username']

    except Exception as e:
        return redirect("/login/")

    else:
        users = Followers.objects.filter(follower_id = signup.objects.get(username = request.session['username']).uid)
        for x in  (users):
            print(x.follower.profilepic)

        Group = g.objects.all().annotate()

        return render(request , "groups/group.html" , context = {"users":users , "Group":Group})



def creategroup(request):
    if request.method =="POST":

        try:
            group_name = request.POST['group_name']
            gicon = request.FILES['gicon']
        except Exception as e:
            # print(e)
            return render(request , "groups/add.html" , context = {"form":gform})

        else:

            g.objects.create(group_name = group_name,location = "Nairobi/Kenya", gicon = gicon)
            return redirect("/groups/")
    else:
        return render(request , "groups/add.html" , context = {"form":gform})



def join_group(request , gid):
    try:
        user = signup.objects.get(username = request.session['username']).uid
        print(user)

    except Exception as e:
        print("\n\n\n\n\n\n{}".format(e))
        return redirect("/login/")

    else:
        try:
            gobj = g.objects.get(gid = gid)
            obj = members.objects.create(memberuid_id = user)
            obj.groupid.add(gobj)

        except Exception as e:
            return redirect("/groups/")

        else:
            print("added the user")
            return redirect("/groups/")
