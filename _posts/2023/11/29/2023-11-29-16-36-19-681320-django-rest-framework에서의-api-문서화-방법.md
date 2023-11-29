---
layout: post
title: "[python] Django REST framework에서의 API 문서화 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 강력하고 유연한 API 개발을 위한 프레임워크입니다. API를 개발할 때, 문서화는 매우 중요한 요소입니다. 이번 글에서는 Django REST framework에서 API 문서를 작성하는 방법에 대해 알아보겠습니다.

## 1. DRF-Swagger

DRF-Swagger는 Django REST framework를 위한 확장 기능으로, API를 자동으로 문서화하고 시각적으로 보여줍니다. 이를 사용하여 간단하고 직관적인 API 문서를 생성할 수 있습니다.

설치 방법은 다음과 같습니다:

```python
pip install django-rest-swagger
```

설치가 완료되면, `settings.py` 파일에 다음과 같은 코드를 추가합니다:

```python
INSTALLED_APPS = [
    ...
    'rest_framework_swagger',
]
```

그리고 `urls.py` 파일에 다음과 같은 코드를 추가합니다:

```python
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API 문서')

urlpatterns = [
    ...
    path('docs/', schema_view),
]
```

이제 `/docs` URL에 접속하면 Swagger UI를 통해 API 문서를 확인할 수 있습니다.

## 2. DRF-YASG

DRF-YASG는 DRF-Swagger와 유사한 기능을 제공하는 Django REST framework용 다른 확장 기능입니다. 다양한 커스터마이즈 옵션과 함께 API 문서를 자동으로 생성할 수 있습니다.

DRF-YASG를 설치하려면 다음 명령을 실행합니다:

```python
pip install drf-yasg
```

설치 후, `settings.py` 파일에 다음을 추가합니다:

```python
INSTALLED_APPS = [
    ...
    'drf_yasg',
]
```

그리고 `urls.py` 파일에 다음과 같은 코드를 추가합니다:

```python
from django.urls import path
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API 문서",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ...
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```

이제 `/docs` URL에 접속하면 DRF-YASG를 통해 API 문서를 확인할 수 있습니다.

## 3. Manual Documentation

위에서 언급한 확장 기능을 사용하지 않고도 Django REST framework를 사용하여 수동으로 API 문서를 작성할 수 있습니다. 이 방법은 좀 더 많은 작업을 요구하지만, 완벽하게 커스터마이즈된 문서를 생성할 수 있습니다.

일반적으로, API 뷰 함수나 클래스에 docstring을 작성하여 문서화합니다. docstring에는 해당 API 엔드포인트의 설명, 인자, 반환 값 등이 포함되어야 합니다.

예를 들어:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    """
    이 API는 여러 작업을 수행합니다.
    Args:
        param1 (str): 첫 번째 매개변수입니다.
        param2 (int): 두 번째 매개변수입니다.
    """
    def get(self, request, param1, param2):
        """
        이 엔드포인트는 GET 요청을 처리합니다.
        """
        # 작업 수행
        ...
        return Response(...)
```

이렇게 작성된 docstring은 API 문서를 생성하는 도구를 사용하면 자동으로 문서로 변환됩니다.

## 마무리

위에서 소개한 세 가지 방법을 사용하면 Django REST framework에서 API 문서를 작성할 수 있습니다. 선택한 방법에 따라 자동화된 문서 또는 수동으로 작성된 문서를 생성할 수 있습니다. 적절한 방법을 선택하여 API 문서화를 시작해보세요.