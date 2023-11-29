---
layout: post
title: "[python] Django REST framework에서의 API 개발 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework는 Django 프레임워크를 기반으로 한 파이썬 웹 프레임워크입니다. 이를 사용하여 강력하고 효율적인 API를 개발할 수 있습니다. 이번 블로그 포스트에서는 Django REST framework를 사용하여 API를 개발하는 방법에 대해 알아보겠습니다.


## 1. Django REST framework 설치

먼저, Django REST framework를 설치해야 합니다. 아래의 명령어를 사용하여 설치할 수 있습니다.

```shell
pip install djangorestframework
```

## 2. Django 프로젝트 설정

Django REST framework를 사용하기 위해서는 Django 프로젝트에 몇 가지 설정이 필요합니다. `settings.py` 파일을 열고 아래와 같이 설정해주세요.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
```

위의 설정에서는 REST framework를 `INSTALLED_APPS`에 추가하고, 기본적인 퍼미션 클래스와 인증 클래스를 설정하였습니다.


## 3. Serializer 작성

Serializer는 Django REST framework에서 데이터의 직렬화를 위해 사용됩니다. Serializer를 작성하여 모델 데이터를 JSON 형식으로 변환시킬 수 있습니다. 아래는 Serializer를 작성하는 예시입니다.

```python
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
```

위의 예시에서는 `MyModel` 모델의 모든 필드를 직렬화하는 Serializer를 작성했습니다.


## 4. ViewSet 작성

ViewSet은 Django REST framework에서 데이터에 접근하는 호출 방식을 제공하는 클래스입니다. 아래는 ViewSet을 작성하는 예시입니다.

```python
from rest_framework import viewsets
from .serializers import MyModelSerializer
from .models import MyModel

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

위의 예시에서는 `MyModel` 모델의 데이터를 처리하는 ViewSet을 작성했습니다.


## 5. URL 설정

마지막으로, API의 URL을 설정해야 합니다. `urls.py` 파일을 열고 아래와 같이 설정해주세요.

```python
from django.urls import path, include
from .viewsets import MyModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

위의 예시에서는 `mymodel/`로 시작하는 모든 URL을 `MyModelViewSet`에 매핑시켰습니다.


## 결론

Django REST framework를 사용하면 간편하고 효율적으로 API를 개발할 수 있습니다. 위의 단계를 따라하면 Django REST framework를 사용하여 API를 개발할 수 있습니다. 추가적인 기능을 사용하고 싶을 경우, Django REST framework 문서를 참조하시기 바랍니다.

**참고 자료:**
- [Django REST framework 공식 문서](https://www.django-rest-framework.org/)
- [Django 공식 문서](https://docs.djangoproject.com/)