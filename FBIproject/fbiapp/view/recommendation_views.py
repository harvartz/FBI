from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from ..models import *
from ..forms import *

from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render

import json

# 추천 기능 관련 
    
class RecommendationView(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = request.session.get('result')
        return Response(data)


def result(request):
    context = {}
    return render(request, 'fbiapp/recommendation/result.html')


def input(request):
    return render(request, 'fbiapp/recommendation/input.html')

def test(request, *args, **kwargs):
    item = [3000, 1000, 402, 302, 100]
    data = {"datasets" : item}
    return JsonResponse(data)