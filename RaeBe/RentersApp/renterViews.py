
from  .renterSerializers import *
from django.http import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

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

class GetRentByIdClients(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"]
		snippet = TblRent.objects.all().filter(id_clients=pk)
		serializer = RenterSerializer(snippet,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class PostRent(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = RenterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostMail(ObtainAuthToken):
	def post(self, request, format=None):
		email = request.data.get ("email")
		body = request.data.get ("body")
		title = request.data.get ("title")
		subject, from_email, to = title , 'raebems@gmail.com', email
		text_content = 'Mensaje importante'

		html_content = body
		msg = EmailMultiAlternatives (subject, text_content, from_email, [to])
		msg.attach_alternative (html_content, "text/html")
		msg.content_subtype = 'html'  # set primary content to be text/html
		msg.mixed_subtype = 'related'  # it is important part that ensures embedding of image

		with open ("media/mail assets/RaeBe.png", mode='rb') as f:
			image = MIMEImage (f.read ())
			msg.attach (image)
		msg.send ()
		return Response(status=status.HTTP_200_OK)


class PutRentForUpdate(ObtainAuthToken):
	def put(self, request, format=None):#update data
		pk = request.data.get("id_rent")
		snippet = TblRent.objects.get(id_rent=pk)
		serializer = RenterSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetRateByIdClients(ObtainAuthToken):
	def get(self, request,  format = None):
		pk = request.GET["id_clients"]
		snippet = RelationsComments.objects.all().filter(id_clientsreceiver=pk)
		serializer = RateSerializer(snippet,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class PostRate(ObtainAuthToken):
	def post(self, request, format=None):
		serializer = RateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)