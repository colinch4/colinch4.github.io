---
layout: post
title: "FastAPI와 AWS DynamoDB를 연동하여 NoSQL 데이터베이스 사용하기"
description: " "
date: 2023-09-25
tags: [FastAPI, DynamoDB]
comments: true
share: true
---

NoSQL 데이터베이스는 관계형 데이터베이스와 달리 유연하고 확장 가능한 데이터 저장 방식을 제공합니다. 이번 포스트에서는 FastAPI와 AWS DynamoDB를 연동하여 NoSQL 데이터베이스를 사용하는 방법에 대해 알아보겠습니다.

## 1. AWS 계정 및 DynamoDB 설정

먼저, AWS 계정을 생성하고 AWS Management Console에 로그인합니다. DynamoDB 서비스를 선택하고, 새로운 테이블을 생성합니다. 테이블 이름과 기본 키를 설정해야합니다. DynamoDB에서는 기본 키로 파티션 키 또는 파티션 키와 정렬 키를 함께 사용할 수 있습니다. 이 예제에서는 단순하게 파티션 키만 사용하도록 하겠습니다.

## 2. FastAPI 프로젝트 설정

FastAPI를 사용하기 위해 Python 가상 환경을 설정하고, 필요한 패키지를 설치합니다. 가상 환경을 설정하는 방법은 생략하겠습니다.

```python
# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
```

위의 코드는 FastAPI 프로젝트의 `main.py` 파일에 작성되어 있는 예시입니다. 간단한 루트 엔드포인트를 정의하였습니다. 이제 FastAPI와 DynamoDB를 연동하여 데이터베이스를 사용해보겠습니다.

## 3. Boto3를 사용하여 DynamoDB 연동하기

Boto3는 파이썬에서 AWS 서비스를 사용하기 위한 SDK입니다. 먼저 Boto3를 설치합니다.

```shell
pip install boto3
```

그리고 다음과 같이 DynamoDB와 연동할 코드를 작성합니다.

```python
# main.py

import boto3

ddb = boto3.resource('dynamodb', region_name='YOUR_AWS_REGION')
table = ddb.Table('YOUR_DYNAMODB_TABLE_NAME')

@app.get("/items/{item_id}")
async def get_item(item_id: str):
    response = table.get_item(Key={'id': item_id})
    item = response.get('Item')
    return item
```

위의 코드에서 `YOUR_AWS_REGION`은 AWS 리전(region)의 이름을, `YOUR_DYNAMODB_TABLE_NAME`은 DynamoDB 테이블의 이름을 각각 적절하게 지정해야 합니다. 

이제 `/items/{item_id}` 엔드포인트를 통해 `item_id`에 해당하는 항목을 가져오는 API를 만들었습니다. DynamoDB의 `get_item` 함수를 사용하여 해당 항목을 검색하고 반환합니다.

## 4. 테스트하기

이제 FastAPI 앱을 실행하고, `/items/{item_id}` 엔드포인트에 요청해보겠습니다.

```shell
uvicorn main:app --reload
```

FastAPI가 정상적으로 실행되었다면, 브라우저 또는 API 테스트 도구를 통해 `/items/{item_id}` 엔드포인트에 GET 요청을 보내면 DynamoDB에서 해당 항목을 가져와 반환하는 것을 확인할 수 있습니다.

## 결론

이번 포스트에서는 FastAPI와 AWS DynamoDB를 연동하여 NoSQL 데이터베이스를 활용하는 방법에 대해 알아보았습니다. Boto3를 사용하여 DynamoDB와의 연결을 설정하고, FastAPI에서 해당 데이터를 검색하는 API를 생성했습니다. 이를 통해 NoSQL 데이터베이스를 활용하여 유연하고 확장 가능한 애플리케이션을 개발할 수 있습니다.

#FastAPI #DynamoDB #NoSQL