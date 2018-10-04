
from .carSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblCar.objects.get(id_clients=pk)
		except TblCar.DoesNotExist:
			raise Http404


genericMethods = GenericMethods()

# allow to get and post in generic
class GetCars(ObtainAuthToken):
	def get(self, request, format=None):
		snippets = TblCar.objects.all()
		serializer = CarsSerializer(snippets, many=True)
		return Response(serializer.data)

class GetCarByID(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"]
		snippet = TblCar.objects.get(id_clients=pk)
		serializer = CarsSerializer(snippet)
		return Response(serializer.data, status=status.HTTP_200_OK)

class PostCar(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = CarsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutCarForUpdate(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get("id_clients")
		snippet = genericMethods.get_object(pk)
		serializer = CarsSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



