---
layout: post
title: "[python] Django REST framework에서의 JWT(JSON Web Tokens) 인증 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 JWT(JSON Web Tokens)을 사용하여 사용자 인증을 구현할 수 있는 강력한 기능을 제공합니다. JWT는 클라이언트와 서버 간에 안전하게 인증을 처리하기 위해 사용되는 토큰 기반 인증 방식입니다. 이를 통해 사용자는 토큰을 받아와 이를 사용하여 서버에 대한 인증을 수행할 수 있습니다.

## 1. JWT 설치

먼저, Django 프로젝트에 `djangorestframework-jwt` 패키지를 설치해야 합니다. 다음 명령을 사용하여 패키지를 설치할 수 있습니다:

```
pip install djangorestframework-jwt
```

## 2. Django 설정

JWT 인증을 사용하려면 Django 설정 파일(`settings.py`)에서 몇 가지 변경을 해야 합니다.

먼저, `INSTALLED_APPS`에 `rest_framework_jwt`를 추가해야 합니다:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_jwt',
    ...
]
```

그런 다음, JWT 설정을 추가합니다. `settings.py` 파일에 다음과 같이 설정을 추가합니다:

```python
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),
}
```

위 설정에서 `SECRET_KEY`는 Django 프로젝트의 시크릿 키로 대체되어야 합니다. 기본적으로 JWT는 HS256(Hashed Message Authentication Code HMAC-SHA256) 알고리즘을 사용하며, 토큰 만료 시간을 7일로 설정합니다. 토큰 갱신을 허용하고, 갱신 토큰의 만료 시간을 30일로 설정합니다.

## 3. JWT 인증 뷰 만들기

다음으로는 JWT 인증을 위한 뷰를 만들어야 합니다. Django의 `views.py` 파일에 다음 코드를 추가합니다:

```python
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    ...
    path('api-token-auth/', obtain_jwt_token),
    ...
]
```

위 코드는 `/api-token-auth/` 경로에 대한 POST 요청을 처리하여 JWT 토큰을 반환하는 뷰를 생성합니다.

## 4. JWT 인증 사용하기

이제 클라이언트는 사용자 인증을 위해 JWT 토큰을 사용할 수 있습니다. 인증이 필요한 API 엔드포인트에 대해 요청 헤더에 JWT 토큰을 포함시켜야 합니다. 보통 `Authorization` 헤더에 `Bearer` 접두사를 붙여서 토큰을 전송합니다. 예를 들어:

```
GET /api/user/1 HTTP/1.1
Host: example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

서버에서는 요청을 받아 토큰의 유효성을 검사하여 인증을 수행합니다. 유효한 토큰인 경우, 해당 요청을 처리하고 사용자에게 응답을 반환합니다.

## 결론

Django REST framework에서 JWT 인증을 구현하는 방법을 알아보았습니다. JWT는 강력하면서도 안전한 사용자 인증 방식으로 Django 프로젝트에서 쉽게 사용할 수 있습니다. JWT를 사용하여 클라이언트와 서버 간의 인증을 안전하게 처리할 수 있습니다.