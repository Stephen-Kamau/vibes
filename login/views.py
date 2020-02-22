from django.shortcuts import render , redirect
from django.http import HttpResponse
from signup.models import signup
from django.contrib.auth.hashers import check_password



def login(request):
    if request.method == "POST":
        error_log = list()
        username = request.POST['username']
        password = request.POST['password']

        try:
            userinfo = signup.objects.get(username = username)

        except Exception as e:
            error_log.append(" Wrong credentials")

            return render(request , "login/login.html" , context = {"error_log" : error_log})

        else:
            if check_password(password , userinfo.password):

                # add username to the session
                request.session["username"] = username
                request.session["loginstatus"] = True

                # set the sessions expiry date
                request.session.set_expiry(0)
                # redirect user to home page
                return redirect("/")
            else:
                error_log.append("Wrong credentials")
                return render(request , "login/login.html" , context = {"error_log" : error_log})


    else:
        return render(request , "login/login.html")



def forgotcredetials(request):
    return render(request , "login/forgot.html")



def logout(request):
    # clear the session variables
    request.session.clear()
    request.session.flush()
    request.session["loginstatus"] = False
    return redirect("/")
