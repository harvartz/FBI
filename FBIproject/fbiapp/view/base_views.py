from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from ..models import *
from ..forms import *
from django.contrib import auth
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

import json




def main(request):
    return render(request, 'fbiapp/index.html')


 # 마이페이지 기능 관련
   
# def mypage(request):
#     return render(request, 'fbiapp/mypage.html')