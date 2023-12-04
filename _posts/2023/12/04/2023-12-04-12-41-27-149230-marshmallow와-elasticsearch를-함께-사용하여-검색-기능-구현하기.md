---
layout: post
title: "[python] Marshmallow와 Elasticsearch를 함께 사용하여 검색 기능 구현하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

마샬로우(Marshmallow)는 파이썬의 객체 직렬화 라이브러리입니다. 엘라스틱서치(Elasticsearch)는 분산 검색 및 분석 엔진입니다. 이번 글에서는 마샬로우와 엘라스틱서치를 함께 사용하여 데이터를 검색하는 기능을 구현하는 방법을 알아보겠습니다.

## 1. 마샬로우(Marshmallow) 모델 정의하기

우선 검색할 데이터를 제공하는 마샬로우 모델을 정의해야 합니다. 예를 들어, 사용자(User) 객체를 다음과 같이 정의해보겠습니다.

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Email()
    bio = fields.Str()
```

위 코드에서는 사용자의 id, 이름, 이메일, 소개 등의 속성을 정의합니다.

## 2. 엘라스틱서치(Elasticsearch) 인덱스 설정하기

검색 기능을 사용하기 위해 먼저 엘라스틱서치에 인덱스를 설정해야 합니다. 간단히 말해, 엘라스틱서치에 데이터를 저장하고 인덱싱하는 방법을 설정하는 것입니다.

```python
from elasticsearch import Elasticsearch

es = Elasticsearch()

index_name = "users"

index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "keyword"},
            "email": {"type": "keyword"},
            "bio": {"type": "text"}
        }
    }
}

es.indices.create(index=index_name, body=index_settings)
```

위 코드에서는 `users`라는 인덱스를 생성하고, 사용자의 id, 이름, 이메일, 소개에 대한 타입을 정의합니다.

## 3. 데이터 인덱싱하기

마샬로우 모델을 사용하여 데이터를 엘라스틱서치에 인덱싱해보겠습니다.

```python
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "bio": "Welcome to my profile!"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "bio": "Hello, I'm Jane!"}
]

for user in users:
    es.index(index=index_name, body=user)
```

위 코드에서는 두 명의 사용자 데이터를 `users` 인덱스에 인덱싱합니다.

## 4. 데이터 검색하기

이제 마샬로우와 엘라스틱서치를 사용하여 데이터를 검색해보겠습니다.

```python
from marshmallow.utils import pprint

# 사용자 이름이 "John"인 사용자 검색
search_query = {
    "query": {
        "match": {
            "name": "John"
        }
    }
}

response = es.search(index=index_name, body=search_query)
pprint(response)
```

위의 예시는 사용자 이름이 "John"인 사용자를 검색하는 방법을 보여줍니다. 검색 결과는 `response` 변수에 저장되고, `pprint()` 함수를 통해 보기 좋게 출력됩니다.

## 결론

이번 글에서는 마샬로우와 엘라스틱서치를 함께 사용하여 데이터 검색 기능을 구현하는 방법을 살펴보았습니다. 마샬로우를 사용하여 데이터를 직렬화하고, 엘라스틱서치를 사용하여 데이터를 검색하고 인덱싱하는 방법을 배웠습니다. 이러한 방법을 응용하여 다양한 검색 기능을 구현할 수 있습니다.

## 참고 자료
- [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/en/stable/)
- [Elasticsearch 공식 문서](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)