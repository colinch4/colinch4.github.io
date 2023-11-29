---
layout: post
title: "[python] Django REST framework에서의 CDN과의 연동 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

이 글에서는 Django REST framework를 사용하여 CDN(Content Delivery Network)과의 연동 방법에 대해 알아보겠습니다.

## CDN이란?

CDN은 컨텐츠를 전세계에 효율적으로 배포하기 위해 사용되는 분산 네트워크입니다. CDN은 웹 사이트의 정적 파일(이미지, CSS, JavaScript 등)을 여러 지역의 서버에 복제하여 빠른 전송을 제공합니다.

## Django에서 CDN 사용하기

Django에서 CDN을 사용하려면 `django.contrib.staticfiles` 앱을 활성화하여 정적 파일을 제공해야합니다. 이 앱은 `STATIC_URL` 설정에 지정된 URL을 통해 정적 파일을 서비스합니다.

### 1. `settings.py` 파일 설정

먼저, Django 프로젝트의 `settings.py` 파일을 열고 다음과 같이 `STATIC_URL` 변수를 설정합니다.

```python
STATIC_URL = '/static/'
```

위의 코드에서 `STATIC_URL`은 정적 파일이 서비스될 URL을 나타냅니다. 이 URL을 통해 클라이언트에서 정적 파일에 접근할 수 있습니다.

### 2. Django REST framework에서의 CDN 사용

Django REST framework에서 CDN을 사용하려면 `django-rest-framework-cdn` 패키지를 설치해야합니다. 이 패키지는 Django REST framework에서 CDN을 쉽게 사용할 수 있도록 도와줍니다.

먼저, 패키지를 설치합니다.

```bash
pip install django-rest-framework-cdn
```

설치가 완료되면, `settings.py` 파일에 아래 코드를 추가합니다.

```python
INSTALLED_APPS = [
    ...
    'cdn',
    ...
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_RENDERER_CLASSES': [
        ...
        'cdn.renderers.CDNRenderer',
        ...
    ],
    ...
}
```

위의 설정은 CDNRenderer를 사용하여 REST framework에서 CDN을 활성화시킵니다.

### 3. CDN Renderer를 사용하여 정적 파일 제공

CDN Renderer를 사용하여 정적 파일을 제공하려면, Serializer 클래스에서 `renderer_classes` 속성을 설정해야합니다. 다음은 예시입니다.

```python
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    class Meta:
        renderer_classes = [CDNRenderer]  # CDNRenderer를 사용하여 정적 파일 제공
```

이제 Django REST framework를 사용하여 CDN과 정적 파일을 쉽게 연동할 수 있습니다.

## 마치며

이번에는 Django REST framework에서 CDN과의 연동 방법에 대해 알아보았습니다. CDN을 사용하면 정적 파일을 더 효율적으로 제공할 수 있고, 웹 페이지의 로딩 속도를 개선할 수 있습니다. Django REST framework와 CDN의 강력한 조합을 활용하여 웹 애플리케이션의 성능을 향상시키세요!

참고: [Django REST framework CDN GitHub 저장소](https://github.com/reflectionspro/django-rest-framework-cdn)