from .models import Opportunity, Shelter
from rest_framework import serializers

class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['url', 'name', 'species', 'breed', 'age', 'gender', 'size', 'description', 'shelter']
        
class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelter
        fields = ['url', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number']