from django.urls import path
from .views import LLN, Binomial, CentralLimitTheorem, ConfidenceInterval, Exponential, Normal, Pareto, Poisson, Probplot, Weibull, pdf

urlpatterns = [
    path('normal', Normal.as_view(), name="normal"),
    path('pareto', Pareto.as_view(), name="pareto"),
    path('ci', ConfidenceInterval.as_view(), name="ci"),
    path('pdf', pdf.as_view(), name="pdf"),
    path('clt', CentralLimitTheorem.as_view(), name="clt"),
    path('prob', Probplot.as_view(), name="prob"),
    path('lln', LLN.as_view(), name="lln"),
    path('binomail', Binomial.as_view(), name="binomail"),
    path('poisson', Poisson.as_view(), name="poisson"),
    path('weibull', Weibull.as_view(), name="weibull"),
    path('exponential', Exponential.as_view(), name="exponential"),
]