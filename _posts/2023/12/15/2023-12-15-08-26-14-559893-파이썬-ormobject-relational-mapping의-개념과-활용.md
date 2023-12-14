---
layout: post
title: "[python] 파이썬 ORM(Object-Relational Mapping)의 개념과 활용"
description: " "
date: 2023-12-15
tags: [python]
comments: true
share: true
---

## 목차

1. [ORM이란?](#ORM이란)
2. [ORM의 장점](#ORM의-장점)
3. [파이썬에서의 ORM 활용](#파이썬에서의-ORM-활용)
4. [결론](#결론)

---

## ORM이란?

ORM은 객체와 관계형 데이터베이스 간의 매핑을 의미합니다. 이를 통해 데이터베이스 테이블의 레코드와 객체지향 프로그래밍 언어의 객체 간의 변환을 자동화할 수 있습니다.

이것은 데이터베이스 쿼리 작성과 객체 지향 프로그래밍을 결합하여, 데이터베이스 스키마를 직접 다루지 않고도 데이터베이스에 접근할 수 있게 해줍니다.

---

## ORM의 장점

1. **객체지향적 접근**: ORM을 사용하면 데이터베이스 레코드를 객체로 쉽게 다룰 수 있습니다. 이것은 코드를 읽고 이해하기 쉽게 만들어줍니다.
2. **데이터베이스 독립성**: ORM을 사용하면 서로 다른 종류의 데이터베이스 시스템 간에 쉽게 전환할 수 있습니다. ORM은 데이터베이스와의 연결 부분을 캡슐화하므로, 데이터베이스 전환 시 변경해야 할 부분을 최소화합니다.
3. **반복적 작업 최소화**: ORM을 사용하면 CRUD(Create, Read, Update, Delete) 작업을 자동화하여 개발 시간을 단축시킬 수 있습니다.

---

## 파이썬에서의 ORM 활용

파이썬에서 ORM을 활용하기 위해서는 주로 Django나 SQLAlchemy와 같은 ORM 라이브러리를 사용합니다.

```python
# Django ORM 예시
from myapp.models import *
qs = MyModel.objects.filter(name="example")
for obj in qs:
    print(obj)
```

```python
# SQLAlchemy ORM 예시
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mymodel import MyModel, Base

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
example = MyModel(name="example")
session.add(example)
session.commit()
```

---

## 결론

ORM은 객체지향적인 접근으로 데이터베이스를 관리할 수 있게 해주어 개발과 유지보수를 더 효율적으로 만들어 줍니다. 파이썬에서 ORM을 사용하면 데이터베이스와의 상호작용을 더 쉽게 다룰 수 있으며, 개발 생산성을 높일 수 있습니다.