

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .  import carsViews,carsImagesView,policyView,coverageView
#both for each view
urlpatterns = [
    url(r'^GetCars/$', carsViews.GetCars.as_view()),#get all cars
    url(r'^PostCar/$', carsViews.PostCar.as_view()),  # get all cars
    url(r'^GetCarByID/$', carsViews.GetCarByID.as_view()),  # post a car
    url(r'^PutCarForUpdate/$', carsViews.PutCarForUpdate.as_view()),  # post a car
    url(r'^PostCarImages/$', carsImagesView.PostCarImages.as_view()),  # get all car

    url(r'^GetPolicy/$', policyView.GetPolicy.as_view()),  # get all cars
    url(r'^PostPolicy/$', policyView.PostPolicy.as_view()),  # get all cars
    url(r'^GetPolicyByID/$', policyView.GetPolicyByID.as_view()),  # post a car
    url(r'^PutPolicyForUpdate/$', policyView.PutPolicyForUpdate.as_view()),

    url(r'^PostCoverage/$', coverageView.PostCoverage.as_view()),  # get all cars
    url(r'^GetCoverageByID/$', coverageView.GetCoverageByID.as_view()),  # get all cars
    url(r'^PutCoverageForUpdate/$', coverageView.PutCoverageForUpdate.as_view()),  # get all cars


]

urlpatterns = format_suffix_patterns(urlpatterns)
