---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing) 정책을 왜 사용하는가요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

CORS는 브라우저가 보안상의 이유로 동일 출처 정책(Same-Origin Policy)에 따라 다른 출처(도메인, 프로토콜, 포트)의 리소스에 직접 액세스하는 것을 제한하는 정책을 우회합니다. 따라서, CORS 정책을 허용하면 웹 애플리케이션이 다른 출처에서 데이터를 가져오거나 API를 호출할 수 있게 됩니다.

이러한 기능은 주로 API 서버가 다른 도메인에서의 요청을 허용하기 위해 사용됩니다. 예를 들어, 웹 애플리케이션이 별도의 도메인에 호스팅되어 있고 해당 애플리케이션이 API 서버에 데이터를 요청할 때, CORS를 설정하여 해당 요청을 허용할 수 있습니다.

따라서, CORS 정책은 웹 애플리케이션의 보안을 유지하면서 다른 출처의 리소스에 접근할 수 있도록 하는 중요한 보안 메커니즘입니다.

더 자세한 정보는 MDN Web Docs의 "Cross-Origin Resource Sharing (CORS)" 문서를 참고하십시오. [MDN Web Docs - Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)