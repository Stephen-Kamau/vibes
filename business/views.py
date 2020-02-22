from django.shortcuts import render
from django.http import HttpResponse
from .forms import sell_frm



def business(request):
    form = sell_frm()
    if request.method =='POST':
        return render(request , "business/business.html" , context = {"form":form})

    else:
        return render(request , "business/business.html" , context = {"form":form})
