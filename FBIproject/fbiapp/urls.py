from django.urls import path
from fbiapp.view import base_views, recommendation_views, survey_views, user_views
# from . import views

# app_name = 'fbiapp'

urlpatterns = [
    # base_views
    path('', base_views.main, name ='main'),
    path('mypage/', base_views.mypage, name="mypage"),
    # 설문조사
    path('survey/', survey_views.survey, name='survey'),
    path('survey/question', survey_views.question, name='question'),
    path('survey/result', survey_views.result, name='result'),
    # 회원기능
    path('login/', user_views.login, name="login"),
    path('logout/', user_views.logout, name="logout"),
    path('signup/', user_views.signup, name="signup"),
    # 추천기능 
    path('api/result/', recommendation_views.RecommendationView.as_view(), name="result_api"),
    path('result/', recommendation_views.result, name="result"),
    path('input/', recommendation_views.input, name="input"),   
    path('input/test/', recommendation_views.test, name="test"),   
] 