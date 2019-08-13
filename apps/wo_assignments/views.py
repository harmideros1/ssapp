from .models import WorkOrderAssignment
from rest_framework import viewsets, generics
from .serializers import WOAssignmentSerializer
from django_filters.rest_framework import DjangoFilterBackend

# class WOAssingnments(viewsets.ModelViewSet):
# class WOAssingnments(generics.ListAPIView):
#     queryset = WorkOrderAssignment.objects.all()
#     serializer_class = WOAssignmentSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['technician', 'client', 'state']

class WOAssingnmentsbk(viewsets.ModelViewSet):
    queryset = WorkOrderAssignment.objects.all()
    serializer_class = WOAssignmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['technician','client']

