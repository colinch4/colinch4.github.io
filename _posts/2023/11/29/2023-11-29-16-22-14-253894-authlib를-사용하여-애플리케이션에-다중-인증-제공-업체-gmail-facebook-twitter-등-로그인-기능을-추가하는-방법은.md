---
layout: post
title: "[python] Authlib를 사용하여 애플리케이션에 다중 인증 제공 업체 (Gmail, Facebook, Twitter 등) 로그인 기능을 추가하는 방법은?"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

인증은 모든 애플리케이션이 반드시 해야하는 중요한 기능 중 하나입니다. 사용자가 간편하게 로그인할 수 있도록 여러 다중 인증 제공 업체를 지원하는 애플리케이션을 만들고 싶다면, Authlib를 사용할 수 있습니다. Authlib는 다양한 인증 및 인가 프로토콜을 지원하여 애플리케이션에 손쉽게 다중 인증을 추가할 수 있습니다.

### 1. Authlib 설치하기

먼저, Python 패키지 관리자인 pip를 사용하여 Authlib를 설치해야 합니다. 다음 명령어를 실행하여 Authlib를 설치하세요.

```bash
pip install authlib
```

### 2. 애플리케이션 설정하기

Authlib를 사용하여 인증을 추가하려는 애플리케이션의 설정을 변경해야 합니다. 이 설정에서는 각 인증 제공 업체의 클라이언트 ID와 클라이언트 비밀번호 등을 지정해야 합니다.

```python
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

oauth = OAuth(app)

oauth.register(
    name='google',
    client_id='your-google-client-id',
    client_secret='your-google-client-secret',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    userinfo_url='https://www.googleapis.com/oauth2/v1/userinfo',
    client_kwargs={'scope': 'openid profile email'}
)

oauth.register(
    name='facebook',
    client_id='your-facebook-client-id',
    client_secret='your-facebook-client-secret',
    authorize_url='https://www.facebook.com/dialog/oauth',
    access_token_url='https://graph.facebook.com/v2.12/oauth/access_token',
    userinfo_url='https://graph.facebook.com/me',
    client_kwargs={'scope': 'email'}
)

# 다른 인증 제공 업체도 필요한 경우 여기에 추가
```

### 3. 로그인 경로 생성하기

이제 각 인증 제공 업체의 로그인 경로를 생성해야 합니다. 다음은 간단한 예제 코드입니다.

```python
from flask import redirect, url_for

@app.route('/login/<provider>')
def login(provider):
    oauth = OAuth.create_client(provider)
    redirect_uri = url_for('authorize', provider=provider, _external=True)
    return oauth.authorize_redirect(redirect_uri)
```

### 4. 콜백 경로 생성하기

로그인 후 콜백이 발생하는 경로를 생성해야 합니다. 이 경로는 인증 제공 업체의 콜백 URL을 설정해야 합니다.

```python
@app.route('/authorize/<provider>')
def authorize(provider):
    oauth = OAuth.create_client(provider)
    token = oauth.authorize_access_token()
    profile = oauth.profile()
    # 사용자 정보 처리 및 세션에 저장 등 로직 추가
    return redirect('/')
```

### 5. 템플릿 엔진을 사용한 로그인 링크 생성하기

로그인 페이지에서 다중 인증 제공 업체에 대한 로그인 링크를 생성하는 방법이 필요할 수 있습니다. Flask의 템플릿 엔진을 사용하여 이를 구현할 수 있습니다.

```html
<!-- 예제 템플릿 코드 -->
<ul>
  <li><a href="{{ url_for('login', provider='google') }}">Google 로그인</a></li>
  <li><a href="{{ url_for('login', provider='facebook') }}">Facebook 로그인</a></li>
</ul>
```

위와 같이 애플리케이션에 다중 인증 제공 업체 로그인 기능을 추가하려면 Authlib를 사용하면 됩니다. Authlib는 클라이언트 ID, 클라이언트 비밀번호와 같은 설정을 통해 간단한 코드 구현을 통해 다중 인증 기능을 신속하게 만들 수 있습니다.

더 자세한 내용은 [Authlib 공식 문서](https://docs.authlib.org/)를 참조하세요.