---
layout: post
title: "[python] Authlib를 사용하여 애플리케이션에 SSO (Single Sign-On)을 구현하는 방법은?"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

SSO (Single Sign-On)는 사용자가 여러 애플리케이션에 대해 한 번만 로그인하면, 다른 애플리케이션들에 자동으로 접근할 수 있는 인증 방식입니다. 이번 글에서는 Python의 `Authlib` 라이브러리를 사용하여 SSO를 구현하는 방법에 대해 알아보겠습니다.

## 1. Authlib 설치

먼저, `Authlib`를 설치해야 합니다. 아래의 명령어를 사용하여 설치할 수 있습니다:

```
pip install Authlib
```

## 2. 애플리케이션 등록

Authlib를 사용하기 위해서는 애플리케이션을 등록해야 합니다. 대부분의 SSO 서비스 제공자는 개발자 포털에서 애플리케이션을 등록하고 클라이언트 ID 및 클라이언트 시크릿을 발급해줍니다. 이 정보는 나중에 사용됩니다.

## 3. Flask 애플리케이션 설정

SSO를 구현하기 위해 Flask 웹 프레임워크를 사용하는 예제를 보겠습니다. 아래와 같이 `app.py` 파일을 생성하고, 다음과 같은 코드로 SSO 기능을 추가합니다.

### app.py

```python
from flask import Flask, redirect, url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

oauth = OAuth(app)
sso = oauth.register(
    'sso',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    server_metadata_url='https://sso-provider.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile'}
)

@app.route('/')
def index():
    if not sso.authorized:
        return redirect(url_for('sso.login'))
    token = sso.token
    # 토큰을 이용하여 사용자 정보를 얻고 원하는 작업을 수행합니다.
    return 'Hello, {}'.format(token['name'])

if __name__ == '__main__':
    app.run()
```

위 코드에서 굵게 표시된 부분은 사용자가 직접 설정해야 하는 부분입니다. 

- `SECRET_KEY`: Flask 애플리케이션의 시크릿 키를 설정합니다.
- `YOUR_CLIENT_ID`: 등록한 애플리케이션의 클라이언트 아이디를 입력합니다.
- `YOUR_CLIENT_SECRET`: 등록한 애플리케이션의 클라이언트 시크릿을 입력합니다.
- `server_metadata_url`: SSO 제공자의 메타데이터 URL을 입력합니다. 이 URL은 클라이언트 등록 시에 제공됩니다.

## 4. SSO 로그인

애플리케이션을 실행하고 브라우저에서 `http://localhost:5000`에 접속하면 SSO 로그인 화면이 표시됩니다. 사용자는 등록된 SSO 계정으로 로그인하고, 인증이 완료되면 `index()` 함수에서 사용자의 이름을 화면에 출력합니다.

## 5. 추가 작업

위의 예제는 간단한 SSO 로그인을 구현한 것이며, 실제로는 추가적인 작업이 필요할 수 있습니다. 예를 들어, 사용자 정보를 세션에 저장하거나, 로그아웃 기능을 구현하는 등의 작업이 필요할 수 있습니다.

`Authlib`는 다양한 인증 프로토콜과 플랫폼을 지원하므로, 자세한 내용은 공식 문서를 참고하시기 바랍니다.

## 결론

이제 `Authlib`를 사용하여 Python 애플리케이션에 SSO를 구현하는 방법에 대해 알아보았습니다. SSO를 통해 사용자는 더 편리하게 여러 애플리케이션을 이용할 수 있고, 개발자는 인증과 관련된 로직을 단순화할 수 있습니다.

## 참고 자료

- [Authlib 공식 문서](https://docs.authlib.org/)
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [OAuth 2.0 백서](https://oauth.net/2/)
- [OpenID Connect 스펙](https://openid.net/specs/openid-connect-core-1_0.html)