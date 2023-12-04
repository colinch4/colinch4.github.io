---
layout: post
title: "[python] Marshmallow와 Flask를 함께 사용하여 RESTful API 개발하는 방법"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

이번 포스트에서는 Marshmallow와 Flask를 함께 사용하여 RESTful API를 개발하는 방법에 대해 알아보겠습니다. Marshmallow는 Python 데이터 직렬화 및 유효성 검사 라이브러리이며, Flask는 유연하고 간결한 웹 프레임워크입니다. 이 두 가지를 결합하여 데이터를 직렬화하고 API 엔드포인트에서 유효성을 검사할 수 있습니다.

## 1. 프로젝트 설정

처음으로, Flask와 Marshmallow를 설치해야 합니다. 아래의 명령어를 사용하여 설치합니다.

```shell
pip install flask marshmallow
```

## 2. 모델 정의

RESTful API에서 사용할 데이터 모델을 정의해야 합니다. 예를 들어, 간단한 사용자 모델을 만들어 보겠습니다. `User` 클래스를 만들고 Marshmallow 스키마를 사용하여 데이터를 직렬화합니다.

```python
from marshmallow import Schema, fields

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
```

## 3. API 엔드포인트 작성

Flask를 사용하여 API 엔드포인트를 작성합니다. 아래의 예제는 사용자를 생성할 수 있는 엔드포인트입니다. POST 요청으로 사용자 정보를 전달하면, Marshmallow 스키마를 사용하여 유효성을 검사한 뒤, 사용자를 생성합니다.

```python
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    user_schema = UserSchema()
    errors = user_schema.validate(request.json)
    
    if errors:
        return jsonify(errors), 400
    
    user = User(id=1, **request.json)
    
    # 데이터베이스에 사용자를 저장하는 로직
    # ...

    return jsonify(user_schema.dump(user)), 201

if __name__ == '__main__':
    app.run()
```

## 4. API 서버 실행

API 서버를 실행하기 위해 아래의 명령어를 사용합니다.

```shell
python app.py
```

## 결론

이번 포스트에서는 Marshmallow와 Flask를 사용하여 RESTful API를 개발하는 방법에 대해 알아보았습니다. Marshmallow는 데이터 직렬화 및 유효성 검사를 위한 강력한 라이브러리이며, Flask는 간단하고 효율적인 웹 프레임워크입니다. 이 두 가지를 함께 사용하면 간단하고 유연한 RESTful API를 개발할 수 있습니다.

더 자세한 정보를 원한다면, 아래의 공식 문서를 참조하세요.

- [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/)
- [Flask 공식 문서](https://flask.palletsprojects.com/)