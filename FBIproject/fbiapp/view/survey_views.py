# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render, get_object_or_404, redirect
# from ..models import *
# from ..forms import *
# from django.contrib import auth
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.core.paginator import Paginator

# import json

# # 설문조사 기능 관련
    
# def survey(request):
#     return render(request, 'fbiapp/survey/survey.html')

# def question(request):
#     questions = Questions.objects.all()
#     page_numbers_range = 1
#     paginator = Paginator(questions, page_numbers_range)
#     page = request.GET.get('page')
#     questions = paginator.get_page(page)
#     current_page = int(page) if page else 1
#     start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#     end_index = start_index + page_numbers_range
#     page_range = paginator.page_range[start_index:end_index]
#     return render(request, 'fbiapp/survey/question.html', {'questions':questions, 'page_range':page_range, 'paginator':paginator})


# def result(request):
#     if request.method == 'POST':
#         user = User.object.filter(user_id=request.user)[0]
#         print("user : ", user)
#         result = json.loads(request.body)
#         user.age = result['answer1']
#         user.keyword = result['answer2']
#         user.state = result['answer3']
#         user.environment = result['answer4']
#         user.cycle = result['answer5']
#         print("유저 : ", user.age, user.keyword, user.state, user.environment, user.cycle)
#         user.save()
#         return render(request, 'fbiapp/index.html', {'result': result})
