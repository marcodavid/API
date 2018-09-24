

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .  import clientViews
from .  import addressView
from .  import driverLicenseView
#both for each view
urlpatterns = [
    url(r'^GetClients/$', clientViews.GetClients.as_view()),#get all users,
    url(r'^PostClientToSign/$', clientViews.PostClientToSign.as_view()),#post new user you only need pass  and email
    url(r'^PostClientToLogin/$', clientViews.PostClientToLogin.as_view()),  #post email and password(login)  and response  json with all user information
    url(r'^PutClientForUpdate/$', clientViews.PutClientForUpdate.as_view()),
    url(r'^DeleteClient/$', clientViews.DeleteClient.as_view()),  #post email and password(login)  and response  json with all user information
    url(r'^GetAllAddress/$', addressView.GetAllAddress.as_view()),  # get all address ,post new address
    url(r'^GetAddressByClient/$', addressView.GetAddressByClient.as_view()),  # get all address ,post new address
    url(r'^PostAddress/$', addressView.PostAddress.as_view()),  # get all address ,post new address
    url(r'^PutAddressForUpdate/$', addressView.PutAddressForUpdate.as_view()),  # get all address ,post new address
    url(r'^DeleteAddress/$', addressView.DeleteAddress.as_view()),  # get all address ,post new address
    url(r'^GetDriverLicenseByClient/$', driverLicenseView.GetDriverLicenseByClient.as_view()),  # get all address ,post new address
    url(r'^PostDriverLicense/$', driverLicenseView.PostDriverLicense.as_view()),  # get all address ,post new address
    url(r'^PutDriverLicenseForUpdate/$', driverLicenseView.PutDriverLicenseForUpdate.as_view()),  # get all address ,post new address
    url(r'^DeleteDriverLicense/$', driverLicenseView.DeleteDriverLicense.as_view()),  # get all address ,post new address

]

urlpatterns = format_suffix_patterns(urlpatterns)
