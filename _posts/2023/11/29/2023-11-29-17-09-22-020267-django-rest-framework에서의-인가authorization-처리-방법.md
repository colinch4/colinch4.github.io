---
layout: post
title: "[python] Django REST framework에서의 인가(Authorization) 처리 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 웹 API의 보안을 유지하기 위해 다양한 인증과 인가 기능을 제공합니다. 이 중에서도 인가(Authorization)는 특정 사용자가 특정 리소스에 접근할 수 있는 권한을 부여하는 과정을 말합니다.

## 인가 종류

Django REST framework은 다양한 인가 방식을 지원합니다. 가장 일반적인 인가 방식은 다음과 같습니다.

### 1. Token-based 인가

토큰 기반 인가는 사용자가 인증을 통해 발급된 토큰을 사용하여 API에 접근하는 방식입니다. 사용자가 인증 후 토큰을 발급받으면 해당 토큰을 API 요청의 헤더에 포함하여 보낼 수 있습니다. Django REST framework는 `rest_framework.authtoken` 모듈을 사용하여 토큰 기반 인가를 제공합니다.

### 2. Session-based 인가

세션 기반 인가는 사용자가 웹 애플리케이션에 로그인한 상태를 유지하며 인가를 처리하는 방식입니다. 사용자가 로그인하면 세션을 유지하며, 이후의 API 요청은 세션 정보를 통해 인가를 확인합니다. Django REST framework는 기본적으로 세션 기반 인가를 지원합니다.

### 3. OAuth 인가

OAuth 인가는 외부 서비스의 인증을 통해 API에 접근하는 방식입니다. 사용자가 외부 서비스를 통해 API에 접근할 수 있는 권한을 부여하면 해당 서비스를 통해 인가를 처리합니다. Django REST framework는 `django-oauth-toolkit` 패키지를 사용하여 OAuth 인가를 지원합니다.

## 인가 설정하기

Django REST framework에서 인가를 설정하는 방법은 간단합니다. 다음의 단계를 따라하면 됩니다.

1. `settings.py` 파일에서 `DEFAULT_AUTHENTICATION_CLASSES` 변수를 설정하여 사용할 인증 방식을 지정합니다. 예를 들어, 토큰 기반 인증을 사용하려면 다음과 같이 설정합니다.

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.TokenAuthentication',
       ],
   }
   ```

2. 인증 방식에 따라 사용자 모델과의 연결을 설정합니다. 토큰 기반 인증을 사용한다면, `AUTH_USER_MODEL`과 `Token` 모델을 연결하여 사용자 인증을 처리할 수 있습니다. 예를 들어,

   ```python
   AUTH_USER_MODEL = 'myapp.CustomUser'
   ```

이제 Django REST framework에서 인가를 사용할 준비가 되었습니다.

## 인가 기능 사용하기

인가 기능을 사용하려면 각 API 뷰나 뷰셋에 인가 클래스를 지정해야 합니다. 인가 클래스는 해당 인가 방식에 따라 다르게 지정됩니다.

### 토큰 기반 인가

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 인가된 사용자만 접근 가능한 코드
        ...
```

### 세션 기반 인가

Django REST framework는 내부적으로 Django의 인가 시스템을 사용하므로 별도의 설정이 필요하지 않습니다. Django의 기본 세션 인가 기능을 사용하기만 하면 됩니다.

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class MyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 인가된 사용자만 접근 가능한 코드
        ...
```

### OAuth 인가

Django REST framework에서 OAuth 인가를 사용하려면 `django-oauth-toolkit` 패키지를 설치하고 설정해야 합니다. 자세한 내용은 해당 패키지의 문서를 참조하십시오.

## 결론

Django REST framework에서의 인가 처리는 간단하게 설정할 수 있고 다양한 인가 방식을 지원합니다. 웹 API의 보안을 강화하기 위해서는 적절한 인가 방식을 선택하여 적용하는 것이 중요합니다. Django REST framework의 자세한 내용은 공식 문서를 참조하시면 됩니다.

**참고 자료:**
- Django REST framework 공식 문서: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- Django OAuth Toolkit 공식 문서: [https://django-oauth-toolkit.readthedocs.io/](https://django-oauth-toolkit.readthedocs.io/)