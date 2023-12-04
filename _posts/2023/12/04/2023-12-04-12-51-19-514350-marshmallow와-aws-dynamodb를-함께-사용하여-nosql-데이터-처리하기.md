---
layout: post
title: "[python] Marshmallow와 AWS DynamoDB를 함께 사용하여 NoSQL 데이터 처리하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

NoSQL 데이터베이스는 관계형 데이터베이스와 달리 유연하고 확장 가능한 데이터 모델을 제공합니다. AWS DynamoDB는 매우 확장 가능하고 높은 처리량을 지원하는 NoSQL 데이터베이스입니다. 이 글에서는 Python의 Marshmallow와 함께 AWS DynamoDB를 사용하여 NoSQL 데이터 처리하는 방법에 대해 알아보겠습니다.

## Marshmallow란?

Marshmallow는 Python 객체와 데이터를 직렬화(serialize)하고 역직렬화(deserialize)하기 위한 라이브러리입니다. Marshmallow를 사용하여 데이터를 직렬화하면, 그 데이터를 다른 시스템에 전송하거나 저장하기 쉽습니다. 또한, 역직렬화를 통해 데이터를 손쉽게 파싱하고 조작할 수 있습니다.

## AWS DynamoDB 설정하기

먼저, AWS DynamoDB를 사용하기 위해 필요한 설정을 해야합니다. AWS 계정을 생성한 후, IAM 사용자를 생성하고 필요한 권한을 부여해야합니다. 그리고 AWS CLI를 설치한 후, `aws configure` 명령어를 통해 AWS 계정 정보를 설정합니다.

## Marshmallow 모델 설정하기

Marshmallow를 사용하여 데이터 모델을 시리얼라이즈하려면, 데이터 모델에 대한 스키마를 정의해야합니다. 스키마는 데이터 모델의 필드와 필드 유효성 검사 규칙을 정의하는 역할을 합니다. 다음은 예시 모델과 스키마입니다.

```python
from marshmallow import Schema, fields

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class UserSchema(Schema):
    id = fields.Str()
    name = fields.Str(required=True)
    email = fields.Email(required=True)
```

위의 예시에서는 `User` 모델과 `UserSchema` 스키마를 정의했습니다. `UserSchema`는 `User` 모델의 필드를 정의하고 필드의 유효성 검사 규칙을 설정합니다.

## AWS DynamoDB와 연동하기

Marshmallow와 AWS DynamoDB를 함께 사용하려면, DynamoDB Python SDK인 `boto3`를 설치해야합니다. 그리고 `boto3`를 사용하여 데이터를 저장, 조회, 수정, 삭제할 수 있습니다. 다음은 DynamoDB에 데이터를 저장하는 예시 코드입니다.

```python
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def save_user(user):
    user_data = UserSchema().dump(user)
    table.put_item(Item=user_data)

user = User(id='1', name='John', email='john@example.com')
save_user(user)
```

위의 예시에서는 `boto3`를 사용하여 DynamoDB와 연결하고, `users` 테이블에 데이터를 저장하는 `save_user` 함수를 정의했습니다.

## 데이터 조회하기

DynamoDB에서 데이터를 조회하기 위해서는 `query` 메서드나 `scan` 메서드를 사용할 수 있습니다. `query` 메서드는 특정 키를 기반으로 데이터를 조회하고, `scan` 메서드는 테이블의 모든 데이터를 조회합니다. 다음은 `query` 메서드를 사용하여 특정 사용자를 조회하는 예시 코드입니다.

```python
def get_user_by_id(user_id):
    response = table.query(
        KeyConditionExpression='id = :id',
        ExpressionAttributeValues={':id': user_id}
    )
    if response.get('Items'):
        user_data = response['Items'][0]
        user = UserSchema().load(user_data)
        return user

user = get_user_by_id('1')
print(user.name, user.email)
```

위의 예시에서는 `query` 메서드를 사용하여 `id` 필드 기반으로 사용자를 조회하고, 조회된 데이터를 `UserSchema`를 사용하여 역직렬화합니다.

## 데이터 수정하기

DynamoDB에서 데이터를 수정하기 위해서는 `update_item` 메서드를 사용합니다. 다음은 `update_item` 메서드를 사용하여 사용자의 이메일 주소를 수정하는 예시 코드입니다.

```python
def update_user_email(user_id, new_email):
    table.update_item(
        Key={'id': user_id},
        UpdateExpression='SET email = :email',
        ExpressionAttributeValues={':email': new_email}
    )

update_user_email('1', 'new_email@example.com')
```

위의 예시에서는 `update_item` 메서드를 사용하여 `email` 필드를 수정합니다.

## 데이터 삭제하기

DynamoDB에서 데이터를 삭제하기 위해서는 `delete_item` 메서드를 사용합니다. 다음은 `delete_item` 메서드를 사용하여 사용자를 삭제하는 예시 코드입니다.

```python
def delete_user(user_id):
    table.delete_item(Key={'id': user_id})

delete_user('1')
```

위의 예시에서는 `delete_item` 메서드를 사용하여 사용자를 삭제합니다.

## 결론

이 글에서는 Marshmallow를 사용하여 데이터 직렬화 및 역직렬화를 처리하고 AWS DynamoDB와 연동하여 NoSQL 데이터를 처리하는 방법에 대해 알아보았습니다. Marshmallow의 강력한 직렬화 기능과 DynamoDB의 확장 가능한 NoSQL 데이터베이스를 함께 사용하면 애플리케이션의 데이터 처리에 유용합니다.

## 참고자료

- [Marshmallow 공식 문서](https://marshmallow.readthedocs.io)
- [AWS SDK for Python(Boto3) 공식 문서](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS DynamoDB 공식 문서](https://docs.aws.amazon.com/dynamodb/)