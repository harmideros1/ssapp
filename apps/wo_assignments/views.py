from .models import WorkOrderAssignment
from rest_framework import viewsets, generics
from .serializers import WOAssignmentSerializer
from django_filters.rest_framework import DjangoFilterBackend

# class WOAssingnments(viewsets.ModelViewSet):
class WOAssingnments(generics.ListAPIView):
    queryset = WorkOrderAssignment.objects.all()
    serializer_class = WOAssignmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['technician',]

    # def get_queryset(self):
    #     try:
    #         user_id = self.kwargs['user_id']
    #         queryset = WorkOrderAssignment.objects.filter(technician=user_id)
    #     except KeyError:
    #         queryset = WorkOrderAssignment.objects.all()

    #     return queryset

