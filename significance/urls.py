from django.urls import path
from .views import Baysean, ChiSquare, FDist, PValue, PermutationTest, Power, TTest

urlpatterns = [
    path('permtest', PermutationTest.as_view(), name="permtest"),
    path('pvalue', PValue.as_view(), name="pvalue"),
    path('fdist', FDist.as_view(), name="fdist"),
    path('power', Power.as_view(), name="power"),
    path('ttest', TTest.as_view(), name="ttest"),
    path('chisquare', ChiSquare.as_view(), name="chisquare"),
    path('baysean', Baysean.as_view(), name="baysean"),
]