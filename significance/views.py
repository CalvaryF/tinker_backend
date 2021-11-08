from django.http.response import JsonResponse
import random
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import numpy as np
import math
from scipy.stats import skewnorm, ttest_ind, t, chi2, chisquare
from pandas import DataFrame as df
from statsmodels.stats.power import TTestIndPower

## overall structure for this should be classical tests vs permutation tests (or something like that)


class PValue(APIView):

    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "PVal":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

# 2 sided? 
def perm(nperms, data, sizeA, sizeB):
    #data is a dataframe
    perms = []
    n = sizeA+sizeB
    idx_B = set(random.sample(range(n),sizeB))
    idx_A = set(range(n)) - idx_B
    return data.loc[idx_B].mean - data.loc[idx_A].mean()

class PermutationTest(APIView):
    
    def get(self, request, format=None):
        locA = 1
        locB = 2
        nperms = 100
        sizeA = 100
        sizeB = 85
        
        ## generate sample data with different locations
        A= skewnorm.rvs(0, loc=locA, scale=1, size = sizeA)
        B= skewnorm.rvs(0, loc=locB, scale=1, size = sizeB)
        perms = [perm(df(A+B),sizeA, sizeB) for _ in range(nperms)]
        meanA = np.mean(A)
        meanB = np.mean(B)
        #perms is a dataframe
        #The below is a p value
        pg = np.mean(perms > meanA - meanB)
        if sizeA != None:
            data = {
            "A":A,
            "meanA": meanA,
            "B":B,
            "meanB": meanB,
            "perms": perms,
            "percent_greater": pg
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

#analysis of variance
#are the standard deviations of two sets of data statistically different from each other
class FDist(APIView):

    def get(self, request, format=None):
        df1 = 1
        df2 = 2
        size = 100
        if size != None:
            data = {
            "FDist":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class Power(APIView):

    def get(self, request, format=None):
        effect = 0.8
        alpha = 0.05
        power = 0.8
        effect_sizes = np.array([0.2, 0.5, 0.8])
        sample_sizes = np.array(range(5, 100))
        analysis = TTestIndPower()
        es1 = [analysis.power(effect, nobs=sample_sizes, ratio=1.0, alpha=alpha)]
        size = 100
        if size != None:
            data = {
            "Power":es1
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class TTest(APIView):

    def get(self, request, format=None):
        locA = 1
        locB = 2
        nperms = 100
        sizeA = 30
        sizeB = 30
        ## generate sample data with different locations
        A= skewnorm.rvs(0, loc=locA, scale=1, size = sizeA)
        B= skewnorm.rvs(0, loc=locB, scale=1, size = sizeB)
        df = 30
        tdist = t(1,df)
        result = ttest_ind(A,B)
        size = 100
        if size != None:
            data = {
            "result":result,
            "tdist":tdist
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class ChiSquare(APIView):

    def get(self, request, format=None):
        expected = [25,25,25,25]
        observed = [10,10,40,40]
        df = 4
        result = chisquare(observed, expected)
        size = 100
        p=[]
        i = 0
        while i < 500:
            p.append([i*.01,(chi2.pdf(i*.01,df))*2.5*80])
            i += 1
        if size != None:
            data = {
            "dist":p,
            "result":result
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class Baysean(APIView):

    def get(self, request, format=None):
        size = 100
        if size != None:
            data = {
            "PVal":""
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


## Sampling / Resampling

## P values vs Power

## P Value Hacking

## Chi Square Test

## Baysean UpdatingBeta DIstribution

## Andrew Gelman examples