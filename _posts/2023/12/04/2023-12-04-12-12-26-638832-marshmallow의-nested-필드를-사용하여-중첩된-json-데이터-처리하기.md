---
layout: post
title: "[python] Marshmallow의 Nested 필드를 사용하여 중첩된 JSON 데이터 처리하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Marshmallow는 Python용 직렬화 및 역직렬화 라이브러리로, 데이터 모델과 JSON 데이터 사이의 변환을 용이하게 해줍니다. 중첩된 JSON 데이터를 다루는 경우, Marshmallow의 Nested 필드를 사용하여 간편하게 처리할 수 있습니다.

## Nested 필드란?

Marshmallow의 Nested 필드는 JSON 데이터 구조 내에서 다른 객체를 포함하는 필드입니다. Nested 필드를 사용하면 중첩된 객체 간의 관계를 표현할 수 있으며, 중첩된 필드의 데이터를 직렬화 및 역직렬화할 수 있습니다.

## 예제

아래 예제는 사용자 및 사용자의 프로필 정보를 담은 JSON 데이터를 처리하는 방법을 보여줍니다.

먼저, 다음의 데이터 모델을 정의합니다.

```python
from marshmallow import Schema, fields

class ProfileSchema(Schema):
    name = fields.Str()
    age = fields.Int()

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    profile = fields.Nested(ProfileSchema)
```

위의 코드에서 `ProfileSchema`는 프로필 정보를 나타내는 스키마이고, `UserSchema`는 사용자 정보를 나타내는 스키마입니다. `UserSchema`의 `profile` 필드는 `ProfileSchema`의 인스턴스를 포함하고 있으므로, 중첩된 필드로 정의됩니다.

다음은 JSON 데이터를 직렬화하고 역직렬화하는 예제 코드입니다.

```python
# 직렬화
user_data = {
    "id": 1,
    "username": "john",
    "profile": {
        "name": "John Doe",
        "age": 30
    }
}

schema = UserSchema()
result = schema.dumps(user_data)
print(result)  # 결과: {"id": 1, "username": "john", "profile": {"name": "John Doe", "age": 30}}

# 역직렬화
json_data = '{"id": 1, "username": "john", "profile": {"name": "John Doe", "age": 30}}'

result = schema.loads(json_data)
print(result)  # 결과: {'id': 1, 'username': 'john', 'profile': {'name': 'John Doe', 'age': 30}}
```

위의 코드에서 `dumps` 함수는 데이터를 직렬화하고, `loads` 함수는 JSON 데이터를 역직렬화합니다. 결과를 출력하면, 원하는 형태의 JSON 데이터가 생성되는 것을 확인할 수 있습니다.

## 결론

Marshmallow의 Nested 필드를 사용하면 중첩된 JSON 데이터를 처리하기 간단하고 효율적으로 할 수 있습니다. 중첩된 객체 간의 관계를 표현하고, 데이터를 직렬화 및 역직렬화하는 작업을 쉽게 수행할 수 있습니다.

더 자세한 내용은 Marshmallow의 공식 문서를 참조하시기 바랍니다.

- [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/en/stable/)