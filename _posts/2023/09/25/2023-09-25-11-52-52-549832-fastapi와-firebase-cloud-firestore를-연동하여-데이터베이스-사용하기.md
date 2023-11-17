---
layout: post
title: "FastAPI와 Firebase Cloud Firestore를 연동하여 데이터베이스 사용하기"
description: " "
date: 2023-09-25
tags: [FastAPI]
comments: true
share: true
---

Firebase Cloud Firestore는 NoSQL 기반의 클라우드 데이터베이스로, 실시간 데이터 동기화와 확장성을 제공하는 매우 강력한 도구입니다. 이번 포스트에서는 FastAPI와 Firebase Cloud Firestore를 연동하여 데이터베이스를 사용하는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하고, 새 프로젝트를 생성합니다.
2. 프로젝트 설정으로 이동하여 "서비스 계정" 탭에서 새 서비스 계정을 만들고, "비공개 키"를 생성합니다.
3. 생성된 비공개 키를 안전한 장소에 보관합니다.

## FastAPI 프로젝트 설정

1. FastAPI 프로젝트를 생성합니다.
2. 필요한 라이브러리를 설치합니다. (`pip install firebase-admin pydantic`)

## Firebase 인증 설정

1. Firebase 비공개 키를 프로젝트의 루트 디렉토리에 저장합니다.
2. FastAPI의 설정 파일에서 Firebase 인증 정보를 로드합니다. 예를 들어, `firebase_service_account.json` 파일을 사용하는 경우 다음과 같이 설정 파일을 작성합니다.

```python
# app/settings.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    firebase_service_account_path: str = "firebase_service_account.json"
    
    class Config:
        env_file = ".env"
```

```python
# main.py

from fastapi import FastAPI
from firebase_admin import credentials, firestore, initialize_app

from app.settings import Settings

app = FastAPI()
settings = Settings()

# Firebase 초기화
cred = credentials.Certificate(settings.firebase_service_account_path)
firebase_app = initialize_app(cred)
db = firestore.client()
```

## 데이터베이스 사용하기

FastAPI에서 Firebase Cloud Firestore를 사용하는 예제입니다.

```python
# main.py

from fastapi import FastAPI
from firebase_admin import db
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: str
    name: str
    email: str

@app.post("/users")
async def create_user(user: User):
    user_ref = db.reference("users")
    user_ref.child(user.id).set(user.dict())
    return {"message": "User created successfully"}
```

이 예제에서는 `User` 모델을 정의하고, POST 요청을 통해 사용자를 생성하고 Firestore에 저장하는 API를 구현했습니다. Firebase의 `db.reference` 메서드를 사용하여 Firestore 데이터베이스에 접근하고, `set` 메서드를 사용하여 데이터를 저장합니다.

## 마치며

이번 포스트에서는 FastAPI와 Firebase Cloud Firestore를 연동하여 데이터베이스를 사용하는 방법을 알아보았습니다. Firebase의 다른 기능과 FastAPI의 다른 기능을 함께 사용하여 강력한 웹 애플리케이션을 개발할 수 있습니다. Firebase와 FastAPI의 공식 문서를 참고하여 더 많은 기능을 활용해 보세요. #FastAPI #Firebase