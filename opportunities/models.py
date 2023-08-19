from django.db import models

# Create your models here.
from django.db import models

class Opportunity(models.Model):
    ADOPTION = 'A' 
    FOSTERING = 'F' 
    TYPE_CHOICES = [ 
        (ADOPTION, 'Adoption'),
        (FOSTERING, 'Fostering'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True)
    size = models.CharField(max_length=6, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], blank=True)
    description = models.TextField(blank=True)
    shelter = models.ForeignKey('Shelter', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
