from rest_framework import serializers
from .models import Person

# ModelSerializer 뒤에서 설명합니다
class BasePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','phone')

# 위 코드는 models.py에서 Person이라는 모델에서 데이터를 뽑아서 응답으로 
#  보낼텐데, 응답의 형태 중 하나인 Base 형태를 BasePersonSerializer라고 정의할께 라는 뜻이다

#이메일 정보를 요청할 때 쓸 수 있는 시리얼라이저는 아래와 같이 제작하면 된다.
class EmailPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'email')
