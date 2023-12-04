---
layout: post
title: "[python] Marshmallow와 OpenAPI(Swagger)를 함께 사용하여 API 문서화하는 방법"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

이번 포스트에서는 Marshmallow와 OpenAPI(Swagger)를 함께 사용해서 Python으로 작성된 REST API를 문서화하는 방법에 대해 알아보겠습니다.

## Marshmallow 소개
Marshmallow는 Python의 직렬화와 역직렬화를 위한 라이브러리입니다. 데이터를 JSON 형식으로 직렬화하고, 역직렬화 할 수 있게 해주며, 데이터 유효성 검사 등의 기능도 제공합니다. 이를 통해 API 요청과 응답의 데이터 형식을 일관성 있게 관리할 수 있어 개발 효율성을 높일 수 있습니다.

## OpenAPI(Swagger) 소개
OpenAPI는 RESTful API를 설계, 빌드 및 문서화하기 위한 표준 규격입니다. Swagger는 OpenAPI를 위한 툴셋 중 하나로, API를 쉽게 문서화하고 테스트할 수 있는 기능을 제공합니다. Swagger를 사용하면 API 사용자들이 API와 상호 작용하는 방법을 쉽게 이해하고 사용할 수 있습니다.

## Marshmallow와 OpenAPI(Swagger)를 함께 사용하기

1. Marshmallow를 사용하여 데이터 모델과 직렬화/역직렬화 스키마를 정의합니다. 예를 들어, 다음과 같은 사용자 모델과 스키마를 정의할 수 있습니다.

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Email()
```

2. Flask나 Django와 같은 웹 프레임워크에서 API 엔드포인트를 구현합니다. 이때, Marshmallow로 정의한 스키마를 사용하여 데이터를 직렬화하거나 역직렬화할 수 있습니다.

3. Swagger로 API 문서를 자동으로 생성하기 위해 flasgger라는 Python 패키지를 사용합니다. 아래와 같이 필요한 패키지를 설치합니다.

```
pip install flasgger
```

4. API 엔드포인트의 함수에 Swagger의 `@swag_from` 데코레이터를 추가하여 문서 정보를 추가합니다. 다음은 Swagger 문서화를 위한 예시입니다.

```python
from flasgger import swag_from

@app.route('/users', methods=['GET'])
@swag_from('swagger/users.yaml')
def get_users():
    """
    Get all users
    """
    # API 로직 구현

@app.route('/users', methods=['POST'])
@swag_from('swagger/users.yaml')
def create_user():
    """
    Create a new user
    """
    # API 로직 구현
```

5. Swagger 문서를 작성하는 Yaml 파일을 만듭니다. 예시로 users.yaml 파일을 만들고, 다음과 같이 작성할 수 있습니다.

```yaml
swagger: "2.0"
info:
  description: "This is a sample Swagger API documentation."
  version: "1.0.0"
  title: "User API"
paths:
  /users:
    get:
      tags:
        - users
      responses:
        200:
          description: "OK"
          schema:
            $ref: "#/definitions/User"
    post:
      tags:
        - users
      parameters:
        - name: "user"
          in: "body"
          required: true
          schema:
            $ref: "#/definitions/User"
      responses:
        201:
          description: "Created"
          schema:
            $ref: "#/definitions/User"
definitions:
  User:
    type: "object"
    properties:
      id:
        type: "integer"
      name:
        type: "string"
      email:
        type: "string"
```

6. API 서버를 실행하고 Swagger 문서를 확인합니다. Flask를 사용한다면 다음과 같이 코드를 추가합니다.

```python
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

if __name__ == '__main__':
    app.run()
```

위의 코드를 실행한 후에는 `http://localhost:5000/apidocs`를 통해 Swagger UI를 확인할 수 있습니다. 이를 통해 API 엔드포인트의 목록, 요청/응답 형식 등을 쉽게 확인할 수 있습니다.

이처럼 Marshmallow와 OpenAPI(Swagger)를 결합하여 API 문서를 자동으로 생성할 수 있습니다. 이를 통해 API의 사용법을 명확히 문서화하고, 개발자 간의 협업을 원활하게 진행할 수 있습니다.

## 참고 자료
- [Marshmallow 공식 문서](https://marshmallow.readthedocs.io/)
- [Swagger 공식 사이트](https://swagger.io/)