---
layout: post
title: "[php] PHP에서 API 호출을 위한 기본 인증( Basic Authentication) 처리"
description: " "
date: 2023-12-21
tags: [php]
comments: true
share: true
---

API 호출 시 보안을 위해 기본 인증을 사용해야 할 때가 있습니다. PHP를 사용하여 API에 요청을 보내기 위해 기본 인증을 처리하는 방법에 대해 알아보겠습니다.

## cURL을 사용한 기본 인증

cURL을 사용하여 API에 요청을 보내는 방법은 매우 일반적입니다. 기본 인증을 사용하여 cURL을 이용해 API에 접근하는 방법은 아래와 같습니다.

```php
<?php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.example.com/data');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
curl_setopt($ch, CURLOPT_USERPWD, 'username:password');
$result = curl_exec($ch);
curl_close($ch);
?>
```
위 코드에서 'username'과 'password'는 해당 API에 제공된 인증 정보로 대체되어야 합니다.

## Guzzle을 사용한 기본 인증

Guzzle은 PHP로 만들어진 HTTP 클라이언트 라이브러리로, 기본 인증을 포함한 여러 인증 방식을 지원합니다. 기본 인증을 사용하여 Guzzle을 이용해 API에 접근하는 방법은 아래와 같습니다.

```php
<?php
require 'vendor/autoload.php';

use GuzzleHttp\Client;

$client = new Client([
    'base_uri' => 'https://api.example.com/',
    'auth' => ['username', 'password']
]);

$response = $client->request('GET', 'data');
$body = $response->getBody();
echo $body;
?>
```
위 코드에서 'username'과 'password'는 해당 API에 제공된 인증 정보로 대체되어야 합니다.

## 요약

PHP에서 API 호출을 위한 기본 인증 처리는 cURL과 Guzzle을 통해 간단하게 구현할 수 있습니다. 중요한 점은 인증 정보를 안전하게 보관하고 전송하는 것이며, 보안 상의 이유로 버전 관리 시스템에 비밀번호를 저장하는 것을 피해야 합니다.

이와 관련된 자세한 내용은 PHP 공식 웹사이트나 cURL, Guzzle의 공식 문서를 참고하시기 바랍니다.