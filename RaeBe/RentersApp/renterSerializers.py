from  .renterModels import *
from rest_framework import serializers

class RentPreferencesSerializer(serializers.ModelSerializer):


    class Meta:
        model = TblRentpreferences
        fields = '__all__'
