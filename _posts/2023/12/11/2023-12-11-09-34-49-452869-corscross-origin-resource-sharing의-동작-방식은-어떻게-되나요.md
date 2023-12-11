---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing)의 동작 방식은 어떻게 되나요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

1. **프리플라이트 요청**: 먼저 클라이언트가 실제 요청을 보내기 전에 OPTIONS 메서드를 사용하여 서버에 프리플라이트(pre-flight) 요청을 보냅니다. 이 프리플라이트 요청은 실제 요청을 보내기 전에 서버가 허용하는지 여부를 확인하는 용도로 사용됩니다.

2. **응답 헤더**: 서버는 프리플라이트 요청에 대한 응답으로 Access-Control-Allow-Origin, Access-Control-Allow-Methods 및 Access-Control-Allow-Headers와 같은 헤더를 포함하여 요청이 허용되는지 여부를 클라이언트에게 알려줍니다. 이 헤더들은 클라이언트의 요청을 처리할 수 있는지 여부를 결정하는 데 사용됩니다.

3. **실제 요청**: 클라이언트가 서버로 실제 요청을 보내면, 브라우저는 요청에 대해 서버로부터 받은 응답에 포함된 Access-Control-Allow-Origin 헤더를 체크하여 요청이 허용되었는지 확인합니다. 만약 허용되었다면 클라이언트는 서버로부터 받은 응답을 처리할 수 있습니다.

이러한 과정을 통해 CORS는 보안상의 이유로 동일 출처 정책(Same Origin Policy)을 우회하면서, 안전하게 클라이언트가 다른 도메인의 자원을 요청하고 처리할 수 있도록 합니다.

자세한 내용은 MDN 웹 문서를 참고하시기 바랍니다: [MDN Web Docs - CORS](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)