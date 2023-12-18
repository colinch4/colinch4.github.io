---
layout: post
title: "[python] FastAPI와 Apache Cassandra의 연동"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

FastAPI는 빠르고 쉽게 API를 작성할 수 있는 파이썬 웹 프레임워크이며, Apache Cassandra는 분산형 NoSQL 데이터베이스 시스템입니다. 이 블로그 글에서는 FastAPI와 Apache Cassandra를 연동하여 데이터를 읽고 쓰는 방법에 대해 알아보겠습니다.

## 1. Apache Cassandra 설치 및 설정

먼저, Apache Cassandra를 설치하고 설정해야 합니다. [공식 웹사이트](https://cassandra.apache.org/)에서 Apache Cassandra를 다운로드하고 설치하는 방법을 참고할 수 있습니다.

## 2. FastAPI 프로젝트 설정

FastAPI 프로젝트를 설정하고 FastAPI와 Apache Cassandra를 연동하기 위해 `cassandra-driver`를 사용합니다.

```python
pip install fastapi
pip install cassandra-driver
```

## 3. Apache Cassandra 연결

FastAPI 앱 내에서 Cassandra와의 연결을 설정합니다.

```python
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
```

## 4. 데이터 읽기 및 쓰기

FastAPI 엔드포인트에서 Cassandra 데이터베이스를 읽기 및 쓰기 위해 다음과 같이 쿼리를 작성합니다.

```python
from fastapi import FastAPI
from cassandra.cluster import Cluster

app = FastAPI()
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

@app.get("/user/{user_id}")
async def read_user(user_id: int):
    query = f"SELECT * FROM users WHERE id={user_id}"
    result = session.execute(query)
    for row in result:
        return {"name": row.name, "email": row.email}
    return {"error": "User not found"}

@app.post("/user/{user_id}")
async def create_user(user_id: int, name: str, email: str):
    query = f"INSERT INTO users (id, name, email) VALUES ({user_id}, '{name}', '{email}')"
    session.execute(query)
    return {"message": "User created successfully"}
```

위의 예시 코드에서는 FastAPI 앱과 Apache Cassandra를 연동하여 사용자 정보를 읽고 쓰는 간단한 기능을 구현한 것입니다.

## 결론

이제 FastAPI와 Apache Cassandra를 연동하여 데이터베이스를 활용하는 방법에 대해 알아보았습니다. FastAPI의 빠른 속도와 Cassandra의 분산형 특성을 활용하면 더욱 효율적인 웹 애플리케이션을 구축할 수 있을 것입니다. FastAPI와 Apache Cassandra를 함께 사용하여 더욱 강력한 애플리케이션을 개발해보세요!