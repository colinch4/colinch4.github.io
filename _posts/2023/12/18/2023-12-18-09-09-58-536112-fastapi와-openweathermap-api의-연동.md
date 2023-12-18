---
layout: post
title: "[python] FastAPI와 OpenWeatherMap API의 연동"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

FastAPI는 빠르고 간단하게 API를 만들 수 있는 웹 프레임워크이며, OpenWeatherMap API는 날씨 정보를 제공하는 API입니다. 이 블로그 포스트에서는 FastAPI를 사용하여 OpenWeatherMap API와 연동하여 날씨 정보를 제공하는 간단한 예제를 살펴보겠습니다.

## 1. FastAPI 설치

먼저 FastAPI를 설치합니다.

```bash
pip install fastapi
```

## 2. OpenWeatherMap API 키 발급

OpenWeatherMap API를 사용하기 위해서는 API 키가 필요합니다. [OpenWeatherMap 웹사이트](https://openweathermap.org/)에서 회원가입을 한 후에 API 키를 발급받을 수 있습니다.

## 3. FastAPI 애플리케이션 작성

다음은 간단한 FastAPI 애플리케이션을 작성하는 예제입니다.

```python
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city: str):
    api_key = "<Your-OpenWeatherMap-API-Key>"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()
```

위의 코드는 `/weather` 엔드포인트를 통해 해당 도시의 날씨 정보를 제공하는 간단한 API를 만드는 예제입니다.

## 4. 테스트

애플리케이션을 실행한 후 `http://127.0.0.1:8000/weather/{city}`에 접속하여 날씨 정보를 확인할 수 있습니다.

## 결론

FastAPI를 사용하면 간단하게 RESTful API를 만들 수 있으며, OpenWeatherMap API와의 연동을 통해 실제로 유용한 서비스를 제공할 수 있습니다. FastAPI와 OpenWeatherMap API의 연동을 통해 다양한 웹 서비스나 애플리케이션을 구축할 수 있을 것입니다.