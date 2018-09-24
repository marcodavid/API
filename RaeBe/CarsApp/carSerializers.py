
from .carModels import *
from rest_framework import serializers



class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblCar
        fields = '__all__'

class CarsByIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblCar
        fields = 'id_clients'