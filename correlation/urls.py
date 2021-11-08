from django.urls import path

from correlation.views import RandomCorrelation, RandomView


urlpatterns = [
path('randomcorrelation', RandomCorrelation.as_view(), name="randomcorrelation"),
path('v', RandomView.as_view(), name="v"),
]