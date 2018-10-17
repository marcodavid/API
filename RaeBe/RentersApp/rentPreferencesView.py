
from .renterSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblRentpreferences.objects.get(id_clients=pk)
		except TblRentpreferences.DoesNotExist:
			raise Http404

genericMethods = GenericMethods()


class PostRentPreferences(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = RentPreferencesSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetRentPreferencesByClient(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"];
		snippet = genericMethods.get_object(pk)
		serializer = RentPreferencesSerializer(snippet)
		return Response(serializer.data)

class PutRentPreferencesForUpdate(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get("id_clients")
		snippet = genericMethods.get_object(pk)
		serializer = RentPreferencesSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteRentPreferences(ObtainAuthToken):
	def delete(self, request, format=None):
		pk = request.data.get("id_clients")
		TblRentpreferences = genericMethods.get_object(pk)
		TblRentpreferences.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)