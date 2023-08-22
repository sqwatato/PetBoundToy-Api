from .models import Opportunity, Shelter
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
        
class ShelterSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Shelter
        fields = ['url', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number', 'id']
        
class OpportunitySerializer(ModelSerializer):
    shelter = ShelterSerializer(many=False, read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Opportunity
        fields = ['url', 'name', 'species', 'breed', 'age', 'gender', 'size', 'description', 'shelter', 'image', 'type', 'id']