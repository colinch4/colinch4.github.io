---
layout: post
title: "[python] SQLAlchemy와 Microsoft SQL Server 데이터베이스 연동"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Microsoft SQL Server는 인기있는 관계형 데이터베이스 관리 시스템(RDBMS) 중 하나입니다. SQLAlchemy는 파이썬에서 SQL 데이터베이스에 접근하기 위한 강력한 ORM(Object-Relational Mapping) 툴킷입니다. 이 글에서는 SQLAlchemy를 사용하여 Microsoft SQL Server 데이터베이스에 연결하는 방법을 알아보겠습니다.

## SQLAlchemy 설치

먼저, SQLAlchemy를 설치해야 합니다. 다음 명령을 사용하여 SQLAlchemy를 설치하세요.

```python
pip install SQLAlchemy
```

## Microsoft SQL Server 드라이버 설치

SQLAlchemy에서 Microsoft SQL Server와 연동하기 위해서는 해당 데이터베이스를 위한 드라이버를 설치해야 합니다. Python에서는 pyodbc라는 드라이버를 사용하여 Microsoft SQL Server에 연결할 수 있습니다.

다음 명령을 사용하여 pyodbc를 설치하세요.

```python
pip install pyodbc
```

## SQLAlchemy 연결 설정

SQLAlchemy를 사용하여 Microsoft SQL Server에 연결하기 위해서는 연결 문자열과 연결 엔진을 구성해야 합니다.

```python
from sqlalchemy import create_engine

# 연결 문자열
connection_string = 'mssql+pyodbc://<username>:<password>@<server_name>/<database_name>?driver=ODBC+Driver+17+for+SQL+Server'

# 연결 엔진 생성
engine = create_engine(connection_string)
```

위의 코드에서 `<username>`, `<password>`, `<server_name>`, `<database_name>`은 자신의 환경에 맞게 설정해야 합니다. 또한, ODBC 드라이버 버전을 정확히 지정해야 합니다.

## 데이터베이스에 연결하기

연결 엔진을 사용하여 데이터베이스에 연결할 수 있습니다.

```python
# 연결 엔진을 사용하여 연결
connection = engine.connect()

# SQL 쿼리 실행
result = connection.execute('SELECT * FROM <table_name>')

# 결과 출력
for row in result:
    print(row)

# 연결 종료
connection.close()
```

위의 코드에서 `<table_name>`은 데이터베이스에서 쿼리할 테이블의 이름으로 대체해야 합니다.

## SQLAlchemy 모델 정의

SQLAlchemy를 사용하면 데이터베이스의 테이블을 파이썬 클래스로 매핑할 수 있습니다. 다음은 SQLAlchemy 모델의 예입니다.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
```

위의 코드에서 `User` 클래스는 `users` 테이블과 매핑됩니다. 각 컬럼은 클래스의 속성으로 정의됩니다.

## 데이터 조회하기

저장된 데이터를 쿼리하기 위해서는 SQLAlchemy의 쿼리 기능을 사용할 수 있습니다. 다음은 데이터 조회의 예입니다.

```python
from sqlalchemy.orm import sessionmaker

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

# 모든 사용자 조회
users = session.query(User).all()

# 결과 출력
for user in users:
    print(user.name, user.age)

# 세션 종료
session.close()
```

위의 코드에서 `User` 클래스는 앞서 정의한 SQLAlchemy 모델입니다. `query()` 메서드를 사용하여 원하는 데이터를 조회할 수 있습니다.

## 결론

위의 방법을 사용하면 SQLAlchemy를 활용하여 Microsoft SQL Server 데이터베이스에 손쉽게 연결하고 데이터를 조회할 수 있습니다. SQLAlchemy의 강력한 ORM 툴킷을 사용하여 데이터베이스 작업을 더욱 편리하게 처리할 수 있습니다.

## 참고 자료

- SQLAlchemy 공식 문서: <https://docs.sqlalchemy.org/>
- pyodbc 패키지 문서: <https://github.com/mkleehammer/pyodbc>
- Microsoft ODBC 드라이버 다운로드: <https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server>