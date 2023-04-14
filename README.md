# DRF-tutorial
장고 REST 튜토리얼

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