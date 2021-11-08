from django.urls import path
from .views import PCA, HierarchicalClustering, KMeansClustering, ModelBasedClustering

urlpatterns = [
    path('pca', PCA.as_view(), name="pca"),
    path('kmeans', KMeansClustering.as_view(), name="kmeans"),
    path('hcluster', HierarchicalClustering.as_view(), name="hcluster"),
    path('modelcluster', ModelBasedClustering.as_view(), name="modelcluster"),
]