from django.http.response import JsonResponse
from numpy.random.mtrand import sample
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import numpy as np
import math
from scipy.stats import skewnorm, probplot, pareto, binom, poisson, weibull_min, expon, bernoulli
import pandas as pd



class Pareto(APIView):
    ## more long tails?
    ##maybe do power law in general and have pareto be a part of it
    def post(self, request, format=None):
        size = request.data.get("size")
        a, m = 3., 2.  # shape and mode
        if size != None:
            data = {
            'pareto': ((np.random.pareto(3, size))).tolist()
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class Normal(APIView):

    def post(self, request, format=None):
        size = request.data.get("size")
        skew = request.data.get("skew")
        values = skewnorm.rvs(skew, loc=0, scale=1, size=size).tolist()
        valuesseries = pd.Series(values)
        mad = valuesseries.mad()
        mean = skewnorm.mean(skew, loc=0, scale=1)
        median = skewnorm.median(skew, loc=0, scale=1)
        if size != None:
            data = {
            'normal': values,
            "stdrandom": np.std(values),
            "stdpdf": skewnorm.std(skew, loc=0, scale=1),
            "mad":mad,
            "mean": mean
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class CentralLimitTheorem(APIView):
    def post(self, request, format=None):
        samplesize = request.data.get("samplesize")
        samplemeans = request.data.get("samplemeans")
        np.random.seed(1)
        x = [np.mean(
        np.random.randint(
            -40, 40, samplesize)) for _i in range(samplemeans)]
        print(len(x))
        if samplesize != None:
            data = {
            'means':x,
    
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

def interval(sample, level, n):
    mean = np.mean(sample)
    d = level*(np.std(sample)/math.sqrt(n))
    ci = [mean + d ,mean -d]
    return ci
    
## might want to comment on non normal distributions here
class ConfidenceInterval(APIView):
    #calculates a number of confidence intervals from random samples
    def get(self, request, format=None):
        confidencelevel= .95
        samplesize = 100
        numsamples = 10
        #this can be replaced with a gaussian or whatever
        samples = [
        np.random.randint(
            10, 30, samplesize).tolist() for _i in range(numsamples)]
        intervals = []

        #means can be appended here if needed
        for i in samples:
            intervals.append(interval(i, confidencelevel, samplesize))
        
        ci=''
        data={
        "intervals": intervals, 
        "firstsample":samples[0]
        }
        return JsonResponse(data, status=status.HTTP_200_OK)

class pdf(APIView):
    def post(self, request, format=None):
        size = request.data.get("size")
        p = []
        i = -500
        n = skewnorm.pdf(0,0, loc=0, scale=1)
        print(n)
        while i < 500:
            p.append([i*.01,(skewnorm.pdf(i*.01,0, loc=0, scale=1))*2.5*80])
            i += 1
        if size != None:
            data = {
            'pdf': p
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


# Check to see if this is right, related to the QQ and fitting
class Probplot(APIView):
    def get(self, request, format=None):
        #data = request.data.get("data")
        values = skewnorm.rvs(2, loc=0, scale=1, size=10).tolist()
        prob = probplot(values)
        data = {
        "prob": tuple(zip(prob[0][0].tolist(),prob[0][1].tolist())),
        "line": prob[1]
        }
        return JsonResponse(data, status=status.HTTP_200_OK)
        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

# Test this one too, should work
class LLN(APIView):
    ##maybe add options for different distributions
     def get(self, request, format=None):
            samplesize = 100
            values = pareto.rvs(1)
            mean = np.empty(samplesize)
            for n in range(1, samplesize):
                mean[n] = np.mean(values[:n])
            data = {
            "mean":mean
            }
            return JsonResponse(data, status=status.HTTP_200_OK)
            return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

# Maybe use one of these to explain the concept of a shape parameter

## Discrete distributions

## Bernoulli

class Poisson(APIView):
    def get(self, request, format=None):
        size = 100
        shape = 1
        values = poisson.rvs(1)
        if size != None:
            data = {
            "poisson":values
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class Bernoulli(APIView):
    def get(self, request, format=None):
        size = 100
        probability = 1
        values = bernoulli.rvs(probability)
        if size != None:
            data = {
            "bernoulli":values
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class Binomial(APIView):
    def get(self, request, format=None):
        size = 100
        ntrials = 10
        probability = .5
        values = binom.rvs(ntrials, probability, size=size)
        if size != None:
            data = {
            "binomail": values
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class Weibull(APIView):
    def get(self, request, format=None):
        size = 100
        values = weibull_min.rvs(1)
        if size != None:
            data = {
            "weibull":values
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


class Exponential(APIView):
    def get(self, request, format=None):
        size = 100
        values = expon(size = size)
        if size != None:
            data = {
            "binomail":values
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)




## Long tail Law of marge numbers / central limmit theorem

## Gaussian Standard deviation

## Long tail standard deviation vs Mean absolute deviation

## Skewness Mean Median

## Jensen's Inequality (maybe this goes somewhere else)



