from django import forms
from .models import User

class UserSignupForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = {'user_id', 'password', 'name', 'age', 'keyword','state','environment','cycle' }


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'user_id', 'password'}


class UserSurveyResultForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'user_id', 'age', 'keyword', 'state', 'environment', 'cycle'}

# 선택지 
smell_Choices = (
    ("1", "아주 약함"),
    ("2", "약함"),
    ("3", "보통(냄)"),
    ("4", "강함"),
    ("5", "아주 강함"),
)

amount_Choices = (
    ("1", "아주 적음"),
    ("2", "적음"),
    ("3", "보통"),
    ("4", "많음"),
    ("5", "아주 많음"),
)

pain_Choices = (
    ("1", "통증 없음"),
    ("2", "조금 아픔"),
    ("3", "아픔"),
    ("4", "많이 아픔"),
    ("5", "매우 아픔"),
)

outside_Choices = (
    ("1", "달리기"),
    ("2", "자전거 타기"),
    ("3", "헬스"),
    ("4", "댄스"),
    ("5", "요가"),
)

inside_Choices = (
    ("1", "TV 보기"),
    ("2", "동영상 시청"),
    ("3", "독서"),
    ("4", "아이돌보기"),
    ("5", "친구와 통화하기"),
    ("6", "공부하기"),
)

class InputForm(forms.Form):
    smell = forms.ChoiceField(choices = smell_Choices)
    amount = forms.ChoiceField(choices = amount_Choices)
    pain = forms.ChoiceField(choices = pain_Choices)
    outside = forms.ChoiceField(choices = outside_Choices)
    inside = forms.ChoiceField(choices = inside_Choices)