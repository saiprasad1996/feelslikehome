
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from feelslikehome import settings
from django.conf.urls.static import static

from . import choices
from . import views

urlpatterns = [
    
    url(r'^$',views.index),
    url(r'^api/docs',views.docs),
    url(r'^api/stores/(?P<srccountry>[A-Za-z0-9]+)/(?P<destcountry>[A-Za-z0-9]+)/(?P<storename>[A-Za-z0-9]+)$',views.storesWithSrcandDest),
    url(r'^api/stores/category/(?P<category>[A-Za-z0-9]+)$',views.allStoresByCategory),
    url(r'^api/stores/country/(?P<country>[A-Za-z0-9]+)$',views.allStoresByCountry),
    url(r'^api/stores$',views.allStores),
    url(r'^api/user/(?P<id>[A-Za-z0-9]+)$',views.user),
    url(r'^api/users$',views.allUsers),
    url(r'^api/user$',views.userHandle),
    url(r'^api/store/(?P<id>[A-Za-z0-9]+)$',views.storeDetails),
    #Developers urls
    url(r'^dev/initcountries$',choices.initCountries),
    url(r'^dev/countrycount$',choices.getCount),
    #community urls
    url(r'^com/registerstore$',view=views.registerStore,name="registerstore"),
    url(r'^com/regstores$',view=views.showStores,name='stores'),
    url(r'^com/error$',view=views.error,name='error'),
    url(r'^com/deletestore/(?P<id>[A-Za-z0-9]+)$',view=views.deletestore,name='deletestore'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
"http://collaborizmproject.comli.com/travelsapp/getdata.php?op=withsrcdest&company="+company+"&destcountry="+destination+"&srccountry="+home;
"http://collaborizmproject.comli.com/travelsapp/getdata.php?op=generic&company="+company

'''