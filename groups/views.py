from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def groups(request):
    try:
        request.session['username']

    except Exception as e:
        return redirect("/login/")

    else:
        return render(request , "groups/group.html")
