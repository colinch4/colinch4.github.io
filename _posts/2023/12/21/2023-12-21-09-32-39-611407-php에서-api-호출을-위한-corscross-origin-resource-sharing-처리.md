---
layout: post
title: "[php] PHP에서 API 호출을 위한 CORS(Cross-Origin Resource Sharing) 처리"
description: " "
date: 2023-12-21
tags: [php]
comments: true
share: true
---

웹 개발을 진행하다 보면 웹 페이지에서 다른 도메인의 API를 호출해야 하는 경우가 발생합니다. 이때 CORS(Cross-Origin Resource Sharing) 정책으로 인해 API 호출이 제한될 수 있습니다. 이러한 경우에 PHP를 사용하여 CORS를 처리하는 방법에 대해 알아보도록 하겠습니다.

## CORS란 무엇인가요?

CORS는 Cross-Origin Resource Sharing의 약자로, 다른 도메인 간의 자원 공유를 제한하는 보안 정책입니다. 일반적으로 웹 애플리케이션이 다른 도메인의 자원을 요청할 때, 브라우저는 이러한 요청을 제한합니다. CORS는 이러한 제한을 우회하여 안전하게 자원을 공유할 수 있게 해줍니다.

## PHP에서 CORS 처리 방법

PHP에서 CORS를 처리하기 위해서는 HTTP 응답 헤더에 Access-Control-Allow-Origin 값을 설정해야 합니다. 간단한 예제를 통해 CORS 처리 방법을 알아보겠습니다.

```php
<?php
header("Access-Control-Allow-Origin: *");
```

위 예제에서 `Access-Control-Allow-Origin: *`은 모든 도메인에서의 요청을 허용하는 것을 의미합니다. 이 외에도 필요한 경우 특정 도메인만을 허용할 수 있습니다.

## 요약

웹 개발에서 다른 도메인의 API를 호출할 때 CORS(Cross-Origin Resource Sharing) 정책으로 인해 제약을 받을 수 있습니다. PHP를 사용하여 CORS를 처리하면 이러한 제약을 우회할 수 있습니다. 위에서 설명한 방법을 참고하여 PHP 애플리케이션에서 API 호출에 대한 CORS 처리를 원활하게 수행할 수 있을 것입니다.

이상으로 PHP에서 API 호출을 위한 CORS 처리에 대해 알아보았습니다. 기술적으로 어려운 부분이 있거나 추가적으로 자세한 설명이 필요한 부분이 있다면 언제든지 문의해 주세요!

[참고 자료](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)