---
layout: post
title: "[python] M2Crypto를 사용하여 SSL/TLS 클라이언트에서 SNI(Server Name Indication)를 사용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-12-22
tags: [python]
comments: true
share: true
---

SNI는 여러 도메인 이름을 하나의 IP 주소에 매핑하는데 사용되는 기술로, 여러 개의 SSL/TLS 사이트를 호스팅하는 서버에서 중요한 역할을 합니다. M2Crypto에서 SNI를 사용하여 서버로 요청을 보내는 방법은 다음과 같습니다.

먼저, `M2Crypto.SSL.Context` 객체를 만듭니다. 이때 `M2Crypto.SSL.Context` 생성자에 `sslv23_client_method()`을 인자로 전달하여 SSL/TLS 연결을 설정합니다.

그런 다음, `M2Crypto.SSL.Context` 객체의 `set_tlsext_host_name()` 메서드를 사용하여 SNI 확장을 설정합니다. 이 메서드에는 클라이언트가 연결하려는 서버의 호스트 이름을 전달합니다.

예를 들어, `example.com` 도메인에 연결할 때 SNI를 사용하려면 다음과 같이 코드를 작성할 수 있습니다.

```python
from M2Crypto import SSL

ctx = SSL.Context('sslv23')
ctx.set_tlsext_host_name(b'example.com')

# 나머지 코드를 통해 SSL/TLS 연결을 수립하고 사용합니다.
```

위 코드에서 `set_tlsext_host_name()` 메서드에 전달한 호스트 이름은 바이트 문자열로 전달되어야 합니다.

이렇게 함으로써 M2Crypto를 사용하여 SSL/TLS 클라이언트에서 SNI를 활용할 수 있습니다.