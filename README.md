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

## Serialization
객체를 저장하거나 메모리, 데이터베이스 혹은 파일로 옮기려면 어떻게 해야 할까? 이럴 때 필요한 것이 직렬화이다.  

직렬화란 객체를 바이트 스트림으로 바꾸는 것, 즉 객체에 저장된 데이터를 스트림에 쓰기 write를 위해 연속적인 serial 데이터로 변환하는 것이다.

직렬화의 주된 목적은 객체를 상태 **그대로 저장**하고 필요할 때 다시 생성하여 사용하는 것이다.

## django-serializer 자세히 알아보기

### 🤔 왜?
장고의 serializer는 잘만 활용하면, 효율적으로 valid 검사부터, 쿼리셋에서 불러오는 것까지 간단히 구현가능하다.

**Serializer**
> 직렬화를 하는 직렬변환기?
> **Serialize(직렬화)**
> **쿼리셋,모델 인스턴스 등의 complex type(복잡한 데이터)를** Json,XML등의 컨텐트 타입으로 쉽게 변환 가능한 python datatype으로 변환시켜줌
>> serializer는 우리가 Django에서 사용하는 파이썬 객체나 queryset 같은 복잡한 객체들을 REST API에서 사용할 json과 같은 형태로 변환해주는 어댑터 역할을 한다.  

Serializer는 DJango Rest Framework에서 나온 새로운 요소입니다. 사전적인 의미는 직렬화 하는 무언가 정도로 볼 수 있습니다.

기본적으로 웹에서 통신을 할 때, 즉 데이터를 주고 받을 때는 어느 정도 정해진 포맷이 있습니다. 대표적인 타입이 JSON이나 XML인데, 대부분의 REST API에서는 JSON으로 주고 받기 때문에 JSON만 잘 알고 있으면 된다.

정확한 의미의 직렬화는 Django 프로젝트에서 내가 만든 모델로부터 뽑은 queryset, 즉 모델 인스턴스를 JSON 타입으로 바꾸는 것입니다.

> **Deserialize**
> **받은 데이터(크롤링시 parse사용>python datatype)를 validating 한 후에 parsed data를 complex type으로 다시 변환**
> 이때는 반드시 is_valid()를 호출하여 검사하자

## Django Rest Framework 회원 인증, 유저 모델 확장하기
**들어가며**
지난 시간에는 DRF에서 가장 중요한 개념인 `serializer`를 이해하고 어떻게 뷰와 작성하는지를 보았습니다. 이번 글에서는 DRF로 토큰 기반 회원 인증/가입 및 로그인을 구현해보도록 하겠습니다.

## 쉽게 알아보는 서버 인증(세션/쿠키,JWT)
### **1. Cookie**

**정의**
- <key,value> 형태의 문자열로 브라우저에 저장되어 사용자를 인식하거나 일부 데이터를 저장하는 역할을 수행한다.
- 서버가 클라이언트에 정보를 전달할 때 저장하고자 하는 정보를 응답 헤더(Cookie)에 저장하여 전달한다.

**등장배경 - 왜?**
- 서버에 요청할 때 마다 사용자가 ID,PW를 통해 로그인을 해야하는 불편함이 있었기 때문이다.
- Cookie는 사용자가 한번 로그인을 하면, 쿠키를 생성하여 저장하고 이후 요청은 로그인없이 진행할 수 있는 편의성을 제공해준다.

**문제점**
- Cookie가 노출되었을 때 ID, PW와 같은 중요정보들이 쉽게 노출된다.
- 웹 브라우저마다 Cookie에 대한 지원 형태가 다르기 때문에 브라우저간 공유가 불가능하다.
- Cookie의 사이즈는 4kb로 제한되어 많은 양의 데이터를 담을 수 없다.

### **2. Session** - 04.20
**등장배경 - 왜?**
- Cookie의 문제점을 해결하기 위해 나온 개념이다.  

Cookie에 ID, PW와 같은 중요 정보들을 담는게아니라, 중요정보가 아닌 인증을 위한 별개의 정보를 세션 저장소에 저장하고, 클라이언트는 이 정보를 쿠키에 대신 담아서 요청하고 서버는 세션 저장소에 있는 정보랑 일치하는지 확인하는 방식이다.

**동작과정**
1. 클라이언트가 IP/PW로 서버에 로그인 요청을 한다.
2. IP/PW로 인증 후 사용자를 식별할 특정 유니크한 세션 ID를 만들어 마치 자물쇠처럼 서버의 세션 저장소에 저장한다.
3. 세션 ID를 특정한 형태(Cookie or json)로 클라이언트에 다시 반환하다.
4. 이후 사용자 인증이 ㅍㄹ요한 정보를 요청할 때마다 이 세션 ID를 쿠키에 담아 서버에 함꼐 전달한다.
5. 인증이 필요한 api일 때, 서버는 세션 ID가 세션 저장소에 있는지 확인한다.
6. 있다면 인증 완료 후 api처리, 없다면 401 에러를 반환한다.

**문제점**
- 세션 ID,Cookie 등이 탈취된다면 세션 저장소를 전부 지워 해결 가능하지만, 탈취당하지 않은 정상적인 사용자도 모두 재인증을 해야하는 상황이 발생한다.
- 무엇보다 http의 가장 큰 특성중 하나인 `stateless`를 위배한다는 것이다.
- 만약 서버를 스케일 아웃 해야 한다면? 1번 서버에 로그인한 사용자가 다른 2번 서버로 요청을 보내게 된다면, 2번 서버에는 로그인 상태가 남아있지 않기 때문에 다시 로그인해야 하는 상황이 발생하다.

**문제점 해결**
<span style="color:#FF8200">세션 클러스터링</span>

- 세션 클러스터링으로 섭간 로그인 정보가 담긴 세션을 공유하는 방법이 있지만 실제 서비스와 관련없는 인프라적인 작업으로 서버 리소스를 많이 쓰게 되는 단점이 있다.
- 전체적인 서버 규모가 크지 않다면 나쁘지 않은 방법이지만, MSA로 잘게 쪼개져 수십 수백개의 서버로 이루어진다면 단점이 극명하게 드러날 것이다.

<span style="color:#FF8200">스터키 세션</span>

- 스케일 아웃 시 여러 서버에 세션 정보를 복사할 필요 없도록 특정 세션을 처음 처리한 서버에게 이후 같은 세션의 요청을 같은서버가 처리하도록 하는 방식이다.
- A사용자가 맨처음에 A서버에게 요청했다면 이후 요청은 모두 A서버가 처리하는 방식이다.
- 문제점은 각 서버가 균일하게 요청을 처리할 수 없다는점, 특정 서버에게 요청이 몰릴수도 있다는 문제점이 있다. 즉 로드가 균일하게 밸런싱되지 않는다.
- 무엇보다 클라이언트의 상태를 어디선가 들고있어야 한다는 문제점을 해결하지 못하였다

> 이러한 문제점들을 해결하기 위해 나온 개념이 JWT이다.