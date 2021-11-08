from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import numpy as np
import math
from numpy.random import multivariate_normal


# Multivariate Normal (size, covariance)
class RandomCorrelation(APIView):
    def post(self, request, format=None):
        size = request.data.get("size")
        cov = request.data.get("cov")
        print("it works")
        if size != None:
            var1 = 1
            var2 = 1
            cov_matrix = [[var1, cov],[cov, var2]]
           
            data = {
            'randomcorrelation': multivariate_normal([0,0], cov_matrix, size = size).tolist(),
            'CorrelationCof': cov/math.sqrt(var1*var2)
            }
            print (data.get('corcof'))
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)




class RandomView(APIView):
    def get(self,request, format=None):
        var1 = 1
        var2 = 2
        cov = 0
        cov_matrix = [[var1, cov],[cov, var2]]
        data = {
            'randomcorrelation': multivariate_normal([0,0], cov_matrix, size = 100).tolist()
        }
        return JsonResponse(data, status=status.HTTP_200_OK)

## Sensitivity of correlation

## non linear correlation

## non transitive correlation

## mutual information
