---
layout: post
title: "[python] Authlib를 사용하여 파이썬 웹 애플리케이션에 OIDC (OpenID Connect)를 구현하는 방법은?"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

## 개요
OIDC (OpenID Connect)는 웹 애플리케이션에서 인증 및 사용자 정보를 제공하기 위한 프로토콜입니다. Authlib는 파이썬 애플리케이션에서 OIDC를 손쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 이번 글에서는 Authlib를 사용하여 파이썬 웹 애플리케이션에 OIDC를 구현하는 방법에 대해 알아보겠습니다.

## Authlib 설치
Authlib를 사용하기 위해 먼저 설치해야 합니다. 아래의 명령을 이용해 Authlib를 설치합니다.

```python
pip install authlib
```

## OIDC 프로바이더 설정
Authlib를 사용하여 OIDC를 구현하기 위해서는 먼저 OIDC 프로바이더 설정이 필요합니다. OIDC 프로바이더는 예를 들어 Google, Facebook, Microsoft 등이 될 수 있습니다. 이번 예제에서는 Google을 OIDC 프로바이더로 사용하도록 하겠습니다.

Google OIDC 프로바이더 설정을 위해 [Google 개발자 콘솔](https://console.developers.google.com/)에 접속하여 프로젝트를 생성합니다. 프로젝트를 생성한 후 "API 및 서비스" > "사용자 인증 정보"로 이동하여 "OAuth 클라이언트 ID"를 생성합니다. 생성한 클라이언트 ID의 "승인된 리디렉션 URI"에는 Authlib가 리디렉션을 수행할 주소를 입력합니다. 예를 들어 `http://localhost:5000/login/google/callback`와 같이 입력할 수 있습니다.

## 파이썬 웹 애플리케이션 설정

다음으로, 파이썬 웹 애플리케이션에서 Authlib를 설정해야 합니다. 이 예제에서는 Flask 프레임워크를 사용하여 웹 애플리케이션을 구현한다고 가정하겠습니다. 아래와 같이 필요한 모듈을 임포트하고 OAuth 객체를 생성합니다.

```python
from flask import Flask, redirect, url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    userinfo_url='https://www.googleapis.com/oauth2/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'}
)
```

위 코드에서 `YOUR_SECRET_KEY`, `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`를 각각 애플리케이션의 시크릿 키, 클라이언트 ID, 클라이언트 시크릿으로 대체해야 합니다.

## 로그인 및 사용자 정보 요청

Authlib에서는 OIDC를 사용하여 로그인 및 사용자 정보 요청하기 위한 메서드를 지원합니다. 아래의 코드는 `/login/google` 경로로 요청이 들어왔을 때 Google OIDC 프로바이더를 사용하여 로그인을 수행하는 메서드입니다.

```python
@app.route('/login/google')
def login_google():
    redirect_uri = url_for('login_google_callback', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/login/google/callback')
def login_google_callback():
    token = google.authorize_access_token()
    userinfo = google.parse_id_token(token)
    # 사용자 정보 처리
    return 'Hello, {}'.format(userinfo['name'])
```

이 코드에서는 `/login/google` 경로로 요청이 들어오면 로그인 URL을 생성하고 사용자를 해당 URL로 리디렉션합니다. 사용자가 로그인에 성공하면 `/login/google/callback`으로 리디렉션이 되고, 인증 토큰 및 사용자 정보가 반환됩니다. 여기서는 사용자의 이름을 출력하도록 처리했습니다.

## 동작 확인

이제 파이썬 웹 애플리케이션을 실행하고 `http://localhost:5000/login/google`로 접속하여 Google을 통해 로그인을 수행해보세요. 로그인에 성공하면 사용자의 이름이 화면에 출력됩니다.

이렇게 Authlib를 사용하여 파이썬 웹 애플리케이션에 OIDC를 구현하는 방법에 대해 알아보았습니다. Authlib는 다양한 OIDC 프로바이더와의 통합을 지원하므로 필요에 따라 다른 프로바이더를 사용하여 구현할 수도 있습니다. 자세한 내용은 [Authlib 공식 문서](https://docs.authlib.org/en/latest/index.html)를 참고하시기 바랍니다.