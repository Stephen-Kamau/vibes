from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def messaging(request):
    # return HttpResponse("Hello messages")
    return render(request , "messages/messages.html" ,)
