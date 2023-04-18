from django.urls import path,include
from .views import hello_world,hello_world_drf

# url은 언더바(_)보단 하이픈(-)으로 작성하자
urlpatterns = [
    path('hello-world/',hello_world),
    path('hello-world-drf/',hello_world_drf),
]