---
layout: post
title: "[java] HttpClient의 HttpRequestInterceptor와 HttpResponseInterceptor의 차이는?"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

HttpRequestInterceptor는 요청을 변경하거나 조작하는 데 사용됩니다. 이 인터페이스를 구현하는 클래스는 HttpClient가 서버로 보내기 전에 요청에 대한 변형을 수행할 수 있습니다. 예를 들어, 헤더를 추가하거나 수정하거나 요청에 보내기 전에 요청을 암호화하는 등의 작업을 수행할 수 있습니다.

HttpResponseInterceptor는 응답을 변경하거나 조작하는 데 사용됩니다. 이 인터페이스를 구현하는 클래스는 HttpClient가 서버로부터 응답을 받은 후 응답에 대한 변형을 수행할 수 있습니다. 예를 들어, 응답 헤더를 분석하거나 수정하거나 응답 본문을 압축 해제하는 등의 작업을 수행할 수 있습니다.

따라서 HttpRequestInterceptor와 HttpResponseInterceptor는 HttpClient에서 요청 및 응답을 처리하는 방식을 커스터마이징하는 데 사용되는 인터페이스입니다. 이를 통해 사용자는 HttpClient를 자신의 요구에 맞게 조정하여 좀 더 효율적인 네트워크 통신을 구현할 수 있습니다.