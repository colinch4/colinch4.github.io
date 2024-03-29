---
layout: post
title: "[web] PHP 버전 이슈"
description: " "
date: 2021-06-17
tags: [web]
comments: true
share: true
---

## PHP 버전 이슈

## 악명 높은 php

php는 웹환경에서 가장 널리 이용되는 언어 중 하나이나, 진입 장벽이 낮은 대신 언어가 자주 변하는 터라 악명 역시 높다(언어가 버젼별로 변화가 큰데, 서버사이드 언어이다 보니 서버환경에 의존적일 수 밖에 없다. 서버환경에서는 보수적으로 접근하기 때문에 버전이 낮은 경우가 많고, 호스팅 업체마다 버젼이 다른 경우가 많다). 오늘은 예전 코드를 포팅하면서 발생한 이슈들에 대해서 정리해 볼까 한다.

## 사건 1: 농촌정주환경지표 평가사이트 (2008년 경 개발) 살려내기

대학원 시절 연구실 게시판 사이트로 개발되었던 코드를 수정하여, 연구용 사이트를 개발하였다.
베이스가 됐던 코드가 2000년 경에 연구실 선배가 구축해놓은 것으로 코드가 대부분 php3 내지 php4 수준에서 작성되었다.
두 서버에 포팅을 했는데, 하나는 php5, 하나는 php7 환경에서 기존 코드를 디플로이했다.

* POST, GET으로 넘겨준 인자는 `$_POST`, `$_GET`으로 받아야 한다.
  * 구 버젼에서는 페이지로 넘겨준 값은 `POST`, `GET` 메소드와 상관없이 변수명으로 그대로 받을 수 있었으나, 최근 버젼은 아니다.
  * 파일업로드시 속성값도 바뀌었다. `$_POST`가 아니라, `$_FILES`로 받아줘야 한다.
* php 코드 도입부는 `<?php`가 기본 설정이다.
  * 구 버젼은 `<?`와 같이 간략하게 쓰는 경우가 많았다.
* 더이상 간단한 식 표현(`<?=$variable?>`)를 지원하지 않는다.
  * 최근버젼에는 보안 문제로 해당 구분을 지원하지 않으므로, `<?php echo $variable; ?>`과 같이 풀어써줘야 한다.
* 일부 함수가 바뀌었다.
  * `split` -> `preg_split()`, `explode()`, `str_split()`
  * `mysql` -> `mysqli`
* 서버 파라미터도 직접 접근이 안된다.
  * `$PHP_SELF` -> `$_SERVER['PHP_SELF']`

## 좀 더 정리된 문헌

* [Migrating from PHP 5.6.x to PHP 7.0.x: 이전 버전과 호환되지 않는 변경점](http://php.net/manual/kr/migration70.incompatible.php)점
* [PHP 4에서 PHP 5.0.x로 이행: 이전 버전과 호환되지 않는 변경점](http://php.net/manual/kr/migration5.incompatible.php)
