---
layout: post
title: "[python] Flask-RESTful과 JWT(JSON Web Token)를 이용한 인증 방법"
description: " "
date: 2023-11-30
tags: [python]
comments: true
share: true
---

Flask-RESTful은 파이썬 웹 프레임워크인 Flask를 확장하여 RESTful API를 쉽게 개발할 수 있는 도구입니다. JWT(JSON Web Token)는 API 인증에 사용되는 토큰 기반의 인증 방법입니다. 이번 블로그에서는 Flask-RESTful과 JWT를 함께 사용하여 API 인증을 구현하는 방법에 대해 알아보겠습니다.

## 목차
- [Flask-RESTful 설치](#flask-restful-설치)
- [JWT 패키지 설치](#jwt-패키지-설치)
- [JWT 설정](#jwt-설정)
- [API 인증 구현](#api-인증-구현)
- [토큰 검증 데코레이터](#토큰-검증-데코레이터)
- [API 예제](#api-예제)

## Flask-RESTful 설치

먼저 Flask-RESTful을 설치해야 합니다. 아래의 명령어를 사용하여 설치할 수 있습니다.

```bash
$ pip install flask-restful
```

## JWT 패키지 설치

JWT를 사용하기 위해 PyJWT 패키지를 설치해야 합니다. 아래의 명령어를 사용하여 설치할 수 있습니다.

```bash
$ pip install PyJWT
```

## JWT 설정

Flask-RESTful과 JWT를 함께 사용하기 위해 Flask의 환경 설정에 JWT 설정을 추가해야 합니다. 아래의 코드를 Flask 애플리케이션 설정 파일에 추가합니다.

```python
app.config['JWT_SECRET_KEY'] = 'secret-key'
```

JWT_SECRET_KEY는 토큰을 암호화하는 데 사용되는 비밀 키입니다.

## API 인증 구현

API 인증을 구현하기 위해 먼저 사용자 정보를 저장하고 관리하는 User 모델을 만들어야 합니다. 아래는 User 모델의 예시입니다.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
```

위의 예시에서는 SQLAlchemy를 사용하여 User 테이블을 생성하고 각각의 사용자는 고유한 username과 암호화된 password를 가지고 있습니다.

## 토큰 검증 데코레이터

API 요청 시 전달된 토큰을 검증하기 위해 데코레이터를 작성해야 합니다. 아래는 JWT 토큰 검증을 위한 데코레이터입니다.

```python
from flask_jwt import jwt_required, current_identity

@app.route('/protected')
@jwt_required()
def protected():
    return f'Hello, {current_identity.username}!'
```

## API 예제

아래는 JWT 인증을 사용한 API의 예제입니다.

```python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
api = Api(app)

# JWT 인증을 위한 사용자 정보 저장
users = [{'username': 'admin', 'password': 'admin'}]

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"User(id='{self.id}', username='{self.username}', password='****')"

user_objects = []
for index, user in enumerate(users):
    user_objects.append(User(index, user['username'], user['password']))

def authenticate(username, password):
    for user in user_objects:
        if user.username == username and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

def identity(payload):
    user_id = payload['identity']
    return User(user_id, '', '')

jwt = JWT(app, authenticate, identity)

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return f"Hello, {current_identity.username}!"

api.add_resource(ProtectedResource, '/protected')

if __name__ == '__main__':
    app.run(debug=True)
```

위의 예제는 `/protected` 경로로의 GET 요청이 인증된 사용자에게만 허용됩니다. 허용된 사용자는 요청 시 "Hello, 'username'!" 메시지를 받게 됩니다.

이상으로 Flask-RESTful과 JWT를 이용한 인증 방법에 대해 알아보았습니다. Flask-RESTful과 JWT를 함께 사용하면 보안적으로 안전한 API를 개발할 수 있습니다. 문제가 발생하면 레퍼런스 문서를 참조하십시오.