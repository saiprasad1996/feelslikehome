
from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$',views.index),
    url(r'^store/withsrcdest$',views.storesWithSrcandDest),
    url(r'^stores$',views.allStores)
    url(r'^stores/(?P<country>[A-Za-z0-9]+)$',views.storesInaCountry),
    url(r'^user$',views.user),
]

'''
"http://collaborizmproject.comli.com/travelsapp/getdata.php?op=withsrcdest&company="+company+"&destcountry="+destination+"&srccountry="+home;
"http://collaborizmproject.comli.com/travelsapp/getdata.php?op=generic&company="+company

'''