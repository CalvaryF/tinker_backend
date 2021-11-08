from django.urls import path
from .views import BiasVariance, FakeRegression, LinearRegression, MultipleLinearRegression, NaiveBayes, PolynomialRegression, SplineRegression

urlpatterns = [
    path('linear', LinearRegression.as_view(), name="linear"),
    path('multiplelinear', MultipleLinearRegression.as_view(), name="multiplelinear"),
    path('polynomial', PolynomialRegression.as_view(), name="polynomial"),
    path('spline', SplineRegression.as_view(), name="spline"),
    path('biasvariance', BiasVariance.as_view(), name="biasvariance"),
    path('fake', FakeRegression.as_view(), name="fake"),
]