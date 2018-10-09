
from .carModels import *
from rest_framework import serializers



class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TblCar
        fields = '__all__'

class CarsImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelationsCarimages
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = TblPolicy
        fields = '__all__'

class CoverageSerializer(serializers.ModelSerializer):

    class Meta:
        model =  RelationsCoverage
        fields = '__all__'
