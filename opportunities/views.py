from .models import Opportunity, Shelter
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OpportunitySerializer, ShelterSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint
class OpportunityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Opportunity.objects.all().order_by('-date_created')
    serializer_class = OpportunitySerializer
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        try:
            data = self.request.data
            img = request.FILES.get('image')
            data.pop('image')
            parsed = {}
            for key, value in data.items():
                if key == 'shelter':
                    parsed['shelter'] = Shelter.objects.get(id=int(value[0]))
                elif key == 'age':
                    parsed['age'] = int(value[0])
                else:
                    parsed[key] = value[0]
            Opportunity.objects.create(**parsed, image=img)
            return Response(
                {'success': 'Opportunity created successfully'},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong'},
                status=status.HTTP_400_BAD_REQUEST
            )
            


class ShelterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    # permission_classes = [permissions.IsAuthenticated]