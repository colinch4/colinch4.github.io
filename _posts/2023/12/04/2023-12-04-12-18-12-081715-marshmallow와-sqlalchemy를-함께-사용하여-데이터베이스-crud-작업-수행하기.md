---
layout: post
title: "[python] Marshmallow와 SQLAlchemy를 함께 사용하여 데이터베이스 CRUD 작업 수행하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

## 서론

데이터베이스의 CRUD 작업은 대부분의 애플리케이션에서 기본적으로 수행해야하는 작업입니다. 이를 효율적으로 처리하기 위해 Marshmallow와 SQLAlchemy를 함께 사용할 수 있습니다. Marshmallow는 객체 직렬화 및 역직렬화를 위한 Python 라이브러리이며, SQLAlchemy는 Python에서 가장 인기 있는 ORM(Object-Relational Mapping) 라이브러리입니다. 이번 블로그 포스트에서는 Marshmallow와 SQLAlchemy를 사용하여 데이터베이스 CRUD 작업을 수행하는 방법을 알아보겠습니다.

## 필수 패키지 설치

먼저 프로젝트에 필요한 패키지를 설치해야합니다. 아래의 명령어를 사용하여 Marshmallow와 SQLAlchemy를 설치하세요.

```shell
pip install marshmallow sqlalchemy
```

## 모델 정의하기

데이터베이스의 테이블과 매핑될 모델을 정의해야합니다. SQLAlchemy를 사용하여 모델을 정의하고 Marshmallow를 사용하여 직렬화 및 역직렬화를 위한 스키마를 생성합니다. 예를 들어, 'User'라는 테이블과 매핑될 'User' 모델을 정의해보겠습니다.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from marshmallow import Schema, fields

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Email()
```

## 데이터베이스 연결 설정

데이터베이스와의 연결 설정을 위해 SQLAlchemy의 `create_engine` 함수를 사용하여 연결을 설정해야합니다. 예를 들어, SQLite 데이터베이스와의 연결을 설정하는 방법은 다음과 같습니다.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite 데이터베이스와의 연결 설정
engine = create_engine('sqlite:///mydatabase.db')

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()
```

## 데이터 생성하기

Marshmallow 스키마를 사용하여 데이터를 생성할 수 있습니다. 예를 들어, 다음과 같이 User 모델과 UserSchema를 사용하여 새로운 사용자를 생성하는 방법을 알아보겠습니다.

```python
# 새로운 사용자 생성
new_user_data = {
    "username": "john",
    "email": "john@example.com"
}
user_schema = UserSchema()
new_user = user_schema.load(new_user_data, session=session)
session.add(new_user)
session.commit()
```

## 데이터 조회하기

데이터베이스에서 데이터를 조회하려면 SQLAlchemy를 사용하여 쿼리를 작성해야합니다. 예를 들어, 모든 사용자를 조회하는 방법은 다음과 같습니다.

```python
# 모든 사용자 조회
users = session.query(User).all()

# 사용자 스키마를 사용하여 결과 직렬화
users_schema = UserSchema(many=True)
result = users_schema.dump(users)

print(result)
```

## 데이터 업데이트하기

데이터를 업데이트하려면 먼저 해당 데이터를 조회한 다음에 업데이트할 값을 설정하고 커밋해야합니다. 예를 들어, 사용자의 이메일 주소를 업데이트하는 방법은 다음과 같습니다.

```python
# 사용자 조회
user = session.query(User).filter_by(username='john').first()

# 이메일 주소 업데이트
user.email = 'new_email@example.com'
session.commit()
```

## 데이터 삭제하기

데이터를 삭제하려면 먼저 해당 데이터를 조회한 다음에 `session.delete()` 메서드를 사용하여 삭제해야합니다. 예를 들어, 사용자를 삭제하는 방법은 다음과 같습니다.

```python
# 사용자 조회
user = session.query(User).filter_by(username='john').first()

# 사용자 삭제
session.delete(user)
session.commit()
```

## 결론

Marshmallow와 SQLAlchemy를 함께 사용하면 데이터베이스 CRUD 작업을 쉽게 처리할 수 있습니다. Marshmallow 스키마를 사용하여 데이터 직렬화 및 유효성 검사를 수행하고 SQLAlchemy를 사용하여 데이터베이스와의 상호 작용을 처리 할 수 있습니다. 이를 통해 데이터베이스 작업을 효과적으로 처리할 수 있으며, 코드의 가독성과 유지 보수성을 향상시킬 수 있습니다.

## 참고 자료

- [Marshmallow 문서](https://marshmallow.readthedocs.io/)
- [SQLAlchemy 문서](https://docs.sqlalchemy.org/)