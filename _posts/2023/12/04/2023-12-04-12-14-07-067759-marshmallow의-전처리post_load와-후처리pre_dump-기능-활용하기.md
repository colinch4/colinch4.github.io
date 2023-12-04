---
layout: post
title: "[python] Marshmallow의 전처리(post_load)와 후처리(pre_dump) 기능 활용하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Marshmallow는 Python에서 JSON 직렬화와 역직렬화를 쉽게 처리할 수 있는 라이브러리입니다. Marshmallow의 기능 중에서 전처리와 후처리 기능을 사용하여 데이터 변환과 유효성 검사를 수행할 수 있습니다.

## 전처리(post_load)

전처리는 JSON 데이터를 객체로 역직렬화하는 과정에서 수행되는 작업입니다. 이 기능을 사용하면 역직렬화된 객체에 대해 추가적인 변환 작업을 수행할 수 있습니다.

```python
from marshmallow import Schema, fields, post_load

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class UserSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
```

위 코드에서 `User` 클래스는 `name`과 `age`라는 두 개의 속성을 가지고 있습니다. `UserSchema` 클래스에서는 `User` 객체로 역직렬화하기 위해 `post_load` 데코레이터를 사용한 `make_user` 메서드를 정의하였습니다. 이 메서드에서는 `User` 객체를 생성하고 역직렬화된 데이터를 이용하여 객체의 속성을 초기화합니다. 즉, JSON 데이터를 역직렬화할 때 해당 메서드가 자동으로 호출되어 객체로 변환됩니다.

## 후처리(pre_dump)

후처리는 객체를 JSON 데이터로 직렬화하는 과정에서 수행되는 작업입니다. 이 기능을 사용하면 직렬화된 JSON 데이터에 대해 추가적인 변환 작업을 수행할 수 있습니다.

```python
from marshmallow import Schema, fields, pre_dump

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class UserSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    
    @pre_dump
    def format_age(self, user, **kwargs):
        user.age = f"{user.age}세"
        return user
```

위 코드에서 `User` 클래스와 `UserSchema` 클래스는 이전과 동일합니다. 다만, 이번에는 `pre_dump` 데코레이터를 사용한 `format_age` 메서드를 정의하였습니다. 이 메서드에서는 객체의 `age` 속성 값을 변환하여 직렬화할 때 반영될 JSON 데이터를 수정합니다. 위 예제에서는 `age` 값을 "{age}세"로 변환하여 직렬화될 JSON 데이터에 반영합니다.

## 결론

Marshmallow의 전처리와 후처리 기능을 사용하면 JSON 데이터와 객체 간의 자유로운 변환 작업을 수행할 수 있습니다. 전처리 기능을 활용하여 역직렬화된 객체에 대해 추가적인 초기화 작업을 수행하고, 후처리 기능을 활용하여 객체를 직렬화할 때 원하는 형식으로 데이터를 변환할 수 있습니다.

참고: [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/en/stable/), [Marshmallow GitHub 저장소](https://github.com/marshmallow-code/marshmallow)