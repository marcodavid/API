
from .clientModels import *
from rest_framework import serializers



class ClientsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TblClients
        fields = (

            'id_clients',
            'firstname',
            'lastname',
            'email',
            'password',
            'isrenter',
            'age',
            'curp',
            'telcountry',
            'lada',
            'telnumber',
            'id_address',
            'imgprofilephoto',
            'fulldata'
        )




class ClientsAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblClients
        fields = (


            'email',
            'password'

        )


class AddressSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = TblAddress
        fields = (

            'id_address',
            'id_clients',
            'zipcode',
            'country',
            'state',
            'province',
            'numint',
            'numext',
            'street',
            'city'
        )



class DriverLicenseSerializer(serializers.ModelSerializer):


    class Meta:
        model = TblDriverlicense
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblLocation
        fields = '__all__'
