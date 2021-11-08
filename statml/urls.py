from django.urls import path
from .views import KNN, RandomForest, TreeModel

urlpatterns = [
    path('prob', KNN.as_view(), name="prob"),
    path('prob', TreeModel.as_view(), name="prob"),
    path('prob', RandomForest.as_view(), name="prob"),
]