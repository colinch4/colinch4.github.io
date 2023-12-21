---
layout: post
title: "[javascript] Aurelia와 OpenAPI(Swagger)의 통합 방법"
description: " "
date: 2023-12-21
tags: [javascript]
comments: true
share: true
---

Aurelia는 모던한 JavaScript 프레임워크 중 하나로, 높은 성능과 확장성을 제공합니다. OpenAPI 또는 Swagger는 API를 설계, 빌드, 문서화하고 사용하는 강력한 툴이자 표준 스펙입니다. 이 두 기술을 함께 사용하면 프로젝트를 보다 쉽게 관리할 수 있으며 개발자들은 API에 대한 자세한 정보를 쉽게 찾을 수 있습니다.

## 1. Aurelia 프로젝트 생성

먼저 Aurelia 프로젝트를 생성해야합니다. Aurelia CLI를 사용하여 새로운 프로젝트를 생성하세요.

```bash
npm install -g aurelia-cli
au new my-app
cd my-app
```

## 2. OpenAPI(Swagger) 생성

그 다음, OpenAPI(Swagger)를 이용하여 API를 구성하세요. Swagger Editor 또는 Visual Studio Code의 OpenAPI 확장을 사용하여 API를 작성하고 문서화하세요.

## 3. Aurelia와 OpenAPI(Swagger) 연동

Aurelia 프로젝트에서 OpenAPI(Swagger)를 사용해야 합니다. 이를 위해 `swagger-js`와 `fetch`를 사용하여 API 호출을 관리할 수 있습니다.

먼저, `swagger-js`를 설치하세요.

```bash
npm install swagger-js
```

다음으로, OpenAPI(Swagger) 스펙을 사용하여 API 호출을 작성하세요.

```javascript
import Swagger from 'swagger-js';
const client = await Swagger({ url: '/path/to/swagger.json' });
const response = await client.apis.default.getSomeData();
```

## 4. API 사용

이제 Aurelia 앱 내에서 OpenAPI(Swagger)를 사용하여 API를 호출할 수 있습니다.

```javascript
export class MyViewModel {
  async activate() {
    const response = await client.apis.default.getSomeData();
    console.log(response.body);
  }
}
```

위 코드에서 `activate` 함수는 라우팅이 발생할 때마다 호출되며, API 호출을 수행합니다.

이제 Aurelia와 OpenAPI(Swagger)를 연동하여 더 좋은 사용자 경험과 유지보수성을 제공하도록 프로젝트를 구성할 수 있습니다.

참고문헌:
- [Aurelia Documentation](https://aurelia.io/docs)
- [OpenAPI Specification](https://swagger.io/docs/specification/about/)