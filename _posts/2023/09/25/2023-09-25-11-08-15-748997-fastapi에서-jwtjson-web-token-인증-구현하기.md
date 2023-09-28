---
layout: post
title: "FastAPI에서 JWT(JSON Web Token) 인증 구현하기"
description: " "
date: 2023-09-25
tags: [FastAPI]
comments: true
share: true
---

## 서론

FastAPI는 Python으로 작성된 빠르고 현대적인 웹 프레임워크입니다. 이 프레임워크를 사용하여 JWT(JSON Web Token) 기반의 인증 시스템을 구현하는 방법을 알아보겠습니다. JWT는 웹 애플리케이션에서 사용자 인증과 권한 부여에 사용되는 인증 프로토콜입니다.

## JWT란?

JWT는 클라이언트와 서버 간의 정보 전달을 위한 인증 방식 중 하나로, 토큰 기반의 인증 시스템입니다. 토큰은 사용자의 인증 정보를 포함하고 있으며, 서버는 토큰을 사용하여 사용자를 인증하고 필요한 권한을 부여합니다.

## FastAPI에서 JWT 인증 구현하기

먼저, `fastapi` 및 `pyjwt` 라이브러리를 설치해야 합니다:

```python
pip install fastapi[all]
pip install pyjwt
```

그런 다음, FastAPI 애플리케이션에서 JWT 인증을 구현하기 위해 다음과 같은 단계를 따릅니다:

1. 사용자 모델과 데이터베이스 스키마를 정의합니다.
2. JWT 비밀 키를 설정합니다.
3. 사용자 인증을 위한 라우터 및 함수를 작성합니다.
4. 토큰 발급 및 인증을 처리하는 함수를 작성합니다.

### 1. 사용자 모델 및 데이터베이스 스키마 정의

먼저, 사용자 모델과 데이터베이스 스키마를 정의해야 합니다. 이 예제에서는 간단한 사용자 모델을 사용합니다:

```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
```

### 2. JWT 비밀 키 설정

JWT를 사용하기 위해 비밀 키를 설정해야 합니다. 이는 토큰을 암호화 및 복호화하는 데 사용됩니다. 비밀 키를 설정하는 방법은 다음과 같습니다:

```python
from fastapi import FastAPI

app = FastAPI()

# JWT 비밀 키 설정
SECRET_KEY = "your-secret-key"
```

### 3. 사용자 인증 라우터 및 함수 작성

사용자 인증을 처리하기 위해 라우터와 함수를 작성해야 합니다. 다음은 로그인을 처리하는 예제 코드입니다:

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

# 암호화 및 복호화를 위한 암호화 컨텍스트 객체 생성
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# 로그인 기능을 처리하는 함수
def authenticate_user(username: str, password: str):
    # 사용자 인증 및 데이터베이스 검증 로직 작성
    # ...

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 토큰 만료 시간 설정 (예: 1시간)
    access_token_expires = timedelta(hours=1)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt
```

### 4. 토큰 발급 및 인증 처리 함수 작성

마지막으로, 토큰 발급 및 인증 처리 함수를 작성해야 합니다. 다음은 토큰을 검증하고 사용자를 인증하는 함수 예제입니다:

```python
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 사용자 데이터 검증 로직 작성
    # ...

@app.get("/protected_route")
async def protected_route(current_user: User = Depends(get_current_user)):
    # 보호된 라우터 처리 로직 작성
    # ...
```

## 결론

FastAPI를 사용하여 JWT(JSON Web Token) 인증 시스템을 구현하는 방법을 알아보았습니다. 이를 통해 안전하고 보안성 있는 웹 애플리케이션을 구축할 수 있습니다. JWT의 강력한 기능과 FastAPI의 높은 성능을 조합하여 최신 웹 애플리케이션을 개발해 보세요. 

#FastAPI #JWT #인증 #파이썬