from .models import WorkOrderAssignment
from rest_framework import serializers

# class WOAssignmentSerializer(serializers.HyperlinkedModelSerializer):
class WOAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderAssignment
        fields = "__all__"
        fields = ('id', 'get_full_client', 'address', 'get_technician', 'date')