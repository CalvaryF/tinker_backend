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


class LinearRegression(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "LinearRegression":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class MultipleLinearRegression(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "LinearRegression":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class PolynomialRegression(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "LinearRegression":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class SplineRegression(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "LinearRegression":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class BiasVariance(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "LinearRegression":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class FakeRegression(APIView):
    ## more long tails?
    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "LinearRegression":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

## Linear Regression

## Multiple Linear Regression

## Polynomial Regression

## Spline Regression

## Linear Regression for long tail data (bad)

## Bias vs Variance


