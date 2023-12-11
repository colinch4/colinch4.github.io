---
layout: post
title: "파이썬으로 Azure Cognitive Services API 사용하기"
description: " "
date: 2023-11-06
tags: [azure]
comments: true
share: true
---

Azure Cognitive Services는 인공 지능 및 기계 학습을 활용한 다양한 기능을 제공하는 Microsoft의 클라우드 기반 서비스입니다. 이 서비스를 활용하여 언어 처리, 이미지 분석, 음성 인식 등 다양한 작업을 수행할 수 있습니다. 이번 포스트에서는 파이썬을 사용하여 Azure Cognitive Services API를 활용하는 방법에 대해 알아보겠습니다.

## Azure Cognitive Services API 키 생성하기

Azure Portal에 로그인한 후, Cognitive Services 리소스를 생성합니다. 생성이 완료되면 API 키를 얻을 수 있습니다. 이 키는 인증에 사용되며, API 호출 시 필요합니다. API 키는 보안에 민감한 정보이므로, 암호화된 환경 변수 등을 사용하여 안전하게 보관하는 것이 좋습니다.

## Python에서 Azure Cognitive Services API 호출하기

Azure Cognitive Services를 사용하기 위해 Python에서는 `requests` 모듈을 사용하여 HTTP 요청을 보내는 방식을 사용할 수 있습니다. 먼저, 필요한 모듈을 설치하고 import해야 합니다.

```python
import requests
import json
```

다음으로, API 키와 API 엔드포인트를 변수에 할당합니다.

```python
subscription_key = 'YOUR_SUBSCRIPTION_KEY'
endpoint = 'YOUR_API_ENDPOINT'
```

API 호출을 위한 요청 헤더와 매개 변수를 설정합니다.

```python
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

params = {
    'language': 'en',
    'text': 'Hello, how are you?'
}
```

API를 호출하고 응답을 받습니다.

```python
response = requests.post(endpoint, headers=headers, params=params)
result = response.json()
```

API 호출 결과를 확인합니다.

```python
print(result)
```

## API 종류 및 사용 예시

Azure Cognitive Services는 다양한 API를 제공합니다. 몇 가지 API의 사용 예시를 살펴보겠습니다.

### 1. 언어 감지 API

이 API는 주어진 텍스트의 언어를 감지합니다. 사용자가 입력한 텍스트를 다른 언어로 번역하거나 언어별로 다른 처리를 해줄 때 유용합니다.

#### 요청

```python
endpoint = 'https://api.cognitive.microsofttranslator.com/languages/detect'

params = {
    'subscription-key': subscription_key,
    'api-version': '3.0'
}

text = '안녕하세요, 반갑습니다.'

data = [{
    'text': text
}]

response = requests.post(endpoint, headers=headers, params=params, json=data)
result = response.json()
```

#### 응답

```
{
    'detectedLanguage': {
        'language': 'ko',
        'score': 1.0
    },
    'alternatives': []
}
```

### 2. 이미지 분석 API

이 API는 주어진 이미지를 분석하고 텍스트, 개체, 색상 등의 정보를 추출합니다. 이미지 기반의 머신러닝 작업을 수행할 때 유용합니다.

#### 요청

```python
endpoint = 'https://westus.api.cognitive.microsoft.com/vision/v3.1/analyze'

params = {
    'visualFeatures': 'Description',
    'details': 'Landmarks',
    'language': 'en'
}

image_url = 'https://example.com/image.jpg'

data = {
    'url': image_url
}

response = requests.post(endpoint, headers=headers, params=params, json=data)
result = response.json()
```

#### 응답

```
{
    'description': {
        'tags': ['outdoor', 'building', 'street', 'city', 'skyscraper', 'traffic', 'sign', 'people'],
        'captions': [
            {
                'text': 'A picture of a city with tall buildings and busy streets.',
                'confidence': 0.815040011882782
            }
        ]
    }
}
```

## 마치며

이번 포스트에서는 파이썬으로 Azure Cognitive Services API를 사용하는 방법에 대해 알아보았습니다. Azure Cognitive Services는 다양한 작업을 수행할 수 있는 강력한 도구이며, 파이썬을 통해 이를 활용하는 것은 매우 간단합니다. 프로젝트에서 인공 지능 기능을 구현하기 위해 Azure Cognitive Services를 고려해보세요.

\n\n
hashtags: #Azure #CognitiveServices