from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import numpy as np

class RandomCorrelation(APIView):
    lookup_url_kwarg = 'size'
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            self.request.session.set_expiry(0)

        size = request.data.get(self.lookup_url_kwarg)
        if size != None:
            #this is where the calculation gets done
            #self.request.session['randomcorrelation'] = np.random.normal(loc=0, scale=1.0, size=size).tolist()
           
            data = {
            'randomcorrelation': self.request.session.get('randomcorrelation'),
            }
            return JsonResponse(data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid post data, did not find size'}, status=status.HTTP_400_BAD_REQUEST)


## non linear correlation

## Sensitivity of correlation

## non transitive correlation

## mutual information

##correlation squared?
