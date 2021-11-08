from django.urls import path
from .views import LinearDiscriminant, LogisticRegression, NaiveBayes, ROCCurve, SupportVectorMachine

urlpatterns = [
    path('prob', NaiveBayes.as_view(), name="prob"),
    path('prob', LinearDiscriminant.as_view(), name="prob"),
    path('prob', LogisticRegression.as_view(), name="prob"),
    path('prob', ROCCurve.as_view(), name="prob"),
    path('prob', SupportVectorMachine.as_view(), name="prob"),
]