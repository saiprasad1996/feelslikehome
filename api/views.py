from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from feelslikehome import settings

from api.models import *
from .forms import StoreForm
import json


def showError(message):
    return HttpResponse(json.dumps({"status": "failed", "message": message}))


def index(request):
    return render(request, 'api/index.html')


def docs(request):
    return HttpResponse("Docs page")


# url(r'^stores/(?P<srccountry>[A-Za-z0-9]+)/(?P<destcountry>[A-Za-z0-9]+)/(?P<storename>[A-Za-z0-9]+)$',
#     views.storesWithSrcandDest),

def storesWithSrcandDest(request, srcountry, destcountry, storename):
    src_store = Store.objects.filter(storename=storename, country=srcountry)
    if src_store.exits():
        src_store_category = Store.objects.filter(category=src_store[0].category)[0]

    else:
        return showError("Store does not exist")
    pass


# url(r'^stores/category/(?P<category>[A-Za-z0-9]+)$', views.allStoresByCategory),
def allStoresByCategory(request):
    pass


# url(r'^stores/country/(?P<country>[A-Za-z0-9]+)$', views.allStoresByCountry),
def allStoresByCountry(request):
    pass


# url(r'^stores$', views.allStores),
def allStores(request):
    return HttpResponse("Shows all sotres available in the database api end point")


# url(r'^user/(?P<id>[A-Za-z0-9]+)$', views.user),
def user(request):
    try:
        if request.method == "GET":
            user_id = request.GET["userid"]
            return HttpResponse("User details for the user id : " + user_id)
        elif request.method == "POST":
            return HttpResponse("Update user profile")
        elif request.method == "PUT":
            return HttpResponse("Register a user")
    except MultiValueDictKeyError:
        return HttpResponse("You probably missed out a required parameter")


# url(r'^users', views.allUsers),
def allUsers(request):
    pass


# url(r'^user', views.userHandle),
def userHandle(request):
    pass


# url(r'^store/(?P<id>[A-Za-z0-9]+)', views.storeDetails),
def storeDetails(request):
    pass


# url(r'store', views.storeHandle),
def storeHandle(request):
    pass


def registerStore(request):
    if request.method == "POST":
        form = StoreForm(request.POST, files=request.FILES)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.image = request.FILES['image']
            form.save()
            return redirect('registerstore')
    else:
        form = StoreForm()
    return render(request, 'api/registerstore.html', {'form': form})


def showStores(request):
    if request.method == "GET":
        stores = Store.objects.all()
        return render(request, 'api/stores.html', {'stores': stores})
    else:
        return render(request, 'api/error.html', {'error': "Bad request"})


def error(request,message="Bad Request"):
    return render(request, 'api/error.html', {'error': message})

def deletestore(request,id):
    if request.method == "POST":
        todelete = Store.objects.filter(id=id)
        todelete.delete()
        return redirect('stores')
    else :
        return error(request)