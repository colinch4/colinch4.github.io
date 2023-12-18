---
layout: post
title: "[python] FastAPI와 elasticsearch-py를 이용한 검색 구현"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

본 포스트에서는 FastAPI와 elasticsearch-py를 사용하여 간단한 검색 기능을 구현하는 방법에 대해 알아보겠습니다.

## 목차

1. FastAPI 소개
2. Elasticsearch-py 소개
3. FastAPI 및 Elasticsearch-py를 사용한 검색 기능 구현
4. 결론

## 1. FastAPI 소개
FastAPI는 Python 3.6+의 빠르고(성능은 Starlette 및 Pydantic에 의해 제공됨), 쉽게 사용할 수 있는 웹 프레임워크입니다. FastAPI는 API를 구축하기 위한 간편한 기능을 제공하며, 높은 성능과 자동 문서화 기능을 지원합니다.

## 2. Elasticsearch-py 소개
elasticsearch-py는 공식 Elasticsearch Python 클라이언트로, Elasticsearch 데이터베이스와 상호작용하기 위한 기능을 제공합니다. Elasticsearch-py를 사용하면 Python 애플리케이션에서 Elasticsearch 인덱스를 만들고 관리하며, 데이터를 색인하고 검색할 수 있습니다.

## 3. FastAPI 및 Elasticsearch-py를 사용한 검색 기능 구현
다음은 FastAPI와 Elasticsearch-py를 사용하여 검색 기능을 구현하는 예제 코드입니다.

```python
from fastapi import FastAPI
from elasticsearch import Elasticsearch

app = FastAPI()
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

@app.get("/search")
async def search(q: str):
    res = es.search(index="my_index", body={"query": {"match": {"content": q}}})
    return res
```

위의 코드는 FastAPI를 사용하여 `/search` 엔드포인트를 만들고, 입력받은 검색어를 Elasticsearch에 전달하여 결과를 반환하는 기능을 구현한 것입니다.

## 4. 결론
본 포스트에서는 FastAPI와 elasticsearch-py를 사용하여 간단한 검색 기능을 구현하는 방법에 대해 살펴보았습니다. FastAPI와 Elasticsearch-py를 이용하면 빠르고 안정적인 검색 기능을 간단히 구현할 수 있으며, 이는 Python 기반의 웹 애플리케이션을 개발하는 데 유용한 방법 중 하나입니다.

>`참고문헌`:
>https://fastapi.tiangolo.com/  
>https://elasticsearch-py.readthedocs.io/