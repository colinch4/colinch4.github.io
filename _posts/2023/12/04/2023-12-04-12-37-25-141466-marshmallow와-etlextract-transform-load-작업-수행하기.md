---
layout: post
title: "[python] Marshmallow와 ETL(Extract, Transform, Load) 작업 수행하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

ETL(Extract, Transform, Load)은 데이터 웨어하우스나 데이터베이스로 데이터를 추출하고, 변환하며, 저장하는 과정을 말합니다. Python에서 ETL 작업을 할 때 Marshmallow를 사용하면 데이터의 시리얼라이제이션(Serialization)과 디시리얼라이제이션(Deserialization) 작업을 쉽게 처리할 수 있습니다.

Marshmallow는 Python 객체를 직렬화하고 역직렬화할 수 있는 유연하고 강력한 라이브러리입니다. 이를 사용하여 ETL 작업을 할 수 있습니다.

## Marshmallow 설치

```
pip install marshmallow
```

## Marshmallow를 사용한 ETL 작업 예제

다음 예제는 CSV 파일에서 데이터를 추출하고, 변환한 다음, JSON 파일로 저장하는 간단한 ETL 작업을 보여줍니다.

```python
import csv
import json
from marshmallow import Schema, fields

# 데이터 추출
def extract_data():
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
        return data

# 데이터 변환
class DataSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    email = fields.Email()

def transform_data(data):
    schema = DataSchema(many=True)
    transformed_data = schema.dump(data)
    return transformed_data

# 데이터 저장
def load_data(transformed_data):
    with open('output.json', 'w') as file:
        json.dump(transformed_data, file)

# ETL 작업 실행
data = extract_data()
transformed_data = transform_data(data)
load_data(transformed_data)
```

위 예제에서는 CSV 파일에서 데이터를 추출하는 `extract_data` 함수를 정의합니다. 추출한 데이터를 Marshmallow의 스키마를 사용하여 JSON 형식으로 변환하는 `transform_data` 함수를 정의합니다. 마지막으로 변환한 데이터를 JSON 파일로 저장하는 `load_data` 함수를 정의합니다.

이제 `ETL 작업 실행` 부분에서 위에서 정의한 함수들을 실행하면, CSV 파일에서 데이터를 추출하고, 변환한 후 JSON 파일로 저장합니다.

해당 예제는 Marshmallow를 이용하여 간단한 ETL 작업을 수행하는 방법을 보여줍니다. Marshmallow는 더 복잡한 변환 작업을 수행하기 위한 다양한 기능을 제공하므로, ETL 작업을 할 때 많은 도움이 될 수 있습니다.

## 참고 자료

- [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/)
- [ETL(Extract, Transform, Load)이란](https://en.wikipedia.org/wiki/Extract,_transform,_load)