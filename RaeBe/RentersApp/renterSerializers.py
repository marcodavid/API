from  .renterModels import *
from rest_framework import serializers

class RenterSerializer(serializers.ModelSerializer):


    class Meta:
        model = TblRent
        fields = '__all__'

class RentPreferencesSerializer(serializers.ModelSerializer):


    class Meta:
        model = TblRentpreferences
        fields = '__all__'
