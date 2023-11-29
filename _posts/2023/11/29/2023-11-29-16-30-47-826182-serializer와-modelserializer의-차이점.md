---
layout: post
title: "[python] Serializer와 ModelSerializer의 차이점"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST Framework에서 Serializer와 ModelSerializer는 둘 다 데이터를 직렬화하거나 역직렬화하는 데 사용되는 중요한 도구입니다. 하지만 이 둘은 목적과 사용법에서 차이가 있습니다. 이번 포스팅에서는 Serializer와 ModelSerializer의 주요 차이점에 대해 알아보고자 합니다.

## Serializer

Serializer는 Django에서 제공하는 `serializers.Serializer` 클래스를 기반으로 하며, 다양한 데이터 타입을 다룰 수 있습니다. Serializer를 사용하여 데이터를 직렬화하고, 역직렬화하여 전송하거나 저장할 수 있습니다. Serializer의 사용법은 직관적이고 유연하며, 필요한 모든 필드를 명시적으로 정의할 수 있습니다. 이를 통해 데이터 유효성 검사, 데이터 변환, 관련 필드 및 객체의 포함 등을 다룰 수 있습니다.

```python
from rest_framework import serializers

class MySerializer(serializers.Serializer):
    field1 = serializers.CharField()
    field2 = serializers.IntegerField()
    field3 = serializers.BooleanField()
    
    def create(self, validated_data):
        # 객체 생성 로직 구현
        pass
    
    def update(self, instance, validated_data):
        # 객체 업데이트 로직 구현
        pass
```

## ModelSerializer

ModelSerializer는 Serializer를 상속 받아 사용하는데, Django의 모델과 연결되어 있습니다. ModelSerializer를 사용하면 Serializer에서 수동으로 필드를 추가하거나 메소드를 구현할 필요 없이 모델과 직접적으로 연결하여 쉽게 데이터를 직렬화하거나 역직렬화할 수 있습니다. ModelSerializer는 기본적으로 모델에 정의된 필드와 관계를 자동으로 찾아내어 직렬화에 사용합니다.

```python
from rest_framework import serializers
from myapp.models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = "__all__"
```

## 결론

Serializer는 일반적인 데이터의 직렬화와 역직렬화를 위해 사용되며, 필드를 직접 정의하고 메소드를 구현해야 합니다. ModelSerializer는 모델과 직접 연결되어 모델의 필드와 관계를 자동으로 인식하여 사용하기 때문에 작성할 코드 양이 줄어듭니다.

각각의 용도에 따라 Serializer와 ModelSerializer를 적절하게 사용하는 것이 중요합니다.