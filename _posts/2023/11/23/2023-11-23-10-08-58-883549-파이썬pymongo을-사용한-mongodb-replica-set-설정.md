---
layout: post
title: "[python] 파이썬(PyMongo)을 사용한 MongoDB Replica Set 설정"
description: " "
date: 2023-11-23
tags: [python]
comments: true
share: true
---

이 블로그 포스트에서는 파이썬과 PyMongo를 사용하여 MongoDB Replica Set을 설정하는 방법에 대해 알아보겠습니다.

## Replica Set이란?

MongoDB Replica Set은 데이터베이스 서버의 고가용성을 제공하기 위해 사용되는 기능입니다. Replica Set은 여러 MongoDB 서버로 구성되어 있으며, 주 서버(Primary)와 여러 개의 보조 서버(Secondary)로 구성됩니다. 주 서버에 작성된 데이터는 보조 서버로 복제되어 데이터 손실 및 서비스 중단을 방지합니다.

## Replica Set 설정하기

1. MongoDB 서버 설치 및 Replica Set 구성
   - MongoDB 서버를 설치하고 실행합니다.
   - `mongo` 셸에서 다음 명령을 실행하여 Replica Set 구성을 시작합니다.
     ```shell
     > rs.initiate()
     ```

2. 파이썬과 PyMongo 설치
   - 파이썬과 PyMongo 패키지를 설치합니다.
   - `pip`를 사용하여 다음 명령으로 설치할 수 있습니다.
     ```shell
     $ pip install pymongo
     ```

3. 파이썬 코드 작성
   - 다음은 PyMongo를 사용하여 Replica Set에 연결하고 데이터를 쓰고 읽는 간단한 예제 코드입니다.

     ```python
     import pymongo

     # Replica Set의 주소
     mongo_address = "mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=myReplicaSet"

     # Replica Set에 연결
     client = pymongo.MongoClient(mongo_address)
     db = client.myDatabase

     # 데이터 쓰기
     doc = {"name": "John", "age": 30}
     db.myCollection.insert_one(doc)

     # 데이터 읽기
     result = db.myCollection.find_one({"name": "John"})
     print(result)
     ```

     위의 코드에서는 Replica Set의 주소를 `mongo_address` 변수에 설정하고, `pymongo.MongoClient`를 사용하여 Replica Set에 연결합니다. 데이터를 쓰기 위해 `insert_one` 메서드를 사용하고, 데이터를 읽기 위해 `find_one` 메서드를 사용합니다.

이제 파이썬 코드를 실행하여 Replica Set에 연결하고 데이터를 조작할 수 있습니다.

## 마무리

이번에는 파이썬과 PyMongo를 사용하여 MongoDB Replica Set을 설정하는 방법에 대해 알아보았습니다. Replica Set을 구성하면 MongoDB 데이터베이스의 고가용성을 확보할 수 있으며, PyMongo를 통해 간편하게 데이터를 조작할 수 있습니다.

더 자세한 정보와 옵션에 대해서는 [PyMongo 공식 문서](https://pymongo.readthedocs.io/)를 참고해 주세요.