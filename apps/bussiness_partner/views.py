from .models import BussinessPartner, Address, Zone
from rest_framework import viewsets
from .serializers import BussinessPartnerSerializer, AddressSerializer, ZoneSerializer

class WOZone(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class WOAddress(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class WOAssingnments(viewsets.ModelViewSet):
    queryset = BussinessPartner.objects.all()
    serializer_class = BussinessPartnerSerializer
