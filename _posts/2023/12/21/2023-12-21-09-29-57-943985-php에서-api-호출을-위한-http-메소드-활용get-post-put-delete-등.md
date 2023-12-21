---
layout: post
title: "[php] PHP에서 API 호출을 위한 HTTP 메소드 활용(GET, POST, PUT, DELETE 등)"
description: " "
date: 2023-12-21
tags: [php]
comments: true
share: true
---

PHP를 사용하여 외부 API를 호출하려는 경우, HTTP 메소드를 활용하여 GET, POST, PUT, DELETE 등의 요청을 보내야 합니다. 아래에서는 각 HTTP 메소드를 활용한 예제를 제시하겠습니다.

## GET 메소드를 사용한 API 호출

```php
// GET 요청을 보내는 예제
$url = 'https://api.example.com/products';
$response = file_get_contents($url);
```

## POST 메소드를 사용한 API 호출

```php
// POST 요청을 보내는 예제
$url = 'https://api.example.com/products';
$data = array('name' => 'Product A', 'price' => 100);
$options = array(
  'http' => array(
    'method'  => 'POST',
    'header'  => 'Content-type: application/x-www-form-urlencoded',
    'content' => http_build_query($data)
  )
);
$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);
```

## PUT 메소드를 사용한 API 호출

```php
// PUT 요청을 보내는 예제
$url = 'https://api.example.com/products/123';
$data = array('name' => 'Updated Product A', 'price' => 150);
$options = array(
  'http' => array(
    'method'  => 'PUT',
    'header'  => 'Content-type: application/x-www-form-urlencoded',
    'content' => http_build_query($data)
  )
);
$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);
```

## DELETE 메소드를 사용한 API 호출

```php
// DELETE 요청을 보내는 예제
$url = 'https://api.example.com/products/123';
$options = array(
  'http' => array(
    'method'  => 'DELETE'
  )
);
$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);
```

위 예제들을 통해 PHP에서 다양한 HTTP 메소드를 활용하여 외부 API를 호출하는 방법을 확인할 수 있습니다.

더 많은 정보를 원하시면 아래 PHP 공식 문서를 참고하시기 바랍니다.
[PHP HTTP 메소드](https://www.php.net/manual/en/function.stream-context-create.php)

## 결론
PHP에서는 다양한 HTTP 메소드를 활용하여 API 호출이 가능하며, 위 예제를 사용하여 적절한 요청을 보내고 응답을 처리할 수 있습니다.