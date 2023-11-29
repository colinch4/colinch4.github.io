---
layout: post
title: "[python] Django REST framework에서의 멀티 포멧(Response format) 처리 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 RESTful API를 쉽게 개발할 수 있도록 도와주는 강력한 도구입니다. 이 프레임워크를 사용하면 다양한 요청과 응답 포맷을 처리할 수 있습니다. 이번 블로그 포스트에서는 Django REST framework에서 멀티 포맷을 처리하는 방법에 대해 알아보겠습니다.

## 멀티 포맷 지원 설정

Django REST framework에서 멀티 포맷을 지원하기 위해서는 다음과 같은 설정이 필요합니다.

1. `REST_FRAMEWORK` 설정을 수정하여 지원할 포맷을 지정합니다. 예를 들어, JSON과 XML을 지원하려면 다음과 같이 설정합니다:

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.XMLRenderer',
    )
}
```

2. 각 API 뷰에 대한 `renderer_classes` 옵션을 설정하여 해당 뷰에서 사용할 포맷을 지정할 수 있습니다. 예를 들어, `JSONRenderer`를 사용하여 JSON 포맷을 지원하는 경우 다음과 같이 설정합니다:

```python
class MyAPIView(APIView):
    renderer_classes = [JSONRenderer]
```

## 포맷 선택

Django REST framework에서는 클라이언트 요청 헤더를 통해 클라이언트가 원하는 포맷을 선택하고 처리할 수 있습니다. 기본적으로 Django REST framework는 Accept 헤더를 사용하여 사용 가능한 포맷을 확인합니다.

예를 들어, 클라이언트가 Accept: application/json 헤더를 전송한 경우, JSON 포맷으로 응답을 반환합니다. 만약 클라이언트가 Accept: application/xml 헤더를 전송한 경우, XML 포맷으로 응답을 반환합니다.

또는 URL 뒤에 .json 또는 .xml과 같은 확장자를 추가하여 특정 포맷을 요청할 수도 있습니다.

## 포맷 인식 및 변환

Django REST framework은 자동으로 클라이언트 요청 포맷을 인식하고 적절한 응답 포맷으로 변환해줍니다. 예를 들어, 클라이언트가 JSON으로 요청한 경우, Django REST framework는 자동으로 요청을 JSON으로 인식하고 응답을 JSON으로 반환합니다.

또한 Django REST framework은 데이터 직렬화 및 역직렬화를 위한 다양한 Serializer 클래스를 제공합니다. 이를 사용하여 데이터를 특정 포맷으로 변환하고 클라이언트에 제공할 수 있습니다.

## 요약

이번 포스트에서는 Django REST framework에서 멀티 포맷을 처리하는 방법에 대해 알아보았습니다. `REST_FRAMEWORK` 설정을 수정하여 지원할 포맷을 설정하고, 각 API 뷰에서 `renderer_classes` 옵션을 사용하여 특정 포맷을 선택할 수 있습니다. Django REST framework는 클라이언트 요청 헤더를 통해 포맷을 선택하고, 데이터 직렬화 및 역직렬화를 자동으로 처리합니다.

더 자세한 내용은 [Django REST framework 공식 문서](https://www.django-rest-framework.org/)를 참고하시기 바랍니다.