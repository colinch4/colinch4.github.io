---
layout: post
title: "[typescript] 타입스크립트 동일 출처 정책(Same Origin Policy)에서의 출처(Origin)란 무엇인가요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

출처(Origin)란 프로토콜(예: http 또는 https), 호스트(도메인) 및 포트로 구성된 URL을 말합니다. 예를 들어, `https://www.example.com:443`와 `https://api.example.com:8080`는 서로 다른 출처에 속합니다.

동일 출처 정책은 타입스크립트에 의해 적용되며, 이는 스크립트가 다른 출처로부터 로드된 리소스와 상호 작용하려는 시도를 금지함으로써 악의적인 행위를 방지합니다.

이러한 정책을 우회하는 방법으로는 Cross-Origin Resource Sharing (CORS)와 JSONP(JSON with Padding) 등의 기술이 있습니다.

이러한 출처 정책은 웹 보안을 강화하는 데 중요하며, 타입스크립트에서 웹 애플리케이션을 개발할 때 이를 고려하고 구현하는 것이 중요합니다.

다음은 출처 정책 관련하여 타입스크립트에서 CORS를 구현하는 간단한 예제입니다.

```typescript
// CORS를 활성화하는 방법
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});
```

원문 참조:
- https://developer.mozilla.org/ko/docs/Web/Security/Same-origin_policy
- https://ko.wikipedia.org/wiki/동일_출처_정책
- https://developer.mozilla.org/ko/docs/Web/HTTP/CORS