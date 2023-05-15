# django-rest-knox? - 04.20

django-rest-knox는 Django 웹 프레임워크를 사용하여 RESTful API를 구축할 때 인증과 권한 부여를 처리하는 라이브러리입니다.

이 라이브러리는 JSON Web Token(JWT)을 사용하여 인증을 수행하며 Knox라는 미둘웨어를 통해 API 요청을 인증합니다. Know는 세션 기반 인증과 달리 토큰 기반 인증을 제공하며, 토큰이 만료되면 자동으로 재발급 됩니다.

django-rest-knox를 사용하면 간단하게 RESTful API를 구축할 수 있으며, 인증과 권한 부여를 처리하는 데 필요한 복잡한 작업을 간소화할 수  있습니다. 

또한 이 라이브러리는 Django의 다양한 기능과 플러그인과 호환되므로 다른 Django 앱과 함께 사용할 수 있습니다.

django-rest-knox를 사용하려면 패키지를 다운로드 해야 합니다.

```
pip install django-rest-knox
```

`settings.py`

```python
INSTALLED_APPS = [

    # 기본 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 생성한 앱
    'accountapp',
    'sinppets',

    # 설치한 앱
    'rest_framework',
    'knox', #-> 이렇게 추가시켜줘야 됩니다.
]
```

**하단에 이렇게 코드를 추가시켜줘야 합니다.**

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
}
```