# DRF-tutorial
장고 REST 튜토리얼

작정하고 장고! Django REST Framework 유튜브 강의와 DRF 공식문서를 통해 공부하였습니다.

- <a href="https://www.django-rest-framework.org/">공식문서 링크</a>

## 왜 REST를 써야하는가?
REST API는 헤더 부분에 uri처리 메서드를 명시한다. 이로써 필요한 데이터 바디에 표현할 수 있다. 이는 특정 메서드의 세부 표현을 다양한 언어(json,xml)로 작성할 수 있는 장점이 있고, 헤더 표현의 가독성 향상이라는 효과도 가져다 준다.

## Django REST Framework
Django REST 프레임 워크는 웹 API를 구축하기위한 강력하고 유연한 툴킷입니다.
**What is REST**
Roy Thomas Fielding  
<span style="color:#FFE13C">로이 필딩</span>

로이 필딩이라는 사람이 REST(Representational State Transfer)아키텍처 스타일을 개발한 핵심 인물 중 한명이다.

자신의 박사 학위 논문에서 REST에 대한 개념을 상세히 설명하였다.

1. Using HTTP protocol
2. Convenient resource management
3. Platform independent

**왜 사용하는 가?**
- 웹 브라우징 가능한 API는 개발자에게 큰 유용성입니다.
- OAuth1a 및 OAuth2 용 패키지를 포함한 인증 정책.
- ORM 및 비 ORM 데이터 소스를 모두 지원하는 직렬화.
- 끝까지 사용자 정의 가능-더 강력한 기능이 필요하지 않은 경우 일반 기능 기반보기를 사용하십시오.
- 광범위한 문서 및 훌륭한 커뮤니티 지원.
- Mozilla, Red Hat, Heroku, Eventbrite 등 국제적으로 인정받는 기업에서 사용하고 신뢰합니다.

## 라이브러리 설치
pip install 할때 따로 따로 해줄 필요없이 같이 넣어주면 다 설치해준다.
```
pip install djangorestframework markdown
```

## MVT
**Model**
- 모델(Model)은 데이터베이스에 저장되는 데이터를 의미한다.
**View**
- 뷰(View)는 실직적으로 프로그램 로직이 동작하여 데이터를 가져오고 적절하게 처리한 결과를 템플릿에 전달
**Template**
- 템플릿(Template)은 사용자에게 보여지는 UI부분을 의미합니다.

![](https://velog.velcdn.com/images%2Fdouen159%2Fpost%2F36e581b2-2480-4a84-a65a-f50f88023152%2FKakaoTalk_20200713_005145657.jpg)

장고에서 MVT 패턴에 따라 처리하는 과정을 요약하면 다음과 같습니다.
- 클라이언트로부터 요청을 받으면 URLconf를 이용하여 URL을 분석합니다.
- URL 분석 결과를 통해 해당 URL에 대한 처리를 담당할 뷰를 결정합니다.
- 뷰는 자신의 로직을 실행하면서, 만일 데이터베이스 처리가 필요하면 모델을 통해 처리하고 그 결과를 반환받습니다.
- 뷰는 자신의 로직 처리가 끝나면 템플릿을 사용하여 클라이언트에 전송할 HTML 파일을 생성합니다.
- 뷰는 최종 결과로 HTML 파일을 클라이언트에 보내 응답합니다.

## ORM
**❗ORM이란**
- **ORM**은 Object Relational Mapping(객체-관계-매핑)의 약자이다.
- **ORM**은 객체와 데이터베이스의 관계를 매핑해주는 도구이다. 
- **ORM**은 프로그래밍 언어의 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 도구이다.
- **ORM**은 프로그래밍 언어의 객체와 관계형 데이터베이스 사이의 중계자(통역자) 역할을 한다.
- **ORM**은 **MVC 패턴에서 모델(Model)을 기술하는 도구**이다.
- **ORM**은 **객체와 모델 사이의 관계를 기술하는 도구**이다.

## Routing(라우팅)
어떤 주소로 들어갔을 때 어떤 기능을 실행할지의 연결고리를 작성하는 것이 라우팅이라고 한다.

## ❓HTTPResponse에 대하여
장고를 공부하다가 보니 `HttpReponse`에 대해서 나와서 `HttpResponse`에 대해서 정리하면 좋을 것 같아 정리하였습니다.

### HttpResponse
장고는 `request`와 `response` 객체로 서버와 클라이언트가 주고 받는데, 아래와 같은 절차를 거친다.

1. 특정 페이지가 Request 되면, 장고는 메타데이터를 포함하는 `HttpRequest`객체를 생성한다.
2. 장고는 `urls.py`에서 정의한 특정 View 클래스/함수에 첫 번째 인자로 해당 `HttpRequest` 객체를 전달
3. 해당 View는 결과값을 `HttpResponse`나 `JsonResponse` 객체에 담아 전달

이를 위해서 장고는 `django.http` 모듈에서 `HttpRequest`와 `HttpResponse` API를 제공하는 것이다.

### Render
추가로 Render에 대해서도 작성하면 좋을 것 같아 정리하였습니다.
`Render`는 `HttpResponse` 객체를 반환하는 함수로, `template`을 `context`와 엮어서 `HttpReponse` 객체로 쉽게 반환해 주는 함수라고 한다.

이 함수의 기본형은 
```python
render(request(필수),template_name(필수),
        context=None,content_type=None,
        status=None,using=None)
```
이렇게 되어 있다.

🤔 정확하지 않을 수 있다.
현재 이해한 내용을 작성했기 때문에 정확하지 않을 수 있다.
- template_name : 불러오고 싶은 템플릿 명을 적는다. 이전 함수에서 `loader.get_template()`함수 안에 들어간 인자를 적으면 된다.
- context : View에서 사용하던 변수(Dict 자료형)를 html 템플리에서 전달하는 역할을 한다. `key`값이 템플릿에서 사용할 변수 이름, `value`값이 파이썬 변수가 된다.

**HttpReponse는 아래와 같이 불러올 수 있다**

```python
from django.http import HttpReponse
```

## 정규표현식
정규표현식이란 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어라고 합니다.


## DRF Response 코드 분석
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def hello_world_drf(request):
    return Response({"message":"Hello, world!"})
```

