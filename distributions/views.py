from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import numpy as np

class FlushSession(APIView):
    def get(self,request, format=None):
        if self.request.session.exists(self.request.session.session_key):
            self.request.session.flush()
        return Response('Flushed', status=status.HTTP_200_OK)

class RandomNormal(APIView):
    lookup_url_kwarg = 'size'
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            self.request.session.set_expiry(0)

        size = request.data.get(self.lookup_url_kwarg)
        if size != None:
            self.request.session['randomnormal'] = np.random.normal(loc=0, scale=1.0, size=size).tolist()
           
            data = {
            'randomnormal': self.request.session.get('randomnormal'),
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)

class RandomView(APIView):
    def get(self,request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        data = {
            'randomnormal': self.request.session.get('randomnormal')
        }
        return JsonResponse(data, status=status.HTTP_200_OK)


## Long tail central limit theorem

## Gaussian Standard deviation

## Long tail standard deviation vs Mean absolute deviation

## Skewness Mean Median

## Jensen's Inequality (maybe this goes somewhere else)

## Bias vs Variance

## Confidence Interval

