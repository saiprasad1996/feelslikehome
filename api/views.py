from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.db.utils import IntegrityError
from feelslikehome import settings

from api.models import *
from .forms import StoreForm
import json

BASE_URL = 'https://feelslikehome.herokuapp.com'


def showError(message):
    return HttpResponse(json.dumps({"status": "failed", "message": message}))


def index(request):
    return render(request, 'api/index.html')


def docs(request):
    try:
        pass
    except KeyError:
        return HttpResponse(json.dumps())
    return HttpResponse("Docs page")


# url(r'^stores/(?P<srccountry>[A-Za-z0-9]+)/(?P<destcountry>[A-Za-z0-9]+)/(?P<storename>[A-Za-z0-9]+)$',
#     views.storesWithSrcandDest),

def storesWithSrcandDest(request, srcountry, destcountry, storename):
    src_store = Store.objects.filter(storename__icontains=storename, country=srcountry)
    if src_store.exits():
        src_store_category = Store.objects.filter(category=src_store[0].category)[0]
        stores = []



    else:
        return showError("Store does not exist")
    pass


# url(r'^stores/category/(?P<category>[A-Za-z0-9]+)$', views.allStoresByCategory),
def allStoresByCategory(request):
    try:
        pass
    except KeyError:
        return HttpResponse(json.dumps())
    pass


# url(r'^stores/country/(?P<country>[A-Za-z0-9]+)$', views.allStoresByCountry),
def allStoresByCountry(request):
    try:
        pass
    except KeyError:
        return HttpResponse(json.dumps())
    pass


# url(r'^stores$', views.allStores),
def allStores(request):
    try:
        pass
    except KeyError:
        return HttpResponse(json.dumps())
    return HttpResponse("Shows all sotres available in the database api end point")


# url(r'^user/(?P<id>[A-Za-z0-9]+)$', views.user),
def user(request,id):
    try:
        if request.method == "GET":
            user_id = request.GET["userid"]
            return HttpResponse("User details for the user id : " + user_id)
        elif request.method == "POST":
            body = request.body.decode('utf-8')
            body = json.loads(body)
            user = User.objects.filter(email=body["email"])
            if user.exists():
                user.update(phone = body["phone"],profile = body["profile"])


            user.save()

        elif request.method == "PUT" and id == 'new':
            body = request.body.decode('utf-8')
            body = json.loads(body)
            user = User(name=body["name"], email=body["email"], profile=body["profile"], accesstoken=body["atoken"],
                 country=body["country"])
            user.save(force_insert=True)
            return HttpResponse(json.dumps({"status":"success","message":"User registered successfully"}))
        else :
            return HttpResponse(json.dumps({"status":'failed','message':'Bad request'}))
    except IntegrityError:
        return HttpResponse(json.dumps({"status":"failed","message":"User with same email already exists"}))
    except KeyError:
        return HttpResponse(json.dumps({'status':"failed","message":"You probably missed out some parameters"}))


# url(r'^users', views.allUsers),
def allUsers(request):
    try:
        if request.method == "GET":
            access_token = request.META["HTTP_AUTHORIZATION"]
            if access_token == "feelslikehometoken":
                users = User.objects.all()
                users_selected = []
                for u in users:
                    uu = {"name": u["name"], "country": u["country"]}
                    users_selected.append(uu)
                return HttpResponse(json.dumps(users_selected))
            else:
                return HttpResponse(json.dumps({'status':'failed','message':'Un-authorized request'}))
    except KeyError:
        return HttpResponse(json.dumps({"status": "failed", "message": "Un-authorized request"}))


# url(r'^user', views.userHandle),
def userHandle(request):
    try:
        pass
    except KeyError:
        return HttpResponse(json.dumps())
    pass


# url(r'^store/(?P<id>[A-Za-z0-9]+)', views.storeDetails),
def storeDetails(request, id):
    try:
        store = Store.objects.filter(id=id)
        if store.exists():
            store = store[0]
            categories = store.categories.split(',')
            response = {
                "name": store.name,
                "description": store.description,
                "image": BASE_URL + store.image.url,
                "address": store.address,
                "location": {"latitude": store.latitude,
                             "longitude": store.longitude},
                "country": store.country.name,
                "categories": categories
            }
            return HttpResponse(json.dumps({"status": "success",
                                            "response": response}))

    except KeyError:
        return HttpResponse(json.dumps({"status": 'failed', "message": "Dict. key Error"}))
    pass


# url(r'store', views.storeHandle),
def storeHandle(request):
    try:
        pass
    except KeyError:
        return HttpResponse(json.dumps())
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


def error(request, message="Bad Request"):
    return render(request, 'api/error.html', {'error': message})


def deletestore(request, id):
    if request.method == "POST":
        todelete = Store.objects.filter(id=id)
        todelete.delete()
        return redirect('stores')
    else:
        return error(request)
