---
layout: post
title: "[python] FastAPI의 CORS(Cross-Origin Resource Sharing) 처리"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

웹 애플리케이션을 개발하다보면 CORS 문제를 마주치게 될 때가 있습니다. CORS는 웹 애플리케이션에서 다른 도메인으로부터의 HTTP 요청을 제한하는 보안 매커니즘입니다. 이펙티브한 CORS 처리는 FastAPI를 이용한 웹 애플리케이션 개발시 중요한 요소 중 하나입니다. FastAPI에서는 CORS를 간단하게 처리할 수 있도록 지원하고 있습니다.

## CORS 처리 설정

FastAPI에서 CORS를 다루기 위해서는 `fastapi.middleware.cors`를 import하고 애플리케이션에 미들웨어로 추가해야 합니다. 

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

위 코드에서 `allow_origins`, `allow_credentials`, `allow_methods`, `allow_headers` 등의 값을 설정하여 CORS 처리를 지정할 수 있습니다.

- `allow_origins`: 허용할 도메인의 목록을 지정합니다. 여기서 `*`는 모든 도메인을 허용하겠다는 뜻입니다. 만약 어떤 도메인만을 허용하려면 해당 도메인의 URL을 명시해야 합니다.
- `allow_credentials`: 자격 증명을 허용할지 여부를 지정합니다. `True`로 설정하면 자격 증명을 허용하며, `False`로 설정하면 거부합니다.
- `allow_methods`: 허용할 HTTP 메소드를 지정합니다. 여기서는 `*`를 사용하여 모든 메소드를 허용하겠다는 의미입니다. 필요한 경우 특정 메소드만을 지정할 수도 있습니다.
- `allow_headers`: 허용할 HTTP 헤더를 지정합니다. 마찬가지로 `*`를 사용하여 모든 헤더를 허용하겠다는 의미입니다.

## 결론

FastAPI를 이용하면 CORS를 간단하게 처리할 수 있습니다. 위와 같이 설정을 통해 필요에 맞게 CORS를 다룰 수 있으며, 이를 통해 안전하고 유연한 웹 애플리케이션을 개발할 수 있습니다.