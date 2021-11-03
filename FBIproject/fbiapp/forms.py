from django import forms

# 선택지 
type_Choices = (
    ("11", "일반형"),
    ("12", "일회용 생리대"),
    ("99", "입는 오버나이트"),
    ("121", "어플리케이터형"),
    ("645", "일회용 라이너"),
    ("648", "디지털형"),
    ("942", "생리용품 세트"),
)

topSheet_Choices = (
    ("25", "유기농순면"),
    ("26", "순면"),
    ("27", "순면감촉"),
    ("213", "재생섬유"),
    ("214", "실크감촉"),
)

absorbent_Choices = (
    ("28", "고분자흡수체(SAP)"),
    ("29", "자연흡수체"),
    ("30", "자연외기타흡수체"),
)

madeIn_Choices = (
    ("31", "한국"),
    ("32", "중국"),
    ("33", "그리스"),
    ("113", "일본"),
    ("119", "슬로베니아"),
    ("120", "체코"),
    ("129", "핀란드"),
)

price_Choices = (
    ("0", "2500원 이하"),
    ("1", "3500원 이하"),
    ("2", "5000원 이하"),
    ("3", "5000원 이상"),
)

class InputForm(forms.Form):
    type = forms.ChoiceField(choices = type_Choices)
    topSheet = forms.ChoiceField(choices = topSheet_Choices)
    absorbent = forms.ChoiceField(choices = absorbent_Choices)
    madeIn = forms.ChoiceField(choices = madeIn_Choices)
    price = forms.ChoiceField(choices = price_Choices)