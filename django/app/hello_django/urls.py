from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('hello_django.apps.products.urls')),

    url(r'^api/', include('hello_django.apps.authentication.urls')),
    url(r'^api/', include('hello_django.apps.profiles.urls')),
]
