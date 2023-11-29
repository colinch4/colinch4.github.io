---
layout: post
title: "[python] Authlib를 사용하여 JWT (JSON Web Tokens)를 생성하고 검증하는 방법은?"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

## 소개

JWT (JSON Web Tokens)는 인증과 정보 교환에 사용되는 안전한 방법입니다. Authlib는 Python에서 JWT를 손쉽게 생성하고 검증할 수 있는 라이브러리입니다. 이 블로그 포스트에서는 Authlib를 사용하여 JWT를 생성하고 검증하는 방법에 대해 알아보겠습니다.

## Authlib 설치

Authlib를 사용하려면 먼저 Authlib를 설치해야 합니다. 다음 명령을 사용하여 Authlib를 설치해주세요:

```bash
pip install authlib
```

## JWT 생성

Authlib를 사용하여 JWT를 생성하려면 다음과 같이 코드를 작성해야 합니다.

```python
from authlib.jose import jwt

# JWT 페이로드 생성
payload = {'sub': '1234567890', 'name': 'John Doe'}

# JWT 토큰 생성
token = jwt.encode(payload, 'secret', algorithm='HS256')

print(token)
```

위의 코드는 `sub`과 `name`을 페이로드로 갖는 JWT 토큰을 생성합니다. `jwt.encode` 함수를 사용하여 페이로드와 비밀 키, 알고리즘을 전달하여 JWT 토큰을 생성합니다. 생성된 토큰은 `print` 문을 사용하여 출력됩니다.

## JWT 검증

Authlib를 사용하여 JWT를 검증하려면 다음과 같이 코드를 작성해야 합니다.

```python
from authlib.jose import jwt

# JWT 토큰
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiAiMTIzNDU2Nzg5MCIsICJuYW1lIjogIkpvaG4gRG9lIn0.uCNWV5SZiWPVVxYwM1eBWvVsX4uwBSq0ziL7vwcY_hU'

# JWT 토큰 검증
payload = jwt.decode(token, 'secret')

print(payload)
```

위의 코드는 주어진 JWT 토큰을 검증하고 페이로드를 출력합니다. `jwt.decode` 함수를 사용하여 JWT 토큰과 비밀 키를 전달하여 토큰을 검증하고 페이로드를 반환합니다.

## 마무리

Authlib를 사용하여 JWT를 생성하고 검증하는 방법에 대해 알아보았습니다. Authlib의 강력한 기능을 활용하여 안전하고 신뢰할 수 있는 JWT 토큰을 사용할 수 있습니다. Authlib의 자세한 사용법은 공식 문서를 참조해 주세요.

## 참고 자료

- Authlib 공식 문서: [https://docs.authlib.org](https://docs.authlib.org)
- JWT 공식 문서: [https://jwt.io/introduction/](https://jwt.io/introduction/)