from .models import Opportunity, Shelter
from rest_framework.serializers import ModelSerializer
        
class ShelterSerializer(ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['url', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number']
        
class OpportunitySerializer(ModelSerializer):
    shelter = ShelterSerializer(many=False, read_only=True)
    class Meta:
        model = Opportunity
        fields = ['url', 'name', 'species', 'breed', 'age', 'gender', 'size', 'description', 'shelter', 'image', 'type']