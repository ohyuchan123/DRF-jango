from django.urls import path, include

urlpatterns = [
    path("", include("dj_rest_auth.urls")),  # 해당 라인 추가
    path("registration/", include("dj_rest_auth.registration.urls")),
]
