from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
#  url(r'^$',views.index),
#     url(r'^store/withsrcdest$',views.storesWithSrcandDest),
#     url(r'^stores$',views.allStores)
#     url(r'^stores/(?P<country>[A-Za-z0-9]+)$',views.storesInaCountry),
#     url(r'^user$',views.user),

def index(request):
    return render(request,'api/index.html')

def storesWithSrcandDest(request):
    return HttpResponse("Stores with source and destination api end point")

def allStores(request):
    return HttpResponse("Shows all sotres available in the database api end point")

def storesInaCountry(request):
    return HttpResponse("List of stores in the country")

def user(request):
    try:
        if request.method == "GET":
            user_id = request.GET["userid"]
            return HttpResponse("User details for the user id : "+user_id)
        elif request.method == "POST":
            return HttpResponse("Update user profile")
        elif request.method == "PUT":
            return HttpResponse("Register a user")
    except MultiValueDictKeyError:
        return HttpResponse("You probably missed out a required parameter")
