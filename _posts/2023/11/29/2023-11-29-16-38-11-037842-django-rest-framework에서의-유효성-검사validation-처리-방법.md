---
layout: post
title: "[python] Django REST framework에서의 유효성 검사(Validation) 처리 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 웹 애플리케이션의 API 개발을 쉽게 만들어주는 강력한 도구입니다. 이 프레임워크를 사용하면 여러 가지 유효성 검사 기능을 쉽게 구현할 수 있습니다.

## 1. 유효성 검사 개요
유효성 검사는 클라이언트로부터 받은 데이터가 요구 사항을 충족하는지 확인하는 과정입니다. Django REST framework에서는 유효성 검사를 위해 Serializer 클래스를 사용합니다. Serializer 클래스는 모델 인스턴스를 JSON 또는 다른 포맷으로 변환하는 역할을 하며, 필드 유효성 검사, 개체 유효성 검사 등을 수행할 수 있습니다.

## 2. 필수 필드 유효성 검사
Django REST framework에서 필수 필드를 검증하는 가장 간단한 방법은 Serializer 클래스의 필드에 `required=True` 옵션을 추가하는 것입니다. 이렇게 하면 해당 필드가 클라이언트로부터 전달되지 않으면 유효성 검사 오류가 발생합니다. 예를 들어, 아래의 코드는 `name` 필드가 필수 필드임을 정의합니다.

```python
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
```

## 3. 필드 유효성 검사
Django REST framework에서는 `validate_<field_name>` 메서드를 사용하여 필드 단위의 유효성 검사를 수행할 수 있습니다. 이 메서드는 특정 필드의 유효성을 검사하고, 유효하지 않을 경우 `ValidationError`을 발생시킵니다.

```python
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, value):
        # 유효성 검사 로직을 수행하고 유효하지 않을 경우 ValidationError 발생
        if len(value) < 3:
            raise serializers.ValidationError('이름은 3글자 이상이어야 합니다.')
        return value
```

## 4. 개체 유효성 검사
Django REST framework에서는 `validate()` 메서드를 사용하여 전체 개체에 대한 유효성 검사를 수행할 수 있습니다. 이 메서드는 필드 유효성 검사 이후에 호출되며, 일반적으로 서로 다른 필드 간의 유효성을 검사하는 데 사용됩니다. 예를 들어, 아래의 코드는 `start_date`와 `end_date` 필드 간의 유효성을 검사합니다.

```python
from rest_framework import serializers

class DateRangeSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        # 유효성 검사 로직을 수행하고 유효하지 않을 경우 ValidationError 발생
        if start_date > end_date:
            raise serializers.ValidationError('시작 날짜는 종료 날짜보다 이전이어야 합니다.')

        return attrs
```

## 5. 참고 자료
- [Django REST framework 공식문서](https://www.django-rest-framework.org/)
- [Django 공식문서](https://docs.djangoproject.com/)