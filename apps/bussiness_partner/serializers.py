from .models import BussinessPartner, Address, Zone
from rest_framework import serializers

class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zone
        fields = ['code', 'description',]

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'zone',]


class BussinessPartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BussinessPartner
        fields = [
            'code',
            'f_name',
            's_name',
            'l_name',
            'll_name',
            'employe',
            'address',
            'phone',
            'state',
        ]