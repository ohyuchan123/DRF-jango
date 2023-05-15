from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializer import BasePersonSerializer,EmailPersonSerializer

# Create your views here.
@api_view(['GET']) # 해당 함수 view에서 처리할 http 메소드
def HelloAPI(request):
    return Response({"message":"Django serializer tutorial"}) # http response 형태로 return
    # 요청을 받아 해당 요청에 대한 응답을 제공하는 기능을 합니다.

@api_view(['GET'])
def PersonAPI(request,id):
    now_person = Person.objects.get(id=id)
    serializer = BasePersonSerializer(now_person)
    return Response(serializer.data)
# => id=1에 대해 리턴된 Response: {'id': 1, 'name': '태뽕', 'phone': '01012345678', 'addr': '주소주소'}

@api_view(['GET'])
def EmailAPI(request, id):
    now_person = Person.object.get(id=id)
    serializer = EmailPersonSerializer(now_person)
    return Response(serializer.data)
# => id=1에 대해 리턴된 Response: {'id': 1, 'email': 'email@email.com'}

# 각 View에서 무언가 데이터를 요청할 때, 지금 예시에는 PersonAPI는 사람에 대한 데이터,
# EmailAPI에서는 이메일에 대한 데이터를 요청할 때 각각 원하는 형태로 응답해줘야 하는데
# 모델은 하나니 필요한 데이터만 골라서 보내줘야된다. 즉 이 역할을 해주는게 시리얼라이저라고
# 생각하면된다.