from .models import Opportunity, Shelter
from rest_framework.serializers import ModelSerializer

class OpportunitySerializer(ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['url', 'name', 'species', 'breed', 'age', 'gender', 'size', 'description', 'shelter', 'image', 'type']
        
class ShelterSerializer(ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['url', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number']