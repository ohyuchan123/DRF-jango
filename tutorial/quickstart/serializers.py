from django.contrib.auth.models import User, Group
from rest_framework import serializers

#HyperlinkedModelSerializer는 개발자가 관련 리소스에 대한 하이퍼링크를
# 포함하면서 Django 모델과 같은 복잡한 데이터 유형을 직렬화 및 역직렬화할
#  수 있도록 하는 Django REST 프레임워크의 직렬 변환기입니다.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']