
from .clientSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblLocation.objects.get(id_clients=pk)
		except TblLocation.DoesNotExist:
			raise Http404

genericMethods = GenericMethods()
class GetLocations(ObtainAuthToken):
	def get(self, request, format=None):
		snippets = TblLocation.objects.all().filter()
		serializer = LocationSerializer(snippets, many=True)
		return Response (serializer.data)


class PostLocation(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = LocationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetLocationByClient(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"];
		snippet = genericMethods.get_object(pk)
		serializer = LocationSerializer(snippet)
		return Response(serializer.data)

class PutLocationForUpdate(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get("id_clients")
		snippet = genericMethods.get_object(pk)
		serializer = LocationSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteLocation(ObtainAuthToken):
	def delete(self, request, format=None):
		pk = request.data.get("id_clients")
		TblLocation = genericMethods.get_object(pk)
		TblLocation.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)