from .models import WorkOrderAssignment
from rest_framework import serializers

# class WOAssignmentSerializer(serializers.HyperlinkedModelSerializer):
class WOAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderAssignment
        fields = (
            'client',
            'client_contact_person',
            'client_employe',
            'client_phone',
            'client_status',
            'address',
            'description',
            'technician',
            'technician_name',
            'date',
        )