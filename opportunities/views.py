from .models import Opportunity, Shelter
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OpportunitySerializer, ShelterSerializer

class OpportunityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Opportunity.objects.all().order_by('-date_created')
    serializer_class = OpportunitySerializer
    # permission_classes = [permissions.IsAuthenticated]


class ShelterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    # permission_classes = [permissions.IsAuthenticated]