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


class NaiveBayes(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "NB":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class LinearDiscriminant(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "LinearDis":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class LogisticRegression(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "Logistic":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class ROCCurve(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "roc":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class SupportVectorMachine(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "SVM":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)



## Naive Bayes Classification

## Linear DIscriminant

## Logistic Regression

## ROC Curve

## Support Vector Machine
