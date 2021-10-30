from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from ..models import *
from ..forms import *

# 추천 기능 관련 
    
def input(request):
    if request.method == 'GET':
        form = InputForm(request.GET)
        if form.is_valid():
            # 입력 결과
            type = form.cleaned_data['type']
            topSheet = form.cleaned_data['topSheet']
            absorbent = form.cleaned_data['absorbent']
            madeIn = form.cleaned_data['madeIn']
            price= dict(form.fields['price'].choices)[form.cleaned_data['price']]

            print(type, topSheet, absorbent, madeIn, price)


            # 모델 결과 
            item = [3000, 1000, 402, 302, 100]
            return render(request, 'fbiapp/recommendation/result.html', {'datasets' : item})

        else:
            form = InputForm()
            return render(request, 'fbiapp/recommendation/input.html', {'form': form})   

    else:
        form = InputForm()
        print('request is not get')
        return render(request, 'fbiapp/recommendation/input.html', {'form': form})
