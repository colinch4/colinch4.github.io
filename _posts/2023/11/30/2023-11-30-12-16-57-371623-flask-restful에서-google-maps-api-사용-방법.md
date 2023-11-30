---
layout: post
title: "[python] Flask-RESTful에서 Google Maps API 사용 방법"
description: " "
date: 2023-11-30
tags: [python]
comments: true
share: true
---

Flask-RESTful을 사용하는 Python 개발자라면 Google Maps API를 통합하여 위치 기반 서비스를 구축하고 싶을 수 있습니다. 이 블로그 포스트에서는 Flask-RESTful 프레임워크를 사용하여 Google Maps API를 통합하는 방법을 살펴보겠습니다.

## 필요한 패키지 설치

먼저, 프로젝트에 다음과 같은 패키지를 설치해야 합니다.

```
pip install flask-restful
pip install requests
```

## Google Maps API 키 발급받기

Google Maps API를 사용하기 위해서는 먼저 Google Cloud Platform에서 키를 발급받아야 합니다. 다음 단계를 따라 진행해주세요.

1. [Google Cloud Console](https://console.cloud.google.com/)에 로그인합니다.
2. "프로젝트 선택"에서 새로운 프로젝트를 생성합니다.
3. 좌측 상단의 메뉴에서 "API 및 서비스" -> "API 및 서비스 사용 설정"으로 이동합니다.
4. "API 및 서비스 사용 설정" 페이지에서 "Google Maps JavaScript API" 를 찾아 활성화합니다.
5. 왼쪽 메뉴에서도 "보안" -> "Credential"로 이동하여 API 키를 생성합니다.

API 키가 생성되었다면 Flask-RESTful에서 사용할 준비가 완료되었습니다.

## Flask-RESTful 앱에 Google Maps API 통합하기

이제 Flask-RESTful 앱에 Google Maps API를 통합하겠습니다. 다음과 같은 코드를 참고해주세요.

```python
from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class AddressConverter(Resource):
    def get(self, address):
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=YOUR_API_KEY"
        response = requests.get(url)
        data = response.json()
        coordinates = data['results'][0]['geometry']['location']
        return coordinates, 200

api.add_resource(AddressConverter, '/convert/<string:address>')

if __name__ == '__main__':
    app.run(debug=True)
```

위 코드는 Flask-RESTful 앱을 생성하고, `/convert/<address>` 엔드포인트를 만들어 입력된 주소를 Google Maps API를 통해 위도와 경도 좌표로 변환하는 기능을 제공합니다.

주의해야 할 점은 `YOUR_API_KEY` 부분을 발급받은 Google Maps API 키로 바꿔주어야 한다는 점입니다.

## API 사용하기

Flask-RESTful 앱을 실행한 후, 브라우저나 API 클라이언트를 통해 다음과 같이 API를 호출할 수 있습니다.

```
GET /convert/Seoul
```

이렇게 하면 서울의 위도와 경도 좌표가 반환됩니다.

## 결론

이렇게 Flask-RESTful과 Google Maps API를 통합하여 위치 기반 서비스를 구축할 수 있습니다. Flask-RESTful은 편리한 RESTful API 개발을 위한 프레임워크이며, Google Maps API는 위치 정보에 관련된 다양한 기능을 제공합니다.

더 자세한 내용은 [Flask-RESTful 문서](https://flask-restful.readthedocs.io/)와 [Google Maps API 문서](https://developers.google.com/maps/documentation)를 참고하시기 바랍니다.