---
layout: post
title: "[python] SQLAlchemy와 ORM(Object-Relational Mapping)"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

SQLAlchemy는 파이썬에서 사용하는 ORM(Object-Relational Mapping) 라이브러리로, 데이터베이스와의 상호작용을 더 편리하게 만들어줍니다. ORM은 객체와 관계형 데이터베이스 간의 매핑을 담당하여 객체지향 프로그래밍 언어에서 데이터베이스를 사용하기 위한 작업을 추상화합니다.

## ORM의 장점

ORM의 가장 큰 장점은 객체와 데이터베이스 간의 추상화로 인해 개발자가 데이터베이스의 저수준 작업을 직접 다루지 않아도 된다는 것입니다. ORM을 사용하면 SQL 쿼리를 직접 작성하지 않고도 객체를 통해 데이터베이스에 접근할 수 있습니다. 이로 인해 개발자는 데이터베이스에 더 집중하는 것이 아니라 비즈니스 로직에 더 집중할 수 있습니다.

또한, ORM은 데이터베이스에 대한 접근을 추상화하기 때문에 데이터베이스 간의 이식성이 높아집니다. 즉, ORM을 사용하면 애플리케이션을 한 데이터베이스에서 다른 데이터베이스로 쉽게 이관할 수 있습니다. 예를 들어, SQLite에서 개발한 애플리케이션을 MySQL로 이관할 때 ORM을 사용하면 데이터베이스의 변경에 따른 코드의 수정을 최소화할 수 있습니다.

## SQLAlchemy의 기능

SQLAlchemy는 많은 유용한 기능을 제공합니다. 다음은 SQLAlchemy의 일부 기능입니다.

### 객체간의 관계 매핑

ORM은 개발자가 클래스와 그에 대응하는 데이터베이스 테이블 간의 관계를 정의할 수 있도록 해줍니다. SQLAlchemy는 이 관계를 매핑하기 위한 데코레이터, 관계 필드 등 다양한 도구를 제공합니다. 예를 들어, `One-to-One`, `One-to-Many`, `Many-to-Many` 등의 관계를 쉽게 정의할 수 있습니다.

### 데이터베이스 마이그레이션

데이터베이스 스키마의 변경은 애플리케이션의 업데이트 과정에서 필수적입니다. SQLAlchemy는 데이터베이스 스키마 변경을 추적하고 이를 자동으로 적용해주는 마이그레이션 도구인 Alembic을 제공합니다. 이를 통해 데이터베이스 스키마 변경에 따른 코드 수정 및 적용 과정을 간편하게 처리할 수 있습니다.

### 쿼리 작성

SQLAlchemy는 객체를 통해 쿼리를 작성할 수 있는 기능을 제공합니다. 이를 통해 SQL을 직접 작성하지 않고도 데이터베이스에 대한 다양한 작업을 수행할 수 있습니다. SQLAlchemy의 쿼리 작성 기능은 다양한 필터링, 정렬, 집계 기능 등을 제공하여 유연하고 효율적인 쿼리 작성을 가능하게 합니다.

## 참고 자료

- SQLAlchemy 공식 문서: [https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)
- SQLAlchemy 튜토리얼: [https://docs.sqlalchemy.org/en/14/orm/tutorial.html](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- SQLAlchemy ORM 자습서: [https://docs.sqlalchemy.org/en/14/orm/tutorial.html](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)

---
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 데이터베이스 연결 설정
engine = create_engine("sqlite:///test.db")

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

# 모델 정의
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
Base.metadata.create_all(engine)

# 데이터 추가
user = User(name='John', age=25)
session.add(user)
session.commit()

# 데이터 조회
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# 데이터 수정
user.name = 'Jane'
session.commit()

# 데이터 삭제
session.delete(user)
session.commit()
```

위의 예시 코드에서는 SQLAlchemy를 사용하여 SQLite 데이터베이스에 데이터를 추가, 조회, 수정 및 삭제하는 방법을 보여줍니다. SQLAlchemy는 다양한 데이터베이스와 호환되며, 위의 예시 코드에서 `create_engine()` 함수의 매개변수를 변경하여 다른 데이터베이스에 연결할 수 있습니다.
```