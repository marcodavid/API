
from .clientSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblAddress.objects.get(id_clients=pk)
		except TblAddress.DoesNotExist:
			raise Http404


genericMethods = GenericMethods()
class GetAllAddress(ObtainAuthToken):
	def get(self, request, format = None):
		snippets = TblAddress.objects.all()
		serializer = AddressSerializer(snippets, many=True)
		return Response(serializer.data)

class PostAddress(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = AddressSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAddressByClient(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"]
		snippet = genericMethods.get_object(pk)
		serializer = AddressSerializer(snippet)
		return Response(serializer.data)

class PutAddressForUpdate(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get("id_clients")
		snippet = genericMethods.get_object(pk)
		serializer = AddressSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAddress(ObtainAuthToken):
	def delete(self, request, format=None):
		pk = request.data.get("id_address")
		TblAddress = genericMethods.get_object(pk)
		TblAddress.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)