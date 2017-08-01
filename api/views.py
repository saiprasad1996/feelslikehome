from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#  url(r'^$',views.index),
#     url(r'^store/withsrcdest$',views.storesWithSrcandDest),
#     url(r'^stores$',views.allStores)
#     url(r'^stores/(?P<country>[A-Za-z0-9]+)$',views.storesInaCountry),
#     url(r'^user$',views.user),

def index(request):
    return render('api/index.html')

