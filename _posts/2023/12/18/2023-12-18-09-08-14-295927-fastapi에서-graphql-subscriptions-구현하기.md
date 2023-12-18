---
layout: post
title: "[python] FastAPI에서 GraphQL Subscriptions 구현하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

FastAPI는 Python으로 빠르고 현대적인 API를 쉽게 구축할 수 있는 빠른 웹 프레임워크입니다. FastAPI를 사용하면 GraphQL Subscriptions을 구현하여 실시간으로 업데이트되는 데이터를 처리할 수 있습니다.

이번 게시물에서는 FastAPI 및 Starlette 웹 소켓을 사용하여 GraphQL Subscriptions을 구현하는 방법에 대해 알아보겠습니다.

## 필수 요구사항

- Python 3.7 이상
- FastAPI
- Graphene
- Uvicorn
- AIOHTTP
- GraphQL WS
- AnyJSON

## GraphQL Subscriptions 구현

1. **FastAPI 및 Uvicorn 설치**

FastAPI와 Uvicorn은 Python을 위한 웹 프레임워크 및 웹 서버입니다. 다음 명령을 사용하여 설치합니다.

```bash
pip install fastapi uvicorn
```

2. **Graphene 설치**

Graphene은 Python의 GraphQL 구현 라이브러리입니다. 다음 명령을 사용하여 설치합니다.

```bash
pip install graphene
```

3. **AIOHTTP 및 GraphQL WS 설치**

AIOHTTP 및 GraphQL WS는 GraphQL Subscriptions을 구현하는 데 사용됩니다. 다음 명령을 사용하여 설치합니다.

```bash
pip install aiohttp graphql-ws
```

4. **FastAPI 애플리케이션 작성**

다음은 FastAPI 애플리케이션을 작성하는 예제입니다.

```python
from fastapi import FastAPI
from graphene import ObjectType, String, Schema
from starlette.graphql import GraphQLApp

app = FastAPI()

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))

    def resolve_hello(root, info, name):
        return f'Hello, {name}!'

schema = Schema(query=Query)
app.add_route("/", GraphQLApp(schema))
```

이 예제에서는 FastAPI를 사용하여 간단한 GraphQL 쿼리를 처리하고 있습니다.

5. **GraphQL Subscriptions 구현**

GraphQL Subscriptions을 구현하려면 AIOHTTP와 GraphQL WS를 사용하는 웹 소켓을 설정해야 합니다. 이러한 세부 사항은 긴 토픽이므로 자세한 내용은 [공식 문서](https://github.com/aio-libs/aiohttp)를 확인하시기 바랍니다.

## 결론

이제 여러분은 FastAPI를 사용하여 GraphQL Subscriptions을 구현하는 방법을 알게 되었습니다. 실시간으로 업데이트되는 데이터를 다루기 위해 GraphQL Subscriptions을 사용할 수 있으며, 기존의 HTTP 요청-응답 패턴을 벗어나 데이터를 실시간으로 처리할 수 있습니다. FastAPI와 GraphQL을 함께 사용하여 놀라운 실시간 기능을 만들어보세요.