from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def index(request):
    return render(request,'api/index.html')

def docs(request):
    return HttpResponse("Docs page")
# url(r'^stores/(?P<srccountry>[A-Za-z0-9]+)/(?P<destcountry>[A-Za-z0-9]+)/(?P<storename>[A-Za-z0-9]+)$',
#     views.storesWithSrcandDest),

def storesWithSrcandDest(request):
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
            return HttpResponse("User details for the user id : "+user_id)
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



