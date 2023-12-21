---
layout: post
title: "[nodejs] REST API를 위한 CORS(Cross-Origin Resource Sharing) 처리"
description: " "
date: 2023-12-21
tags: [nodejs]
comments: true
share: true
---

웹 애플리케이션을 개발할 때, **CORS(Cross-Origin Resource Sharing)**는 중요한 보안 요소입니다. CORS는 웹 애플리케이션에서 다른 도메인에 있는 리소스에 접근할 수 있도록 허용하는 메커니즘을 말합니다. 특히, REST API를 개발하고 이를 다른 도메인의 웹 애플리케이션에서 사용하는 경우, CORS 정책을 이해하고 올바르게 처리하는 것이 중요합니다.

## CORS가 필요한 이유

웹 애플리케이션의 보안을 위해 브라우저는 다른 도메인에서 리소스를 요청하는 것을 제한합니다. 이것은 **Same-Origin Policy**(SOP)라고 불리며, 이것을 우회하기 위해 CORS가 필요합니다. REST API를 사용하는 웹 애플리케이션에서, API 서버의 도메인과 클라이언트 애플리케이션의 도메인이 다를 수 있기 때문에 CORS를 해결해야 합니다.

## CORS 처리 방법

Node.js에서 CORS를 처리하기 위해 `cors` 패키지를 사용할 수 있습니다. 이 패키지를 사용하면 간단하게 CORS를 처리할 수 있습니다.

```javascript
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());
```

이런식으로 `cors` 패키지를 사용하면, 모든 도메인에서의 요청을 허용하는 것이기 때문에 보안상 취약할 수 있습니다. 따라서, 특정 도메인만 허용하도록 설정할 수 있습니다.

```javascript
const corsOptions = {
  origin: 'http://example.com',
}

app.use(cors(corsOptions));
```

위의 예제는 `http://example.com` 도메인에서의 요청만 허용합니다.

## 요약

CORS는 웹 애플리케이션의 보안을 강화하기 위한 중요한 요소입니다. Node.js에서는 `cors` 패키지를 사용하여 간단하게 CORS를 처리할 수 있습니다. REST API를 개발할 때는 반드시 CORS 정책을 고려하여 보안을 강화해야 합니다.

참고 문헌: [MDN - Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)

이상으로 CORS를 위한 REST API 보안 강화에 대한 글을 마치겠습니다. 감사합니다.