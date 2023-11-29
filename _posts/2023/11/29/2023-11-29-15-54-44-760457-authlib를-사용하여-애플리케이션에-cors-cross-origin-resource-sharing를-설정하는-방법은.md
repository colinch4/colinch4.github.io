---
layout: post
title: "[python] Authlib를 사용하여 애플리케이션에 CORS (Cross-Origin Resource Sharing)를 설정하는 방법은?"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

CORS는 웹 애플리케이션에서 다른 도메인의 리소스에 접근하는 것을 가능하게 하는 보안 방식입니다. Authlib를 사용하여 CORS를 설정하는 방법은 간단합니다. 먼저, Flask를 기반으로 하는 애플리케이션을 가정하고, 다음과 같은 단계를 따르면 됩니다.

1. Authlib 설치하기: Authlib를 설치하기 위해 pip를 사용하세요.

```
pip install authlib
```

2. Flask 애플리케이션에 CORS 미들웨어 추가하기: CORS 미들웨어는 Authlib에 포함되어 있습니다. Flask 애플리케이션을 생성한 후, 다음 코드를 추가하세요.

``` python
from flask import Flask
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
oauth = OAuth(app)

cors = oauth.create_cors(app)
app.config['CORS_ENABLED'] = True
app.wsgi_app = cors(app.wsgi_app)
```
위의 코드에서 `create_cors` 메서드는 Authlib를 사용하여 CORS 미들웨어를 생성합니다. `CORS_ENABLED` 설정을 True로 설정하여 CORS를 활성화합니다. 그리고 `app.wsgi_app`에 CORS 미들웨어를 추가하여 애플리케이션에 적용합니다.

3. CORS 정책 설정하기: CORS 정책을 설정하기 위해 `@cross_origin` 데코레이터를 사용할 수 있습니다. 예를 들어, 특정 엔드포인트에 대한 CORS 정책을 설정하려면 다음과 같이 코드를 작성하세요.

``` python
from flask import jsonify
from authlib.integrations.flask_client import cross_origin

@app.route('/api/data')
@cross_origin()
def api_data():
    data = {'key': 'value'}
    return jsonify(data)
```

위의 코드에서 `@cross_origin()` 데코레이터를 `api_data` 엔드포인트에 추가했습니다. 이렇게 하면 해당 엔드포인트에서 CORS 정책이 적용됩니다.

이제 Authlib를 사용하여 Flask 애플리케이션에 CORS를 설정하는 방법을 알게되었습니다. 이를 통해 다른 도메인의 리소스에 액세스할 수 있는 보안 정책을 구현할 수 있습니다.

더 자세한 정보는 [Authlib 문서](https://docs.authlib.org/en/latest/client/flask.html#cross-origin-resource-sharing)를 참조하세요.