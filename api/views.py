import json

from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from api.models import *
from api.utils.exception import UnAvailableException
from .backend.security import hashup
from .forms import StoreForm, LoginForm

BASE_URL = 'https://feelslikehome.herokuapp.com'


def showError(message):
    response = HttpResponse(json.dumps({"status": "failed", "message": message}))
    response['Content-Type'] = 'application/json'
    return response


def json_response(obj):
    '''

    :param obj: Dictionary
    :return:    HttpResponse
    '''
    response = HttpResponse(json.dumps(obj))
    response['Content-Type'] = 'application/json'
    return response


def index(request):
    return render(request, 'api/index.html')


def docs(request):
    try:
        return showError('Docs Not yet defined')
    except KeyError:
        return showError('Failed to open docs')


# url(r'^stores/(?P<srccountry>[A-Za-z0-9]+)/(?P<destcountry>[A-Za-z0-9]+)/(?P<storename>[A-Za-z0-9]+)$',
#     views.storesWithSrcandDest),

def storesWithSrcandDest(request, srcountry, destcountry, storename):
    # TODO 1 -Get the categories of the store with source country requested
    src_store = Store.objects.filter(name__icontains=storename, country=srcountry)
    if src_store.exists():
        categories = src_store[0].categories.split(',')
        categories = [c.strip() for c in categories]
        stores_list = []
        # TODO 2 -Get the stores available in the destination country
        stores_dest = Store.objects.filter(country=destcountry)
        if not stores_dest.exists():
            return showError('No stores are available in the given destination country')
        for store in stores_dest:
            cat = store.categories.split(',')
            cat = [c.strip() for c in cat]
            for c in categories:
                if c in cat:
                    stores_list.append(
                        {"id": store.id, "name": store.name, "country": store.country.name, "address": store.address})
                    break
        return json_response(stores_list)
    else:
        return showError("Store does not exist")
    pass


#    url(r'^api/stores/name/(?P<name>[A-Za-z0-9]+)$',views.storesByName),
def storesByName(request, name):
    try:
        if request.method == 'GET':
            stores = Store.objects.filter(name__icontains=name)
            if not stores.exists():
                raise UnAvailableException
            storelist = []
            for s in stores:
                storelist.append(
                    {"id": s.id, "name": s.name, "country": s.country.name, "address": s.address})
            response = {"status": "success", "stores": storelist}
            return json_response(response)
        else:
            return showError("Bad request")
    except UnAvailableException:
        return showError('No store available with the name')


# url(r'^stores/category/(?P<category>[A-Za-z0-9]+)$', views.allStoresByCategory),

def allStoresByCategory(request, category):
    try:
        stores = Store.objects.all()
        storelist = []
        for s in stores:
            categories = s.categories
            categories = categories.split(',')
            categories = [c.strip() for c in categories]
            if any(category in s for s in categories):
                id = s.id
                name = s.name
                storelist.append(
                    {"id": id, "name": name, "country": s.country.name, "address": s.address, "categories": categories})
            if len(storelist) == 0:
                raise UnAvailableException
        return json_response({"stores": storelist, "status": "success"})
    except KeyError:
        return showError("You have missed some required parameters")
    except UnAvailableException:
        return showError("Your query does not match any category")


# url(r'^stores/country/(?P<country>[A-Za-z0-9]+)$', views.allStoresByCountry),
def allStoresByCountry(request, country):
    try:
        country = Country.objects.filter(code=country.upper())[0]
        stores = Store.objects.all()
        storelist = []
        for s in stores:
            if s.country.code == country.code:
                id = s.id
                name = s.name
                storelist.append({"id": id, "name": name, "country": s.country.name, "address": s.address})
        return json_response({"stores": storelist, "status": "success"})
    except KeyError:
        return showError("You have missed some required parameters")
    except IndexError:
        return showError("Sorry the country code you entered is either unavailable to wrong")


# url(r'^stores$', views.allStores),
def allStores(request):
    try:
        stores = Store.objects.all()
        storelist = []
        for s in stores:
            storelist.append({"id": s.id, "name": s.name, "country": s.country.name, "address": s.address})
        response = json.dumps({"stores": storelist, "status": "success"})
        return HttpResponse(response)
    except KeyError:
        return HttpResponse(json.dumps({"status": "failed", "message": "You have missed some required parameters"}))


# url(r'^user/(?P<id>[A-Za-z0-9]+)$', views.user),
def user(request, id):
    try:
        if request.method == "GET":
            user_id = request.GET["userid"]
            return HttpResponse("User details for the user id : " + user_id)
        elif request.method == "POST":
            body = request.body.decode('utf-8')
            body = json.loads(body)
            user = User.objects.filter(email=body["email"])
            if user.exists():
                user.update(phone=body["phone"], profile=body["profile"])

            user.save()

        elif request.method == "PUT" and id == 'new':
            body = request.body.decode('utf-8')
            body = json.loads(body)
            user = User(name=body["name"], email=body["email"], profile=body["profile"], accesstoken=body["atoken"],
                        country=body["country"])
            user.save(force_insert=True)
            return HttpResponse(json.dumps({"status": "success", "message": "User registered successfully"}))
        else:
            return showError('Bad request')
    except IntegrityError:
        return showError("User with same email already exists")
    except KeyError:
        return showError("You probably missed out some parameters")


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
                return showError('Un-authorized request')
    except KeyError:
        return showError("Un-authorized request")


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


def registerStore(request):
    if request.method == "POST" and request.session.has_key('username'):
        username = request.session["username"]
        form = StoreForm(request.POST, files=request.FILES)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.image = request.FILES['image']
            form.save()
            return redirect('registerstore')
        return render(request, 'api/registerstore.html', {'form': form, 'username': username})
    elif request.method == "GET" and request.session.has_key('username'):
        form = StoreForm()
        username = request.session["username"]
        return render(request, 'api/registerstore.html', {'form': form, 'username': username})
    else:
        return HttpResponseRedirect('login')
    return render(request, 'api/error.html', {'error': "Please login to continue"})


def dashboard(request):
    return render(request, 'api/dashboard.html', {"username": "Sai Prasad"})


def login(request):
    if request.session.has_key('username'):
        return HttpResponseRedirect('dashboard')
    if request.method == "POST":

        user = request.POST['email']
        password = request.POST['password']
        admin = AdminUser.objects.filter(email=user, password=hashup(password))
        if admin.exists():
            request.session['username'] = user
            return HttpResponseRedirect('dashboard')
        else:
            form = LoginForm()
    else:
        form = LoginForm()

    return render(request, 'api/login.html', {'form': form})


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

def profile(request):
    if request.method == "POST" and request.session.has_key('username'):
        username = request.session['username']
        user = request.POST["email"]
        password = request.POST["password"]
        update = AdminUser.objects.filter(email=user).update(password=hashup(password))
        if update == 1:
            return redirect('profile')
        else:
            return render(request, 'api/profile.html', {'message': "Oops! Something went wrong"})
    elif request.method == "GET" and request.session.has_key('username'):
        username = request.session['username']
        admin = AdminUser.objects.filter(email=username)[0]
        return render(request, 'api/profile.html', {"name": admin.name, "email": admin.email})
    else:
        return redirect('login')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('login')
