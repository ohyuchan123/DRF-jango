from django.shortcuts import render
# `Render`는 `HttpResponse` 객체를 반환하는 함수로, 
# `template`을 `context`와 엮어서 `HttpReponse` 객체로 쉽게 반환해 
# 주는 함수라고 한다.

from django.http import HttpResponse
#해당 View는 결과값을 `HttpResponse`나 `JsonResponse` 객체에 담아 전달


from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# 기존 장고 방식
def hello_world(requset):
    return HttpResponse("hello world")

# DRF 방식으로
@api_view() # api_view 데코레이터는 DRF에서 제공하는 데코레이터 중 하나이며,
# 이를 사용하면 Django의 view 함수를 DRF view 함수로 변경할 수 있습니다.
def hello_world_drf(request):
    return Response({"message":"Hello, world!"})
    # 함수 내에서는 REsponse 객체를 반환하고 있으며, 이 객체는 DRF에서 제공하는 Response 클래스의 인스턴스입니다.
    # 이 클래스는 일반 Django HttpResponse 객체와 비슷하지만, JSON 지렬화 및
    # CORS(Cross-Origin Resource Sharing)지원과 같은 추가 기능을 제공합니다.

# 따라서 위 DRF 방식으로 코드는 GET 요청을 수신하면 "message" 키와 "Hello, world" 값을 가진 JSON 응답을 반환합니다.