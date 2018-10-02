from .carModels import *
from .carSerializers import *
from django.http import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import hashlib


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblCar.objects.get(id_clients=pk)
		except TblCar.DoesNotExist:
			raise Http404


genericMethods = GenericMethods()

# allow to get and post in generic
class GetCars(APIView):
	def get(self, request, format=None):
		snippets = TblCar.objects.all()
		serializer = CarsSerializer(snippets, many=True)
		return Response(serializer.data)

class PostForGetCarByID(APIView):
	def post(self, request, format=None):
		pk = request.data.get("id_clients")
		snippets = TblCar.objects.filter(id_clients = pk)
		serializer = CarsSerializer(snippets, many=True)
		return Response(serializer.data)

class PostCar(APIView):
	def post(self, request, format=None):
		serializer = CarsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




