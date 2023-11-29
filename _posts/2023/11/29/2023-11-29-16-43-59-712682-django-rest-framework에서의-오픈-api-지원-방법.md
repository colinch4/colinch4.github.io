---
layout: post
title: "[python] Django REST framework에서의 오픈 API 지원 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 Django 프레임워크를 확장하여 RESTful API를 쉽게 개발할 수 있는 도구입니다. 이를 통해 오픈 API를 제공하려는 경우 다음과 같은 방법을 사용할 수 있습니다.

## 1. Django REST framework의 설정

Django REST framework의 설정 파일인 `settings.py`에서 API 관련 설정을 할 수 있습니다. `INSTALLED_APPS`에 `rest_framework`를 추가하고, `REST_FRAMEWORK` 설정을 통해 API의 기본 동작을 커스터마이징할 수 있습니다. 예를 들면 다음과 같은 설정이 있을 수 있습니다:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

위의 설정 예시에서는 인증과 권한 설정을 통해 인증된 사용자에게만 API 접근을 허용하고, 토큰 기반의 인증 방식을 사용하도록 설정하였습니다. REST framework의 설정에 대한 자세한 내용은 공식 문서[^1^]를 참조하세요.

## 2. Serializers 사용하기

Django REST framework의 핵심 기능 중 하나는 serializers입니다. Serializers는 Django 모델을 JSON 형식으로 직렬화하고 요청 데이터를 역직렬화하여 처리할 수 있는 기능을 제공합니다. serializers를 사용하여 API에서 사용할 데이터 형식을 정의하고, 이를 통해 모델 정보를 포함하는 JSON 응답을 생성할 수 있습니다. serializers의 예시 코드는 아래와 같습니다:

```python
from rest_framework import serializers

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
```

위의 예시에서는 `MyModel` 모델을 기반으로 하는 serializer를 정의하였습니다. 이를 통해 모델의 필드들을 자동으로 직렬화하여 API 응답으로 반환할 수 있습니다.

## 3. Views 및 URL 설정

Django REST framework에서는 API의 엔드포인트와 해당 엔드포인트의 동작을 처리하는 views를 설정해야 합니다. 이를 위해 Django의 `views.py` 파일에 `APIView` 또는 `ViewSet` 클래스를 사용하여 views를 정의합니다. 아래는 예시 코드입니다:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    def get(self, request, format=None):
        data = MyModel.objects.all()
        serializer = MyModelSerializer(data, many=True)
        return Response(serializer.data)
```

위의 예시에서는 `MyModel`의 모든 인스턴스를 가져와 직렬화한 결과를 JSON 형태로 반환하는 APIView를 정의하였습니다.

마지막으로, `urls.py` 파일에서 views와 API 엔드포인트의 URL을 매핑시켜야 합니다. 아래는 예시 코드입니다:

```python
from django.urls import path
from .views import MyAPIView

urlpatterns = [
    path('mymodels/', MyAPIView.as_view(), name='mymodels'),
]
```

위의 예시에서는 `/mymodels/`에 해당하는 API 엔드포인트로 들어오는 모든 요청을 `MyAPIView`와 매핑하여 처리합니다.

## 결론

Django REST framework은 강력하고 유연한 도구로서 오픈 API를 쉽게 개발할 수 있도록 도와줍니다. 위의 방법을 통해 Django REST framework을 사용하여 오픈 API를 지원할 수 있습니다.

[^1^]: https://www.django-rest-framework.org/