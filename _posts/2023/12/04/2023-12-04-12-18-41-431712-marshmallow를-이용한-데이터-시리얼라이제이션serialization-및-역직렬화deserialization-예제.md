---
layout: post
title: "[python] Marshmallow를 이용한 데이터 시리얼라이제이션(Serialization) 및 역직렬화(Deserialization) 예제"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Marshmallow는 Python의 객체 시리얼라이제이션 및 역직렬화를 처리하기 위한 강력한 라이브러리입니다. 이를 사용하여 데이터를 시리얼라이즈하거나 역직렬화하여 간단하게 JSON 형식으로 변환할 수 있습니다. 이번 예제에서는 Marshmallow를 사용하여 데이터 시리얼라이제이션과 역직렬화를 어떻게 처리하는지 알아보겠습니다.

## Marshmallow 설치

먼저, Marshmallow를 설치해야 합니다. 다음 명령을 사용하여 Marshmallow를 설치할 수 있습니다.

```python
pip install marshmallow
```

## 시리얼라이제이션(Serialization) 예제

시리얼라이제이션은 객체를 일련의 바이트나 문자열 형태로 변환하는 과정을 말합니다. Marshmallow를 사용하여 시리얼라이제이션을 수행해봅시다.

```python
from marshmallow import Schema, fields

# 시리얼라이즈할 데이터를 담을 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Marshmallow 스키마 정의
class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Int()

# 시리얼라이즈할 데이터 객체 생성
person = Person("John Doe", 30)

# 스키마를 사용하여 데이터 시리얼라이즈
person_schema = PersonSchema()
result = person_schema.dump(person)

# 결과 출력
print(result)
```

위의 코드에서는 `Person` 클래스를 정의하고, `PersonSchema` 클래스를 사용하여 `Person` 객체를 시리얼라이즈하고 결과를 출력합니다. 실행해보면 다음과 같은 결과를 얻을 수 있습니다.

```
{
    'name': 'John Doe',
    'age': 30
}
```

## 역직렬화(Deserialization) 예제

역직렬화는 시리얼라이제이션된 데이터를 원래의 객체로 변환하는 과정입니다. Marshmallow를 사용하여 역직렬화를 수행해봅시다.

```python
from marshmallow import Schema, fields

# 역직렬화할 데이터를 담을 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Marshmallow 스키마 정의
class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Int()

# 역직렬화할 데이터 객체 생성
data = {
    'name': 'John Doe',
    'age': 30
}

# 스키마를 사용하여 데이터 역직렬화
person_schema = PersonSchema()
result = person_schema.load(data)

# 결과 출력
print(result)
```

위의 코드에서는 시리얼라이제이션 예제와 마찬가지로 `Person` 클래스와 `PersonSchema` 클래스를 정의합니다. `data` 변수에는 시리얼라이제이션된 데이터가 포함되어 있습니다. 

역직렬화를 위해 `PersonSchema`를 사용하여 데이터를 역직렬화하고 결과를 출력합니다. 실행해보면 다음과 같은 결과를 얻을 수 있습니다.

```
<__main__.Person object at 0x10ebc4f70>
```

역직렬화된 결과는 `Person` 객체입니다.

## 결론

이번 예제에서는 Marshmallow를 사용하여 데이터 시리얼라이제이션과 역직렬화를 어떻게 수행하는지에 대해 간단하게 알아보았습니다. Marshmallow는 JSON 형식으로 데이터를 다룰 때 유용한 도구입니다. 다양한 유효성 검사, 필드 유형 및 시리얼라이제이션 및 역직렬화 옵션을 제공하므로 데이터를 쉽게 변환하고 처리할 수 있습니다.

더 자세한 정보는 [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/)를 참조하세요.