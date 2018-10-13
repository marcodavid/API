
from .clientSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblDriverlicense.objects.get(id_clients=pk)
		except TblDriverlicense.DoesNotExist:
			raise Http404

genericMethods = GenericMethods()


class PostDriverLicense(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = DriverLicenseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetDriverLicenseByClient(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"];
		snippet = genericMethods.get_object(pk)
		serializer = DriverLicenseSerializer(snippet)
		return Response(serializer.data)

class PutDriverLicenseForUpdate(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get("id_clients")
		snippet = genericMethods.get_object(pk)
		serializer = DriverLicenseSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteDriverLicense(ObtainAuthToken):
	def delete(self, request, format=None):
		pk = request.data.get("id_clients")
		TblDriverlicense = genericMethods.get_object(pk)
		TblDriverlicense.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)