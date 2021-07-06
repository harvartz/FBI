from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name ='main'),
    path('survey/', views.survey, name='survey'),
    # path('mypage/<user_id>', views.mypage, name="mypage"),
    path('mypage/', views.mypage, name="mypage"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
] 