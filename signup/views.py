from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import signup as signmodel
from django.contrib.auth.hashers import make_password

def signup(request):
    error_log = list()
    if request.method == "POST":
        username = request.POST['username']
        pnumber = request.POST['pnumber']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        hobby = request.POST['hobby']
        profilepic = request.FILES['profilepic']
        location = "Hello"

        try:
            signmodel.objects.get(email = email)
        except Exception as e:
            try:
                signmodel.objects.get(username = username)

            except Exception as e:
                signmodel.objects.create(username = username , pnumber = pnumber , email = email , password = password ,
                hobby = hobby , profilepic = profilepic , location = location)
                return redirect("/login/")

            else:
                error_log.append("User exists")
                print("\n\n\n\n\n{}".format(error_log))
                return render(request , "signup/signup.html" , context = {"error_log":error_log})

        else:
            error_log.append("User exists")
            print("\n\n\n\n\n{}".format(error_log))
            return render(request , "signup/signup.html" , context = {"error_log":error_log})

    else:
        return render(request , "signup/signup.html")
