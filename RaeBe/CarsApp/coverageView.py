
from .carSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken




class GetCoverageByID(ObtainAuthToken):

	def get(self, request,  format = None):
		pk = request.GET["id_policy"]
		snippet = RelationsCoverage.objects.filter(id_policy=pk)
		serializer = CoverageSerializer(snippet, many = True)
		return Response(serializer.data, status=status.HTTP_200_OK)



class PostCoverage(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = CoverageSerializer(data=request.data,many= True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PutCoverageForUpdate(ObtainAuthToken):
	def put(self, request, format=None):
		pk = request.data.get("id_policy")
		snippet = RelationsCoverage.objects.filter(id_policy=pk)
		serializer = CoverageSerializer(snippet,data=request.data,many = True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCoverage(ObtainAuthToken):
	def delete(self, request, format=None):  # delete info details
		pk = request.GET["id_policy"]
		snippet = RelationsCoverage.objects.filter(id_policy=pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)