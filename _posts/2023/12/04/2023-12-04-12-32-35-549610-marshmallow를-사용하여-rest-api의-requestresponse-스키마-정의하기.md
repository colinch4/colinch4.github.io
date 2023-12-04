---
layout: post
title: "[python] Marshmallow를 사용하여 REST API의 Request/Response 스키마 정의하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

REST API를 개발하는 과정에서 Request와 Response의 스키마를 정의해야 하는 경우가 많습니다. 이 때 Marshmallow를 사용하면 간편하게 스키마를 정의하고 검증할 수 있습니다. 이번 블로그 포스트에서는 Python의 Marshmallow를 사용하여 REST API의 Request/Response 스키마를 정의하는 방법에 대해 알아보겠습니다.

## Marshmallow란?

Marshmallow는 Python의 직렬화/역직렬화 라이브러리로, 데이터 객체를 다른 프로그램이나 시스템에서 쉽게 사용할 수 있는 형식으로 변환하는 기능을 제공합니다. Marshmallow는 JSON, YAML 등 다양한 데이터 형식을 지원하며, 객체의 유효성 검사를 위한 기능도 제공합니다.

## 설치

Marshmallow를 사용하기 위해 먼저 설치해야 합니다. 다음 명령어를 사용하여 Marshmallow를 설치할 수 있습니다.

```python
pip install marshmallow
```

## Request 스키마 정의하기

API의 Request에는 클라이언트가 서버로 전송하는 데이터가 포함됩니다. 이 데이터의 형식을 정의하기 위해 Request 스키마를 정의해야 합니다.

```python
from marshmallow import Schema, fields

class CreateUserRequestSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    age = fields.Integer(required=True)
```

위의 코드에서 `CreateUserRequestSchema`는 CreateUser API의 Request 데이터 형식을 정의하는 스키마입니다. 필드마다 Marshmallow에서 제공하는 적절한 타입을 사용하고, 필요에 따라 추가적인 옵션을 설정할 수 있습니다.

## Response 스키마 정의하기

API의 Response에는 서버가 클라이언트로 전송하는 데이터가 포함됩니다. 이 데이터의 형식을 정의하기 위해 Response 스키마를 정의해야 합니다.

```python
class UserResponseSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    age = fields.Integer(required=True)
```

위의 코드에서 `UserResponseSchema`는 User 객체의 데이터 형식을 정의하는 스키마입니다.

## 사용 예시

Request와 Response 스키마를 정의한 뒤에는 이를 실제로 사용할 수 있습니다. 예를 들어, Flask를 사용하여 아래와 같은 CreateUser API를 개발한다고 가정해봅시다.

```python
@app.route('/users', methods=['POST'])
def create_user():
    # Request 데이터를 스키마로 검증
    request_data = request.get_json()
    schema = CreateUserRequestSchema()
    errors = schema.validate(request_data)
  
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Request 데이터를 처리
    # ...
    
    # Response 데이터를 스키마로 형식화
    user = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'age': 30
    }
    response_data = UserResponseSchema().dump(user)
  
    return jsonify(response_data), 201
```

위의 예시에서 `create_user()` 함수에서는 Request 데이터를 `CreateUserRequestSchema`로 검증하고, Response 데이터를 `UserResponseSchema`로 형식화하여 반환합니다.

## 결론

Marshmallow를 사용하면 REST API의 Request와 Response 데이터의 형식을 간편하게 정의하고 검증할 수 있습니다. 이를 통해 개발자는 데이터의 무결성을 높이고, API를 보다 안정적으로 개발할 수 있습니다.

## 참고 자료
- [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/)