from django.shortcuts import render
from django.http import HttpResponse
from signup.models import signup



def login(request):
    error_log = dict({})
    if request.method == "POST":
        try:
            signup.objects.get(username = request.POST['username'])

        except Exception as e:
            error_log = "No user with those credential"

            return render(request , "login/login.html" , context = {"error_log" : error_log})

        else:
            return redirect("/")


    else:
        return render(request , "login/login.html" , context = {"error_log" : error_log})



def forgotcredetials(request):
    return render(request , "login/forgot.html")
