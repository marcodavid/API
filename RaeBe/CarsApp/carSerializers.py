
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


class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('file', 'remark', 'timestamp')


class CoverageSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(CoverageSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model =  RelationsCoverage
        fields = '__all__'
