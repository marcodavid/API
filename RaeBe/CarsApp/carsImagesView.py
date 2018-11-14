
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

class GetCarImagesByID(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"]
		snippet =File.objects.all().filter(id_clients=pk)
		serializer = FileSerializer(snippet,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class PostCarImages(ObtainAuthToken):
		def post(self, request, format=None):
			serializer = FileSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutActiveImages(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get ("id_clients")
		snippet = File.objects.filter(id_clients=pk)
		serializer = CarsImagesSerializer (snippet, data=request.data)
		if serializer.is_valid ():
			serializer.save(isValid=1)
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteImage(ObtainAuthToken):
	def delete(self, request, format=None):  # delete info details
		pk = request.GET["id_clients"]
		type = request.GET["type"]
		id = request.GET["idFile"]
		snippet = File.objects.filter(id_clients=pk)
		sinippet = snippet.filter (type=type)
		if type == "1":
			snippet = snippet.filter(id=id)
			snippet.delete()
		else:
			snippet.delete ()
		return Response(status=status.HTTP_204_NO_CONTENT)
