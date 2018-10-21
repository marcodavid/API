
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


class PostCarImages(ObtainAuthToken):
		def post(self, request, format=None):
			serializer = FileSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





