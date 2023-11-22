---
layout: post
title: "[Java8] CompletableFuture 조합할 수 있는 비동기 프로그래밍"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

CompletableFuture 조합할 수 있는 비동기 프로그래밍
--------------------------------------------------

### 요약

-	한 개 이상의 원격 외부 서비스를 사용하는 긴 동작을 실행할 때는 비동기 방식으로 애플리케이션의 성능과 반응성을 향상시킬 수 있다.
-	우리 고객에게 비동기 API를 제공하는 것을 고려해야 한다. CompletableFuture의 기능을 이용하면 쉽게 비동기 API를 구현할 수 있다.
-	CompletableFuture를 이용할 때 비동기 태스크에서 발생한 에러를 관리하고 전달할 수 있다.
-	동기 API를 CompletableFuture로 감싸서 비동기적이로 소비할 수 있다.
-	서로 독립적인 비동기 동작이든 아니면 하나의 비동기 동작이 다른 비동기 동작의 결과에 의존하는 상황이든 여러 비동기 동작을 조립하고 조합할 수 있다.
-	CompletableFuture에 콜백을 등록해서 Future가 동작을 끝내고 결과를 생산했을 때 어떤 코드를 실행하도록 지정할 수 있다.
-	CompletableFuture 리스트의 모든 값이 완료될 때까지 기다릴지 아니면 하나의 값만 완료되길 기다릴지 선택할 수 있다.
