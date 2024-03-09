from rest_framework.routers import DefaultRouter
from paises.viewsets import CountriesViewset
from django.urls import path, include

router = DefaultRouter()

router.register(basename="iso2",viewset=CountriesViewset, prefix="iso2")

urlpatterns = [

    path("api/", include(router.urls))

]