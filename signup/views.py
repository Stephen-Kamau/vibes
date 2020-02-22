from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import signup as signmodel

def signup(request):
    existance = ("")
    if request.method =="POST":
        email = request.POST['email']
        username = request.POST['username']
        pnumber = request.POST['pnumber']
        # location = request.POST['location']
        hobby = request.POST['hobby']
        profilepic = request.FILES['profilepic']
        password = request.POST['password']
        try:
            existance = signup.objects.get(email = email)

        except Exception as e:
            pass

        else:
            pass
        if existance:
            error_log = "email already in use, try something else out"

        else:
            signmodel.objects.create(email = email , username = username , pnumber = pnumber ,
            location = "Hello" , hobby = hobby , profilepic = profilepic , password = password)

        return redirect("/login/")
    else:
        return render(request , "signup/signup.html" , context = {"error_log": error_log})
