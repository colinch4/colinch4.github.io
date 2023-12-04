---
layout: post
title: "[python] Marshmallow와 PyMongo를 함께 사용하여 MongoDB 데이터 처리하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

이번 포스트에서는 Python의 Marshmallow와 PyMongo를 함께 사용하여 MongoDB 데이터를 쉽게 처리하는 방법을 알아보겠습니다. Marshmallow는 직렬화와 역직렬화 작업을 도와주는 유용한 라이브러리이며, PyMongo는 Python에서 MongoDB와 상호작용하기 위한 라이브러리입니다.

## 1. Marshmallow 및 PyMongo 설치

먼저 Marshmallow와 PyMongo를 설치해야 합니다. 아래의 명령어를 사용하여 설치합니다.

```python
pip install marshmallow pymongo
```

## 2. Marshmallow 스키마 작성

Marshmallow를 사용하여 MongoDB의 데이터를 처리하기 위해 스키마를 작성해야 합니다. 스키마는 데이터 모델의 구조를 정의하는 데 사용됩니다. 예를 들어, 사용자의 이름과 이메일을 저장하는 사용자 스키마를 작성해보겠습니다.

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
```

위의 코드에서 `UserSchema`는 Marshmallow의 `Schema` 클래스를 상속받아 작성된 클래스입니다. `name` 필드와 `email` 필드는 각각 문자열과 이메일 형식을 나타내는 `fields.Str()`과 `fields.Email()`로 정의되었습니다.

## 3. PyMongo를 사용하여 데이터 저장하기

이제 작성한 스키마를 사용하여 PyMongo를 통해 MongoDB에 데이터를 저장하는 방법을 알아보겠습니다. 아래의 코드를 참고하세요.

```python
from pymongo import MongoClient

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017')
db = client['mydatabase']
collection = db['users']

# 새로운 사용자 데이터 생성
new_user = {
    'name': 'John Doe',
    'email': 'johndoe@example.com'
}

# 스키마 유효성 검사
validated_user = UserSchema().load(new_user)
if validated_user.errors:
    print(validated_user.errors)
else:
    # 데이터 저장
    collection.insert_one(validated_user.data)
    print('User data saved successfully.')
```

위의 코드에서는 PyMongo를 사용하여 로컬 MongoDB에 연결한 후, `users` 컬렉션에 새로운 사용자 데이터를 저장하는 과정을 보여줍니다. `UserSchema().load()`를 사용하여 새로운 사용자 데이터를 스키마에 유효성 검사한 후, `validated_user.data`를 사용하여 검증된 데이터를 저장합니다.

## 4. PyMongo를 사용하여 데이터 조회하기

데이터를 저장했다면, 이제 PyMongo를 사용하여 MongoDB에서 데이터를 조회하는 방법을 알아보겠습니다. 아래의 코드를 참고하세요.

```python
from pprint import pprint

# 모든 사용자 데이터 조회
users = collection.find()
for user in users:
    pprint(user)
```

위의 코드에서 `collection.find()`를 사용하여 모든 사용자 데이터를 조회한 후, `pprint` 함수를 사용하여 데이터를 보기 좋게 출력합니다.

## 5. 결론

이제 Marshmallow와 PyMongo를 함께 사용하여 MongoDB 데이터 처리하는 방법을 알게 되었습니다. Marshmallow를 사용하여 데이터의 직렬화와 역직렬화를 처리하고, PyMongo를 사용하여 MongoDB와 상호작용하는 것은 간단하면서도 강력한 방법입니다. 이를 통해 MongoDB 데이터를 효과적으로 다룰 수 있습니다.

Marshmallow 공식 문서: [링크](https://marshmallow.readthedocs.io)
PyMongo 공식 문서: [링크](https://pymongo.readthedocs.io)