---
layout: post
title: "[python] Marshmallow의 Schema 클래스와 Fields 클래스의 차이점"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Marshmallow는 Python에서 JSON 직렬화 및 역직렬화를 위한 인기 있는 라이브러리입니다. 이 라이브러리는 JSON 형식의 데이터를 Python 객체로 변환하거나, Python 객체를 JSON으로 변환하는 기능을 제공합니다.

Marshmallow의 핵심 클래스로는 Schema 클래스와 Fields 클래스가 있습니다. Schema 클래스는 Marshmallow의 주요 기능을 담당하며, 데이터의 직렬화 및 역직렬화를 위한 구조를 정의합니다. Fields 클래스는 Schema 클래스 내에 정의되는 필드 타입을 지정하는 역할을 합니다.

## Schema 클래스

Schema 클래스는 Marshmallow에서 가장 중요한 클래스 중 하나입니다. 이 클래스를 사용하여 데이터 모델의 구조를 정의하고, 직렬화 및 역직렬화 동작을 수행합니다. Schema 클래스를 상속받아 사용자 정의 스키마를 만들 수도 있습니다.

`Schema` 클래스의 주요 기능은 다음과 같습니다:
- 필드 유효성 검사
- 직렬화 및 역직렬화 동작 정의
- 데이터 로드 및 저장

다음은 `Schema` 클래스의 간단한 예제입니다:
```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str()
    age = fields.Integer()
    email = fields.Email()
```
위 예제에서 `Schema` 클래스를 상속받은 `UserSchema` 클래스를 정의하였습니다. `UserSchema` 클래스 내에는 `name`, `age`, `email` 등의 필드가 정의되어 있습니다. 이 필드들은 `fields` 클래스를 이용하여 타입을 지정할 수 있습니다.

## Fields 클래스

Fields 클래스는 Schema 클래스 내에서 필드 타입을 정의하기 위해 사용됩니다. 필드 타입은 데이터의 유효성 검사나 변환을 위해 사용됩니다. Marshmallow에서는 다양한 종류의 필드 타입을 제공하며, 필요에 따라 사용할 수 있습니다.

Fields 클래스의 사용 예제입니다:
```python
from marshmallow import fields

class UserSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Integer()
    email = fields.Email()
```
위 예제에서 `Fields` 클래스를 import하고, `name`, `age`, `email` 필드를 정의할 때 `fields` 클래스를 사용하였습니다. 필요한 경우 필드에 대한 추가 옵션을 지정할 수도 있습니다. 위 예제에서는 `name` 필드를 필수 필드로 정의했습니다.

## 결론

Marshmallow의 Schema 클래스와 Fields 클래스는 JSON 직렬화와 역직렬화를 간편하게 수행하도록 도와주는 핵심 클래스입니다. Schema 클래스는 데이터의 구조를 정의하고, 필드 유효성 검사 및 직렬화 동작을 수행합니다. Fields 클래스는 필드 타입을 지정하는 역할을 합니다. 이 두 클래스를 적절히 활용하여 데이터 모델을 정의하고, JSON 데이터를 쉽게 처리할 수 있습니다.

## 참고자료
- [Marshmallow Documentation](https://marshmallow.readthedocs.io/)
- [Marshmallow GitHub Repository](https://github.com/marshmallow-code/marshmallow)