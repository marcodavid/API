
from .clientModels import TblClients
from .clientSerializers import ClientsSerializer,ClientsAuthSerializer
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate




import hashlib

class GenericMethods:

	def encrypt(self, password):
		encrypted = hashlib.new("sha1", password)
		var = 1;

		return encrypted.hexdigest()


	def get_object(self, pk):
		try:
			return TblClients.objects.get(id_clients=pk)
		except TblClients.DoesNotExist:
			raise Http404


	def check_if_exist(self, password, email):
		qry = TblClients.objects.filter(password=password)
		qry = qry.filter(email=email)
		user_exist = qry
		
		if user_exist:
			return TblClients.objects.get(email=email)


genericMethods = GenericMethods()

#allow to get and post in generic

class GetClients(ObtainAuthToken):
	def get(self, request, format=None):
		snippets = TblClients.objects.all()
		serializer = ClientsSerializer(snippets, many=True)
		return Response(serializer.data)


class PostClientToSign(ObtainAuthToken):#allow to sign user
	def post(self, request, format=None):
		password = request.data.get("password")
		email = request.data.get("email")
		serializer = ClientsSerializer(data=request.data)
		if serializer.is_valid():
			password = genericMethods.encrypt(password)
			exist = genericMethods.check_if_exist(password,email)
			if exist:
				return Response({'error': 'user already exist','Description':serializer.errors}, status.HTTP_400_BAD_REQUEST)
			else:
				snippets = genericMethods.check_if_exist(password, email)
				user = authenticate(username=email, password=password)
				token, created = Token.objects.get_or_create(user=user)
				serializer = ClientsSerializer(snippets, data=request.data)
				if serializer.is_valid():
					serializer.save(password=password)
					return Response({'token': token.key, 'data': serializer.data}, status.HTTP_202_ACCEPTED)
				return Response( status.HTTP_500_INTERNAL_SERVER_ERROR)

		else:
			return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
#if you want a request only about a object or delete/update


class PostClientToLogin(ObtainAuthToken):


	def post(self, request, format=None):
		password = request.data.get("password")
		email = request.data.get("email")
		serializer = ClientsAuthSerializer(data=request.data)
		if serializer.is_valid():
			password=genericMethods.encrypt(password)
			snippets = genericMethods.check_if_exist(password,email)
			if snippets:
				serializer = ClientsSerializer(snippets)
				user = authenticate(username=email, password=password)
				token, created = Token.objects.get_or_create(user=user)
				return Response({'token':token.key,'data':serializer.data}, status.HTTP_202_ACCEPTED)
		return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

class PutClientForUpdate(ObtainAuthToken):
	def put(self, request, format=None):#update data
		pk = request.data.get("id_clients")
		snippet = genericMethods.get_object(pk)
		serializer = ClientsSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteClient(ObtainAuthToken):
	def delete(self, request, format=None):#delete info details
		pk = request.data.get("id_clients")
		TblClients = genericMethods.get_object(pk)
		TblClients.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


