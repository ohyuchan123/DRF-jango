"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from tutorial.quickstart import views

routers = routers.DefaultRouter()
routers.register(r'users',views.UserViewSet)
routers.register(r'groups',views.GroupViewSet)


# 뷰 대신 뷰 세트를 사용하고 있기 때문에 라우터 클래스에 뷰 세트를 등록하기만 하면
# API에 대한 URL conf를 자동으로 생성할 수 있습니다.

# API URL에 대해 더 많은 제어가 필요한 경우 일반 클래스 기반 보기를 사용하고
# URL conf를 명시적으로 작성할 수 있습니다.

# 탐색 가능한 API와 함께 사용할 기본 로그인 및 로그아웃 보기를 포함하고 있습니다.
# 이는 선택 사항이지만 API에 인증이 필요하고 탐색 가능한 API를 사용하려는 경우에 유용합니다.
urlpatterns = [
    path('',include(routers.urls)),
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework'))
]
