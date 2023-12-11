---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing)와 보안 취약점의 관계는 무엇인가요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

서버에서 CORS를 활성화하면, 기본적으로 해당 서버의 리소스에 대한 외부 도메인에서의 접근을 제한하게 됩니다. 클라이언트 애플리케이션이 다른 도메인의 리소스를 요청할 때, 서버는 요청 헤더의 Origin 값을 확인하여 이를 허용할지 결정합니다.

CORS를 제대로 구성하지 않으면, **보안 취약점**으로 이어질 수 있습니다. 허용되지 않은 도메인에서의 리소스 접근으로 인해 중요한 데이터 유출이 발생할 수 있기 때문에, CORS 설정은 신중하게 이루어져야 합니다.

이에 따라 개발자들은 CORS 정책을 적절히 설정하여 외부에서의 불필요한 접근을 차단하고, 보안에 중점을 두어야 합니다.

참고 자료:
- https://developer.mozilla.org/ko/docs/Web/HTTP/CORS