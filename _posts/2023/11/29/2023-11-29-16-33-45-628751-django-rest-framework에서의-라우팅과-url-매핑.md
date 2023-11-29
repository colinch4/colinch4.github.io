---
layout: post
title: "[python] Django REST framework에서의 라우팅과 URL 매핑"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 웹 APIs를 개발하기 위한 강력한 도구입니다. 이를 통해 URL 매핑 및 라우팅을 통해 API 엔드포인트를 설정할 수 있습니다. 이번 포스트에서는 Django REST framework에서의 라우팅과 URL 매핑에 대해 알아보겠습니다.

## URL 매핑

Django에서 URL 매핑은 `urls.py` 파일을 통해 설정됩니다. API 엔드포인트에 대한 URL 매핑은 Django REST framework에서는 `urls.py` 파일을 각 앱 폴더 내에 작성합니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.PostsAPIView.as_view()),
]
```

위의 예시에서는 `/api/posts/` URL이 `PostsAPIView` 클래스로 매핑되었습니다. 이렇게 매핑된 URL은 요청이 들어오면 해당 view 클래스의 메서드를 실행하게 됩니다.

## 라우팅

Django REST framework에서의 라우팅은 URL 매핑을 통해 설정한 API 엔드포인트에 대한 뷰 클래스 메서드를 실행하기 위한 규칙입니다. 라우팅을 설정하기 위해서는 `urls.py` 파일 내에서 `DefaultRouter`를 사용해야 합니다.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostsViewSet, basename='posts')

urlpatterns = [
    path('api/', include(router.urls)),
]
```

위의 예시에서는 `DefaultRouter`를 사용하여 `posts` 엔드포인트에 대한 라우팅을 설정했습니다. 이제 `/api/posts/`에 대한 GET, POST, PUT, DELETE 요청은 `PostsViewSet`에 정의된 메서드로 라우팅됩니다.

## 결론

Django REST framework에서는 URL 매핑과 라우팅을 통해 API 엔드포인트를 설정할 수 있습니다. 이를 통해 개발자는 간단히 URL을 정의하고, 해당 URL에 대한 뷰 클래스 메서드를 실행할 수 있습니다. 이를 통해 원활한 API 개발이 가능해집니다.

참고문서: [Django REST framework - URL 라우팅](https://www.django-rest-framework.org/api-guide/routers/)