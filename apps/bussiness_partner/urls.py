from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'bussiness-partner', views.WOAssingnments)
router.register(r'bussiness-partner-address', views.WOAddress)
router.register(r'bussiness-partner-zones', views.WOZone)

urlpatterns = [
    path('', include(router.urls)),
] 