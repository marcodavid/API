

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .  import carsViews
#both for each view
urlpatterns = [
    url(r'^GetCars/$', carsViews.GetCars.as_view()),#get all cars
    url(r'^PostCar/$', carsViews.PostCar.as_view()),  # get all cars
    url(r'^GetCarByID/$', carsViews.GetCarByID.as_view()),  # post a car

]

urlpatterns = format_suffix_patterns(urlpatterns)
