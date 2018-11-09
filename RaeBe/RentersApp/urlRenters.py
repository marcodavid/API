
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import  rentPreferencesView,renterViews
urlpatterns = [
    url(r'^GetRentByID/$', renterViews.GetRentByID.as_view()),#get all users,
	url(r'^PostRent/$', renterViews.PostRent.as_view()),  # get all users,
	url(r'^PutRentForUpdate/$', renterViews.PutRentForUpdate.as_view()),  # get all users,

    url(r'^GetRentPreferencesByClient/$', rentPreferencesView.GetRentPreferencesByClient.as_view()),#get all users,
	url(r'^PostRentPreferences/$', rentPreferencesView.PostRentPreferences.as_view()),  # get all users,
	url(r'^PutRentPreferencesForUpdate/$', rentPreferencesView.PutRentPreferencesForUpdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)