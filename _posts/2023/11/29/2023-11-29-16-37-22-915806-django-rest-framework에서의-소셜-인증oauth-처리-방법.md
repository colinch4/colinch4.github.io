---
layout: post
title: "[python] Django REST framework에서의 소셜 인증(OAuth) 처리 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

이 글에서는 Django REST framework를 사용하여 소셜 인증(OAuth)을 처리하는 방법에 대해 알아보겠습니다.

## OAuth란?

OAuth는 소셜 미디어나 다른 웹 서비스들에서 사용되는 인증 프로토콜입니다. 이를 통해 사용자는 자신의 소셜 미디어 계정을 사용하여 서드파티 애플리케이션에 로그인할 수 있습니다.

## Django REST framework 및 Django OAuth Toolkit 설치

Django REST framework와 Django OAuth Toolkit은 pip를 통해 설치할 수 있습니다.

```python
pip install djangorestframework
pip install django-oauth-toolkit
```

또한, REST framework와 OAuth Toolkit을 Django 설정 파일에 추가해야 합니다.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'oauth2_provider',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

## 소셜 인증 설정

OAuth를 사용하기 위해선 각 소셜 미디어 플랫폼에서 애플리케이션을 등록해야 합니다. 여기에서는 Facebook을 예시로 들어보겠습니다.

1. Facebook 개발자 페이지에 접속하여 애플리케이션을 생성합니다.
2. 생성한 애플리케이션의 클라이언트 ID와 클라이언트 시크릿을 받아옵니다.

이후, Django 설정 파일에 다음과 같이 Facebook 소셜 인증을 설정합니다.

```python
SOCIAL_AUTH_FACEBOOK_KEY = 'YOUR_FACEBOOK_APP_ID'
SOCIAL_AUTH_FACEBOOK_SECRET = 'YOUR_FACEBOOK_APP_SECRET'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
```

## 소셜 인증 뷰 생성

Django REST framework에서 소셜 인증을 처리하는 뷰를 생성합니다. 이 뷰에서는 OAuth Toolkit을 사용하여 액세스 토큰을 발급 받고 유저 정보를 가져올 수 있습니다.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from oauth2_provider.models import AccessToken
from social_django.utils import psa


class SocialAuthView(APIView):
    @psa()
    def post(self, request, backend):
        token = request.data.get('access_token')
        user = request.backend.do_auth(token)
        
        if user:
            access_token = AccessToken.from_user(user)
            return Response({'access_token': access_token.token})
        
        return Response({'error': 'Authentication failed.'})
```

위의 뷰를 사용하여 소셜 인증을 처리하는 API 엔드포인트를 생성할 수 있습니다.

## 마무리

이제 Django REST framework에서 소셜 인증(OAuth)을 처리하는 방법에 대해 알아보았습니다. OAuth Toolkit을 사용하여 소셜 미디어 플랫폼과 연동하고, 애플리케이션에서 소셜 인증을 처리할 수 있습니다.

관련 문서:
- Django REST framework: https://www.django-rest-framework.org/
- Django OAuth Toolkit: https://oauthlib.readthedocs.io/en/latest/oauth2/django/index.html