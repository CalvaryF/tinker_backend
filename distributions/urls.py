from django.urls import path
from .views import FlushSession, RandomNormal

urlpatterns = [
    path('randomnormal', RandomNormal.as_view(), name="randomnormal"),
    path('flush', FlushSession.as_view(), name="flush"),
]