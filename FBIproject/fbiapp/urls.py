from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name ='main'),
    # 설문조사
    path('survey/', views.survey, name='survey'),
    path('survey/question', views.question, name='question'),
    path('survey/result', views.result, name='result'),
    # 마이페이지
    path('mypage/', views.mypage, name="mypage"),
    # 회원기능
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    # Input 페이지
     path('input/', views.input, name="input"),   
] 