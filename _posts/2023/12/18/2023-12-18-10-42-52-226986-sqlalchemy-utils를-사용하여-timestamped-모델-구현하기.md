---
layout: post
title: "[python] SQLAlchemy-Utils를 사용하여 Timestamped 모델 구현하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

SQLAlchemy는 Python에서 사용되는 강력한 ORM(Object-Relational Mapping) 라이브러리입니다. SQLAlchemy를 보완하는 유용한 확장 라이브러리 중 하나인 SQLAlchemy-Utils는 다양한 유틸리티 및 데이터 유효성 검사를 제공하여 개발 과정을 간소화합니다.

이번에는 SQLAlchemy-Utils를 사용하여 Timestamped 모델을 구현해보겠습니다. Timestamped 모델은 생성일 및 수정일을 자동으로 관리하는 모델입니다. 데이터베이스 테이블에는 `created_at` 및 `updated_at` 필드가 필요하며, 이러한 필드는 생성 및 업데이트 시 자동으로 관리됩니다.

### 1. SQLAlchemy-Utils 설치하기
먼저, SQLAlchemy-Utils를 설치해야 합니다. 다음 명령을 사용하여 설치합니다:

```bash
pip install sqlalchemy-utils
```

### 2. Timestamped 모델 구현하기

아래는 SQLAlchemy-Utils를 사용하여 Timestamped 모델을 구현하는 예제입니다. `Timestamped` 클래스를 생성하고, 이를 상속받는 모델에서 Timestamped 모델의 속성을 이용할 수 있습니다.

```python
from sqlalchemy import Column, Integer
from sqlalchemy_utils import Timestamp

class Timestamped:
  created_at = Column(TZDateTime, default=now)
  updated_at = Column(TZDateTime, default=now, onupdate=now)

class YourModel(Base, Timestamped):
  __tablename__ = 'your_model'
  id = Column(Integer, primary_key=True)
  # 다른 필드 추가
```

위 예제에서 `Timestamped` 클래스는 `created_at` 및 `updated_at` 필드를 선언하고, 이를 상속받는 `YourModel` 클래스는 이러한 필드를 이용할 수 있습니다.

### 3. 사용 예제

Timestamped 모델을 사용하면 다음과 같이 손쉽게 생성일 및 수정일을 관리할 수 있습니다.

```python
# 새로운 모델 인스턴스 생성
new_model = YourModel()
session.add(new_model)
session.commit()

# 모델 업데이트
new_model.some_property = 'updated value'
session.commit()
```

### 결론
SQLAlchemy-Utils를 사용하여 Timestamped 모델을 구현하면 데이터베이스 모델의 생성일 및 수정일을 자동으로 관리할 수 있습니다. 이를 통해 개발자는 더 간편하게 데이터의 히스토리를 추적하고 관리할 수 있습니다.

더 많은 SQLAlchemy-Utils의 유틸리티 및 기능을 탐색하여 다양한 기능을 활용해보시기 바랍니다.

---
참고 문헌:
- [SQLAlchemy-Utils 공식 문서](https://sqlalchemy-utils.readthedocs.io/en/latest/)
- [SQLAlchemy 공식 문서](https://www.sqlalchemy.org/)