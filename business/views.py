from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import sell_frm
from .models import sell_goods
from signup.models import signup
import smtplib



def business(request):
    dataitems = sell_goods.objects.all()

    try:
        uname = request.session["username"]

    except KeyError as e:
        # KeyError
        return redirect("/login/")

    else:

        form = sell_frm()
        if request.method =='POST':
            Gtitle = request.POST['Gtitle']
            GDescription = request.POST['GDescription']
            Gprice = request.POST['Gprice']
            Gphoto = request.FILES['Gphoto']
            Sid = signup.objects.get(username = uname).uid
            sell_goods.objects.create(Gtitle = Gtitle , GDescription = GDescription , Gprice = Gprice , Gphoto = Gphoto , Sid_id = Sid)
            return render(request , "business/business.html" , context = {"form":form , "dataitems":dataitems})

        else:
            return render(request , "business/business.html" , context = {"form":form , "dataitems":dataitems})







def cart(request):
    try:
        request.session['username']

    except Exception as e:
        return redirect("/")

    else:
        data = request.session['items']
        data.append(request.POST['itemid'])
        request.session['items'] = data
        print(request.session['items'])
        return redirect("/business/")



def viewcart(request):
    print(request.session['items'])
    request.session['items'] = [int(item) for item in request.session['items']]
    carts = []

    for x in request.session['items']:
        id = int(x)
        carts.append(sell_goods.objects.filter(GoodId = id))


    print(carts)

    return render(request , "business/cart.html" , locals())



def orders(request):
    print("hello orders")
    print([int(item) for item in request.session['items']])
    goods = [int(item) for item in request.session['items']]
    try:
        request.session["username"]
    except Exception as e:
        return redirect("/login")

    else:
        sender = "anornymous99@gmail.com"
        receiver = "stiveckamash@gmail.com"
        message = """
                    From: {}
                    To: {}
                    Subject:Hello stephen Your orders was received
                    ---------------------------------------------
        """.format(sender,receiver)
        #selects all item details from the cart items
        for goodid in goods:
            print(goodid)
            goodDetails = sell_goods.objects.filter(GoodId = goodid)

            for goodDetail in goodDetails:
                message +="""
                MIME-Version:1.0
                Content-type:text/html
                Subject: Sending Order Gmail to the orderer
                <h3>{}</h3>
                <h3>{}</h3>
                <h3>{}</h3>
                ........................................
                \n\n
                """.format(goodDetail.Gtitle , goodDetail.GLocation , goodDetail.Gprice)
        try:
            print(message)
            sendobj = smtplib.SMTP('smtp.gmail.com' , 587)
            sendobj.starttls()
            sendobj.login("anornymous99@gmail.com","xcmbyzwvy")

        except Exception as e:
            print("Error  ............{}".format(e))
            return HttpResponse(e)
        else:
            sendobj.sendmail(sender , receiver , message)
            request.session["items"] = ""
            # print("Session: " +str(request.session["items"]))
            print("Message send successfully to the orderer")
            return HttpResponse("Thank you for staying connected")


    # return HttpResponse([int(item) for item in request.session['items']])
