---
layout: post
title: "[python] FastAPI와 OpenAPI(Swagger) 문서 자동화"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

FastAPI는 Python의 웹 프레임워크 중 하나로, 손쉽게 API를 작성하고 문서를 자동화할 수 있는 장점을 가지고 있습니다. OpenAPI(Swagger)는 API 디자인 및 문서 자동화를 지원하는 표준 규격입니다. 여기에서는 FastAPI와 OpenAPI(Swagger)를 함께 사용하여 API 문서를 자동으로 생성하는 방법을 알아봅니다.

## FastAPI와 OpenAPI(Swagger)란?

**FastAPI**는 Python의 웹 프레임워크로, Starlette 웹 프레임워크를 기반으로 하면서, Pydantic 및 typehints를 사용하여 빠르게 API를 작성할 수 있습니다. 또한, FastAPI는 자체적으로 OpenAPI 및 JSON Schema를 자동으로 생성하여 API 문서 작성을 용이하게 합니다.

**OpenAPI(Swagger)**는 RESTful API를 위한 표준 스펙으로, API 디자인, 문서 생성, 코드 생성 등을 지원하는 툴킷입니다. OpenAPI를 사용하면 API 명세서를 정의하고 이를 통해 자동으로 문서를 생성할 수 있습니다.

## FastAPI 및 OpenAPI(Swagger)의 장점

- **빠른 개발**: FastAPI를 사용하면 빠르고 간편하게 API를 작성할 수 있습니다.
- **문서 자동화**: OpenAPI(Swagger)를 사용하여 API 명세서를 작성하면, FastAPI가 자동으로 이 명세서를 활용하여 API 문서를 생성할 수 있습니다.
- **표준 준수**: OpenAPI(Swagger)는 표준 스펙으로, API 디자인 및 문서 작성 시 일관성을 유지할 수 있습니다.

## FastAPI와 OpenAPI(Swagger)를 사용한 문서 자동화 예제

다음은 FastAPI와 OpenAPI(Swagger)를 함께 사용하여 API 문서를 자동으로 생성하는 예제입니다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

위 예제 코드는 간단한 FastAPI 애플리케이션입니다. 해당 애플리케이션을 실행하고 `http://127.0.0.1:8000/docs`로 접속하면, FastAPI가 자동으로 OpenAPI(Swagger) 형식의 API 문서를 생성하여 제공합니다.

이와 같이 FastAPI와 OpenAPI(Swagger)를 함께 사용하면 API의 문서 작성 및 관리를 손쉽게 할 수 있습니다.

## 결론

FastAPI와 OpenAPI(Swagger)를 함께 사용하면, 빠르고 편리하게 API를 작성하고 관리할 수 있습니다. FastAPI가 자동으로 API 문서를 생성하므로, 개발자는 API 디자인 및 구현에 집중할 수 있습니다. 이를 통해 생산성을 향상시키고 높은 품질의 API를 제공할 수 있습니다.

이상으로 FastAPI와 OpenAPI(Swagger)를 사용한 API 문서 자동화에 대한 내용을 정리해보았습니다.

참고문헌:
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [OpenAPI(Swagger) 공식 문서](https://swagger.io/docs/)
- [FastAPI와 OpenAPI(Swagger)를 사용한 API 문서 자동화 예제](https://fastapi.tiangolo.com/tutorial/openapi/)