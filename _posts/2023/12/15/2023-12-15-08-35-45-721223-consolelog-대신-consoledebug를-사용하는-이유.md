---
layout: post
title: "[javascript] console.log() 대신 console.debug()를 사용하는 이유"
description: " "
date: 2023-12-15
tags: [javascript]
comments: true
share: true
---

웹 개발을 하다 보면 `console.log()`를 사용하여 개발 중에 데이터나 변수 값을 확인하는 것은 흔한 일이다. 하지만 `console.debug()`를 대신 사용해야 할 때가 있는데, 그 이유에 대해 알아보자.

## 1. `console.debug()`의 목적

`console.debug()`는 코드 내의 디버깅용 메시지를 출력하는 데에 사용된다. 이는 `console.log()`와 같은 기능을 하지만, 개발자 도구에서 명시적으로 디버그 메시지로 필터링되므로 특정 디버깅 목적을 위해 사용하기에 좋다.

## 2. `console.debug()` 사용법

```javascript
console.debug('This is a debug message');
```

## 3. `console.log()`와의 비교

그러나 대부분의 경우 `console.log()`도 충분히 디버깅 용도로 사용될 수 있다. 따라서, `console.debug()`를 사용해야 하는지에 대한 결정은 각 개발자의 개인적인 기호 및 프로젝트 요구 사항에 따라 다를 수 있다.

## 요약

`console.debug()`와 `console.log()` 모두 디버그용으로 값을 로그로 남기는 데 사용되지만, `console.debug()`를 사용하면 더 명시적인 디버깅 메시지를 출력할 수 있다. 그러나 어떤 것을 사용할지에 대한 결정은 팀이나 프로젝트에 따라 달라질 수 있다.

더 많은 정보를 원한다면 [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/API/Console/debug)를 참고하십시오.