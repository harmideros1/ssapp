from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'technician_assignments', views.WOAssingnments)

urlpatterns = [
    # path('', include(router.urls)),
    path('technician_assignments/',views.WOAssingnments.as_view()),
    # url('^technician_assignments/(?P<user_id>.+)/$',views.WOAssingnments.as_view()),
] 