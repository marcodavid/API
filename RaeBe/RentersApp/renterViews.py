
from  .renterSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblRent.objects.get(id_clients=pk)
		except TblRent.DoesNotExist:
			raise Http404


genericMethods = GenericMethods()

# allow to get and post in generic
class GetRents(ObtainAuthToken):
	def get(self, request, format=None):
		snippets = TblRent.objects.all()
		serializer = RenterSerializer(snippets, many=True)
		return Response(serializer.data)

class GetRentByID(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clientsrenter"]
		snippet = TblRent.objects.all().filter(id_clientsrenter=pk)
		serializer = RenterSerializer(snippet,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class PostRent(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = RenterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PutRentForUpdate(ObtainAuthToken):
	def put(self, request, format=None):#update data
		pk = request.data.get("id_rent")
		snippet = TblRent.objects.get(id_rent=pk)
		serializer = RenterSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

