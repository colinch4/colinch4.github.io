---
layout: post
title: "[python] SQLAlchemy-Utils를 사용하여 Soft Deleted 모델 구현하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

소프트 삭제는 데이터를 영구적으로 삭제하지 않고 별도의 플래그나 컬럼을 사용하여 삭제된 상태를 표시하는 기술이다. SQLAlchemy-Utils 라이브러리를 사용하면 간편하게 소프트 삭제를 구현할 수 있다. 

## 1. SQLAlchemy-Utils 설치

먼저 SQLAlchemy-Utils 라이브러리를 설치해야 한다. pip를 사용하여 간편하게 설치할 수 있다.

```python
pip install sqlalchemy-utils
```

## 2. Soft Deleted 모델 구현

다음은 SQLAlchemy-Utils 라이브러리를 사용하여 Soft Deleted 모델을 구현하는 예제이다.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import Timestamp, soft_deletes

Base = declarative_base()

# 소프트 삭제를 위한 믹스인 클래스 적용
class SoftDeletedModel(Timestamp, soft_deletes.Deletable, Base):
    __abstract__ = True

# 실제 모델 정의
class User(SoftDeletedModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
```

위의 코드에서 `SoftDeletedModel` 클래스는 소프트 삭제를 위한 믹스인 클래스로 정의되었다. 그리고 `User` 클래스는 이 `SoftDeletedModel` 클래스를 상속받아 정의되었다.

## 3. Soft Deleted 모델 사용

Soft Deleted 모델을 사용할 때는 삭제되지 않은 데이터만을 조회해야 한다. SQLAlchemy-Utils를 사용하면 소프트 삭제된 데이터를 쉽게 필터링할 수 있다.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

# Soft deleted되지 않은 사용자만 조회
active_users = session.query(User).filter(User.deleted_at == None).all()
```

위의 코드에서 `User.deleted_at == None` 조건을 사용하여 소프트 삭제되지 않은 데이터만을 조회하고 있다.

Soft Deleted 모델을 구현하고 사용함으로써 데이터를 실수로 삭제하는 문제를 방지할 수 있으며, 데이터의 무결성을 유지할 수 있다.

Soft Deleted를 구현할 때 SQLAlchemy-Utils를 사용하면 간편하게 구현할 수 있으며, 복잡한 쿼리 작성 없이 간편하게 소프트 삭제된 데이터를 필터링할 수 있다.