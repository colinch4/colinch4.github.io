---
layout: post
title: "[python] Marshmallow를 사용하여 GraphQL API 개발하는 방법"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

GraphQL은 데이터 쿼리 및 조작 언어입니다. Marshmallow는 Python에서 직렬화 및 역직렬화를 위한 라이브러리입니다. 이 블로그 포스트에서는 Marshmallow를 사용하여 GraphQL API를 개발하는 방법을 살펴보겠습니다.

## 필수 패키지 설치

먼저, 프로젝트에 Marshmallow와 그래프큐엘 관련 패키지를 설치해야 합니다. 아래 명령어를 사용하여 설치합니다.

```
pip install marshmallow graphene
```

## 스키마 정의

다음으로, GraphQL 스키마를 정의해야 합니다. 스키마는 GraphQL API에서 제공할 수 있는 쿼리 및 뮤테이션의 타입과 구조를 정의합니다. 아래는 예제 스키마입니다.

```python
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return "Hello, World!"

schema = Schema(query=Query)
```

## 직렬화 및 역직렬화

GraphQL API에서는 데이터를 직렬화하여 응답으로 전송하거나, 클라이언트로부터 받은 데이터를 역직렬화하여 처리해야 합니다. Marshmallow는 이러한 직렬화 및 역직렬화 작업을 쉽게 수행할 수 있도록 도와줍니다.

아래는 Marshmallow를 사용하여 간단한 직렬화 및 역직렬화를 수행하는 예제입니다.

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.String()
    age = fields.Integer()

# 직렬화
user = {"name": "John Doe", "age": 25}
user_schema = UserSchema()
serialized_user = user_schema.dump(user)
print(serialized_user)

# 역직렬화
deserialized_user = user_schema.load(serialized_user)
print(deserialized_user)
```

## GraphQL 리졸버 작성

GraphQL 리졸버는 GraphQL 스키마의 각 필드에 대한 실제 로직을 작성하는 곳입니다. 예를 들어, `hello` 필드의 경우 "Hello, World!"를 반환하는 로직을 작성해야 합니다.

```python
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return "Hello, World!"

schema = Schema(query=Query)
```

## Flask를 사용하여 GraphQL API 실행

마지막으로, Flask를 사용하여 GraphQL API를 실행할 수 있습니다. 아래는 Flask 애플리케이션에서 GraphQL API를 실행하는 예제 코드입니다.

```python
from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run()
```

위 코드에서 `/graphql` 엔드포인트로 접근하면 GraphQL API를 사용할 수 있습니다. 또한, `graphiql=True` 옵션을 사용하면 그래픽 사용자 인터페이스를 통해 쿼리를 작성하고 실행할 수 있습니다.

## 결론

이제 Marshmallow를 사용하여 GraphQL API를 개발하는 방법을 살펴보았습니다. Marshmallow는 직렬화 및 역직렬화 작업을 단순화하여 개발자가 GraphQL API를 쉽게 구축할 수 있게 도와줍니다.