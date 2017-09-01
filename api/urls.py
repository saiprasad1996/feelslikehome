from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from feelslikehome import settings
from django.conf.urls.static import static

from . import choices
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^api/docs', views.docs),
    url(r'^api/stores/(?P<srccountry>[A-Za-z0-9]+)/(?P<destcountry>[A-Za-z0-9]+)/(?P<storename>[A-Za-z0-9]+)$',
        views.storesWithSrcandDest),
    url(r'^api/stores/category/(?P<category>[A-Za-z0-9]+)$', views.allStoresByCategory),
    url(r'^api/stores/country/(?P<country>[A-Za-z0-9]+)$', views.allStoresByCountry),
    url(r'^api/stores$', views.allStores),
    url(r'^api/stores/name/(?P<name>[A-Za-z0-9]+)$', views.storesByName),
    url(r'^api/user/(?P<id>[A-Za-z0-9]+)$', views.user),
    url(r'^api/users$', views.allUsers),
    url(r'^api/store/(?P<id>[A-Za-z0-9]+)$', views.storeDetails),
    # Developers urls
    url(r'^dev/initcountries$', choices.initCountries),
    url(r'^dev/countrycount$', choices.getCount),
    # community urls
    url(r'^user/dashboard', view=views.dashboard, name='dashboard'),
    url(r'^user/login', view=views.login, name='login'),
    url(r'^user/registerstore$', view=views.registerStore, name="registerstore"),
    url(r'^user/regstores$', view=views.showStores, name='stores'),
    url(r'^user/error$', view=views.error, name='error'),
    url(r'^user/profile', view=views.profile, name="profile"),
    url(r'^user/deletestore/(?P<id>[A-Za-z0-9]+)$', view=views.deletestore, name='deletestore'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
"http://collaborizmproject.comli.com/travelsapp/getdata.php?op=withsrcdest&company="+company+"&destcountry="+destination+"&srccountry="+home;
"http://collaborizmproject.comli.com/travelsapp/getdata.php?op=generic&company="+company

'''
