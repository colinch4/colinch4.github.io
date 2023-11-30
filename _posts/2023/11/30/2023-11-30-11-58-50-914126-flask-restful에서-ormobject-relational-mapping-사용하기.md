---
layout: post
title: "[python] Flask-RESTful에서 ORM(Object-Relational Mapping) 사용하기"
description: " "
date: 2023-11-30
tags: [python]
comments: true
share: true
---

Flask-RESTful은 Flask 프레임워크를 이용하여 RESTful API를 개발할 수 있는 훌륭한 도구입니다. 이번 글에서는 Flask-RESTful을 사용하면서 ORM(Object-Relational Mapping)을 어떻게 사용할 수 있는지 알아보겠습니다.

## ORM이란?

ORM은 객체와 관계형 데이터베이스 간의 매핑을 담당하는 기술입니다. 이를 통해 데이터베이스의 테이블과 연결된 클래스를 사용하여 데이터를 조작할 수 있게 됩니다. ORM을 사용하면 SQL 쿼리를 직접 작성하는 것보다 더 직관적이고 간편하게 데이터베이스를 다룰 수 있습니다.

## SQLAlchemy를 사용한 ORM 설정

Flask-RESTful에서 ORM으로 SQLAlchemy를 지원합니다. SQLAlchemy는 강력하고 유연한 ORM 라이브러리로, 다양한 데이터베이스 시스템과 호환됩니다. SQLAlchemy를 Flask-RESTful 프로젝트에 통합하기 위해 다음과 같이 설정해야 합니다.

1. 필요한 패키지 설치하기

```python
pip install flask_sqlalchemy
```

2. Flask 앱에서 SQLAlchemy 활성화하기

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
```

위 코드는 Flask 앱 객체를 생성하고, 데이터베이스 연결을 위한 URI를 설정하며, SQLAlchemy를 초기화하는 코드입니다. 데이터베이스 URI는 실제 사용하는 데이터베이스에 맞게 변경해야 합니다.

## 모델 클래스 정의하기

SQLAlchemy를 사용하여 데이터베이스와 연결된 클래스인 모델 클래스를 정의해야 합니다. 이 클래스는 데이터베이스 테이블과 매핑되며, 데이터 조작을 위한 메서드를 가지고 있습니다. 예를 들어, 다음과 같은 사용자 모델 클래스를 정의할 수 있습니다.

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

위 코드는 `User` 클래스를 생성하고, `id`, `username`, `email` 등의 속성을 정의한 것입니다. `db.Model` 클래스를 상속받아 데이터베이스 모델로 만들었으며, `__repr__` 메서드를 사용하여 객체를 문자열로 표현할 수 있도록 했습니다.

## API 엔드포인트 작성하기

ORM과 Flask-RESTful을 함께 사용하여 API 엔드포인트를 작성할 수 있습니다. Flask-RESTful의 `Resource` 클래스를 상속받아 엔드포인트를 정의하고, 이를 데이터베이스 모델과 연결하여 데이터를 조작할 수 있습니다. 예를 들어, 다음과 같이 사용자 목록을 반환하는 엔드포인트를 작성할 수 있습니다.

```python
from flask_restful import Resource

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.username for user in users]
```

위 코드는 `UserListResource` 클래스를 생성하고, `get` 메서드를 작성한 것입니다. `User` 클래스의 `query` 속성을 사용하여 모든 사용자를 조회하고, 사용자 이름만을 반환합니다.

## 결론

Flask-RESTful에서 ORM을 사용하여 데이터베이스와의 상호작용을 간편하게 할 수 있습니다. SQLAlchemy를 사용하여 ORM을 설정하고, 모델 클래스를 정의하여 데이터베이스와 매핑하며, API 엔드포인트에서 ORM을 활용할 수 있습니다. ORM을 통해 데이터베이스 조작을 더 쉽고 직관적으로 할 수 있으며, Flask-RESTful과의 통합으로 RESTful API 개발을 보다 효율적으로 이룰 수 있습니다.

참고: [Flask-RESTful documentation](https://flask-restful.readthedocs.io/)