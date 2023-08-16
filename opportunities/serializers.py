from django.contrib.auth.models import User, Group
from rest_framework import serializers

class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'name', 'species', 'breed', 'age', 'gender', 'size', 'description', 'shelter']
        
class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number']