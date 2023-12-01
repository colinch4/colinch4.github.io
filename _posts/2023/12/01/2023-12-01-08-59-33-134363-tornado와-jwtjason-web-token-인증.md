---
layout: post
title: "[python] Tornado와 JWT(Jason Web Token) 인증"
description: " "
date: 2023-12-01
tags: [python]
comments: true
share: true
---

## 들어가기 전에
Tornado는 파이썬으로 작성된 비동기 웹 프레임워크이며, JWT는 웹 애플리케이션에서 사용되는 토큰 기반의 인증 방식입니다. 이번 기사에서는 Tornado에서 JWT 인증을 구현하는 방법에 대해 살펴보겠습니다.

## JWT란?
JWT는 웹 애플리케이션에서 사용자 인증을 위해 토큰을 사용하는 인증 방식 중 하나입니다. 토큰은 클라이언트와 서버 간에 안전하게 전달되며, 토큰에는 클라이언트의 인증 정보가 포함됩니다. 서버는 토큰의 유효성을 확인하여 사용자 인증을 처리합니다.

### JWT 구조
JWT는 세 부분으로 구성됩니다: Header, Payload, Signature. 각 부분은 Base64 인코딩된 문자열로 이루어져 있습니다.

- Header: 토큰의 유형과 해싱 알고리즘 정보가 포함됩니다.
- Payload: 클라이언트 정보, 토큰의 만료 시간 등의 클레임 정보가 포함됩니다.
- Signature: 토큰의 유효성을 검증하기 위한 서명이 포함됩니다.

### JWT 인증 흐름
1. 클라이언트가 로그인 요청을 보냅니다.
2. 서버는 클라이언트의 인증 정보를 확인하고, 유효한 경우에만 토큰을 생성합니다.
3. 서버는 생성한 토큰을 클라이언트에게 전달합니다.
4. 클라이언트는 요청마다 토큰을 포함하여 서버에 요청을 보냅니다.
5. 서버는 토큰의 유효성을 확인하고, 인증이 필요한 리소스에 대해 응답을 처리합니다.

## Tornado에서 JWT 인증 구현하기

### 필요한 모듈 설치
Tornado에서 JWT 인증을 구현하기 위해 다음과 같은 모듈이 필요합니다:

```python
pip install tornado
pip install PyJWT
```

### Tornado 애플리케이션 설정
Tornado 애플리케이션을 시작하기 전에, JWT 인증을 위한 설정을 해야 합니다. 다음은 예시입니다:

```python
import tornado.ioloop
import tornado.web
import jwt

class JWTAuthHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        token = self.request.headers.get('Authorization')
        if token:
            try:
                decoded_token = jwt.decode(token, 'secret-key', algorithms=['HS256'])
                return decoded_token.get('user_id')
            except jwt.exceptions.InvalidTokenError:
                pass
        return None

class MainHandler(JWTAuthHandler):
    def get(self):
        user_id = self.current_user
        if user_id:
            self.write(f"Hello, {user_id}!")
        else:
            self.write("Hello, guest!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

### 클라이언트 요청 보호
JWT 인증을 사용하려면 토큰을 포함한 HTTP 요청을 보호해야 합니다. Tornado에서는 간단하게 RequestHandler를 상속하여 인증이 필요한 요청을 처리할 수 있습니다. 위의 예시에서 `MainHandler` 클래스가 인증이 필요한 리소스를 처리하는 핸들러입니다.

### JWT 생성 및 검증
JWT를 생성하고 검증하기 위해 PyJWT 모듈을 사용합니다. JWT를 생성할 때에는 서버에서 사용하는 고유한 비밀 키를 사용해야 합니다. 위의 예시에서는 'secret-key'라는 문자열을 사용하고 있습니다. 실제 사용할 때에는 더 강력한 비밀 키를 사용해야 합니다.

### 토큰 전달
토큰은 HTTP 요청의 헤더에 포함되어 전달됩니다. 일반적으로 `Authorization` 헤더에 'Bearer <token>'이라는 형식으로 토큰을 포함시킵니다. 위의 예시에서는 `get_current_user` 메소드에서 헤더에서 토큰을 추출하여 사용합니다.

## 마무리
이번 기사에서는 Tornado와 JWT 사용을 결합하여 인증을 구현하는 방법을 살펴보았습니다. Tornado는 비동기 웹 프레임워크로, JWT는 토큰 기반의 인증 방식입니다. 이 두 가지를 조합하여 보안성을 높이고, 사용자의 인증을 처리할 수 있습니다.