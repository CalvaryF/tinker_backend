from django.http.response import JsonResponse
from numpy.random.mtrand import sample
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import numpy as np
import math
from scipy.stats import skewnorm, probplot, pareto
import pandas as pd


class PCA(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "PCA":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class KMeansClustering(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "PCA":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class HierarchicalClustering(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "PCA":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class ModelBasedClustering(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "PCA":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)



## Principal Component Analysis

## K Means Clustering

## Hirearchical Clustering

## Model-Based Clustering