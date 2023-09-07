'''URL configuration for digiplatform project'''
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='servicemanager/', permanent=True)),
    path("servicemanager/", include("servicemanager.urls")),
]
