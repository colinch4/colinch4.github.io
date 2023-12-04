---
layout: post
title: "[python] Marshmallow의 Date 필드와 DateTime 필드의 사용법과 포맷 지정"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Marshmallow은 Python에서 데이터 직렬화 및 검증을 쉽게 수행할 수 있게 해주는 라이브러리입니다. 이번 블로그 포스트에서는 Marshmallow의 `Date` 필드와 `DateTime` 필드의 사용법 및 포맷 지정에 대해 알아보겠습니다.

## Marshmallow의 Date 필드 사용법

Marshmallow의 `Date` 필드는 날짜 값을 직렬화 및 검증하는 데 사용됩니다. 아래는 `Date` 필드를 사용하여 날짜 값을 직렬화하는 예제입니다.

```python
from marshmallow import Schema, fields

class MySchema(Schema):
    birth_date = fields.Date()

data = {
    "birth_date": date(1990, 10, 15)
}

result = MySchema().dump(data)
print(result)  # {'birth_date': '1990-10-15'}
```

`Date` 필드는 `date` 객체를 기대하며, 직렬화된 결과는 ISO 8601 형식으로 표시됩니다.

## Marshmallow의 DateTime 필드 사용법

Marshmallow의 `DateTime` 필드는 날짜 및 시간 값을 직렬화 및 검증하는 데 사용됩니다. 아래는 `DateTime` 필드를 사용하여 날짜와 시간 값을 직렬화하는 예제입니다.

```python
from marshmallow import Schema, fields

class MySchema(Schema):
    event_time = fields.DateTime()

data = {
    "event_time": datetime(2022, 1, 1, 12, 0, 0)
}

result = MySchema().dump(data)
print(result)  # {'event_time': '2022-01-01T12:00:00'}
```

`DateTime` 필드는 `datetime` 객체를 기대하며, 직렬화된 결과는 ISO 8601 형식으로 표시됩니다.

## 포맷 지정

Marshmallow의 `Date` 필드 및 `DateTime` 필드에서는 날짜 및 시간 값의 포맷을 지정할 수도 있습니다. `format` 매개변수를 사용하여 원하는 포맷을 지정할 수 있습니다. 다음은 `Date` 필드와 `DateTime` 필드에서 포맷을 지정하는 예제입니다.

```python
from marshmallow import Schema, fields

class MySchema(Schema):
    birth_date = fields.Date(format="%Y-%m-%d")
    event_time = fields.DateTime(format="%Y-%m-%dT%H:%M:%S")

data = {
    "birth_date": date(1990, 10, 15),
    "event_time": datetime(2022, 1, 1, 12, 0, 0)
}

result = MySchema().dump(data)
print(result)  # {'birth_date': '1990-10-15', 'event_time': '2022-01-01T12:00:00'}
```

위의 예제에서는 `%Y-%m-%d`와 `%Y-%m-%dT%H:%M:%S`와 같은 포맷 문자열을 사용하여 날짜와 시간 값을 원하는 형식으로 표시합니다.

## 결론

이번 블로그 포스트에서는 Marshmallow의 `Date` 필드와 `DateTime` 필드의 사용법 및 포맷 지정에 대해 알아보았습니다. Marshmallow을 사용하면 날짜와 시간 값을 쉽게 직렬화하고 검증할 수 있습니다. 포맷 지정을 통해 출력 결과의 형식을 원하는 대로 조정할 수 있습니다.