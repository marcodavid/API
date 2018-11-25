

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [

    url(r'^api/', include('ClientsApp.urlClients',namespace='clients')),
    url(r'^api/', include('CarsApp.urlCars', namespace='cars')),
    url(r'^api/', include('RentersApp.urlRenters', namespace='renter')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [

    url(r'^api/', include('rest_framework.urls',namespace='rest_framework'))
]

if settings.DEBUG:

        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
