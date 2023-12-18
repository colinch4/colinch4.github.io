---
layout: post
title: "[python] FastAPI에서 JWT(Json Web Token) 사용하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

FastAPI는 파이썬의 높은 성능을 가진 웹 프레임워크 중 하나이며, JWT(Json Web Token)를 사용하여 사용자의 인증과 권한 부여를 처리할 수 있습니다. JWT를 사용하면 효율적으로 사용자를 인증하고, 보안을 유지할 수 있습니다.

## JWT란?

JWT는 사용자의 인증 정보를 안전하게 전달하기 위한 토큰 기반의 인증 방식입니다. 이를 통해 사용자는 로그인 후에 서버에서 제공하는 토큰을 저장하고, 이 토큰을 이용하여 API 요청을 할 수 있습니다.

## FastAPI에서 JWT 사용하기

FastAPI에서 JWT를 사용하여 사용자를 인증하려면, 먼저 PyJWT 패키지를 설치해야 합니다. 

```bash
pip install pyjwt
```

다음으로 FastAPI 앱 내에서 JWT를 사용하기 위한 함수를 작성해야 합니다. 아래는 JWT를 생성하고 검증하는 예시 코드입니다.

```python
from fastapi import FastAPI, HTTPException, Depends
import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

# JWT secret key
SECRET_KEY = "secret"
ALGORITHM = "HS256"

# Token expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Fake user model
class User():
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class TokenData():
    username: str = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verify the username and password
def verify_user(username, password):
    user = User(username, password)
    return user

# Login route
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token_expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({"sub": user.username, "exp": token_expires}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
```

위 코드에서 사용자의 username과 password를 검증하고, 검증이 성공하면 JWT를 생성하여 반환하는 `/token` 엔드포인트를 포함하고 있습니다. 

JWT를 검증하는 방법은 토큰을 디코딩하여 payload에 접근하여 확인할 수 있습니다.

필요에 따라, JWT를 사용하여 라우터의 엔드포인트에 디펜던시로 사용자 인증을 추가할 수 있습니다. 이렇게 하면 해당 엔드포인트에 접근하는 사용자의 토큰을 검증할 수 있습니다.

이렇게 하면 FastAPI 앱에서 JWT를 사용하여 사용자를 인증하고 권한을 부여할 수 있습니다.

## 결론

FastAPI를 사용하여 JWT를 사용하는 것은 효율적이고 안전한 사용자 인증 방법입니다. JWT를 사용하면 사용자의 인증 및 권한 부여를 쉽게 처리할 수 있으며, 보안을 강화할 수 있습니다.

FastAPI에서 JWT를 사용하여 사용자를 인증하고 권한을 부여하는 방법에 대한 자세한 내용은 [FastAPI 공식 문서](https://fastapi.tiangolo.com/)를 참고하시기 바랍니다.