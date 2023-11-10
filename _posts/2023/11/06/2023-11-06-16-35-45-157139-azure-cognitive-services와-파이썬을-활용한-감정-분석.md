---
layout: post
title: "Azure Cognitive Services와 파이썬을 활용한 감정 분석"
description: " "
date: 2023-11-06
tags: [Azure]
comments: true
share: true
---

## 서론
감정 분석은 인간의 감정을 자동으로 인식하고 분석하여 감정 상태를 파악하는 기술입니다. Azure Cognitive Services는 Microsoft Azure에서 제공하는 인공지능 기반의 서비스 중 하나로, 감정 분석을 포함한 다양한 기능을 제공합니다. 이번 포스트에서는 Azure Cognitive Services와 파이썬을 함께 사용하여 감정 분석을 수행하는 방법에 대해 알아보겠습니다.

## Azure Cognitive Services 소개
Azure Cognitive Services는 다양한 분야의 인공지능 기능을 비즈니스에 쉽게 통합할 수 있도록 도와주는 서비스입니다. 이 중에서도 'Text Analytics' 서비스는 텍스트 데이터를 분석하여 언어 감지, 키워드 추출, 감정 분석 등 다양한 기능을 제공합니다.

## 파이썬과 Azure Cognitive Services 연동
Azure Cognitive Services를 사용하기 위해선 먼저 Azure Portal에서 Cognitive Services 리소스를 생성해야 합니다. 생성이 완료되면 해당 리소스의 엔드포인트와 구독 키를 얻을 수 있습니다.

아래는 파이썬에서 Azure Cognitive Services의 감정 분석 기능을 사용하는 예제 코드입니다.

```python
import requests
import json

# Azure Cognitive Services의 감정 분석 API 엔드포인트
endpoint = "https://<your-endpoint>.cognitiveservices.azure.com/text/analytics/v3.0/sentiment"

# Azure Cognitive Services의 구독 키
subscription_key = "<your-subscription-key>"

# 분석할 텍스트
text = "I am very happy"

# 요청 헤더
headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": subscription_key,
}

# 요청 본문
data = {
    "documents": [
        {
            "id": "1",
            "language": "en",
            "text": text
        }
    ]
}

# 감정 분석 요청
response = requests.post(endpoint, headers=headers, json=data)
result = response.json()

# 분석 결과 출력
sentiment = result["documents"][0]["sentiment"]
confidence_scores = result["documents"][0]["confidenceScores"]

print(f"감정: {sentiment}")
print(f"확신도 점수: {confidence_scores}")
```

위 코드에서 `endpoint` 변수와 `subscription_key` 변수에는 각각 생성한 Cognitive Services 리소스의 엔드포인트와 구독 키를 넣어주어야 합니다. 또한, `text` 변수에는 분석할 텍스트를 넣어주면 됩니다.

## 결론
이번 포스트에서는 Azure Cognitive Services와 파이썬을 활용하여 감정 분석을 수행하는 방법에 대해 알아보았습니다. Azure Cognitive Services는 쉽게 활용할 수 있는 감정 분석 기능을 제공하여 다양한 비즈니스에 적용할 수 있습니다. 파이썬을 사용하여 간편하게 감정 분석을 수행할 수 있으므로, 관심 있는 분야에서 활용해보시기 바랍니다.

## 참고 자료
- [Azure Cognitive Services 공식 문서](https://azure.microsoft.com/ko-kr/services/cognitive-services/)
- [Azure Cognitive Services 설명 영상](https://www.youtube.com/watch?v=8uUW5tS7Xa4)
- [Azure Cognitive Services Python SDK GitHub 저장소](https://github.com/Azure/azure-sdk-for-python)