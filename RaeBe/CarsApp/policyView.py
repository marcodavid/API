
from .carSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken


class GenericMethods:


	def get_object(self, pk):
		try:
			return TblPolicy.objects.get(id_car=pk)
		except TblPolicy.DoesNotExist:
			raise Http404


genericMethods = GenericMethods()

# allow to get and post in generic
class GetPolicy(ObtainAuthToken):
	def get(self, request, format=None):
		snippets = TblPolicy.objects.all()
		serializer = PolicySerializer(snippets, many=True)
		return Response(serializer.data)

class GetPolicyByID(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_car"]
		snippet = TblPolicy.objects.get(id_car=pk)
		serializer = PolicySerializer(snippet)
		return Response(serializer.data, status=status.HTTP_200_OK)

class PostPolicy(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = PolicySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutPolicyForUpdate(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get("id_car")
		snippet = genericMethods.get_object(pk)
		serializer = PolicySerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



