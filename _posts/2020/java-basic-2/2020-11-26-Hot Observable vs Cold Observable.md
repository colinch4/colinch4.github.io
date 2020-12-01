---
layout: post
title: "[자바기초] Cold Observable vs Hot Observable"
description: " "
date: 2020-11-26
tags: [java]
comments: true
share: true
---


# Cold Observable
  
  
  Observable을 선언하고 just, fromIterable 함수를 호출해도 옵서버가 subscribe함수를 호출하지 않으면
  
  데이터를 발행하지 않는다.
  
  Cold Observable의 예로는 웹 요청, 데이터베이스 쿼리와 파일 읽기 등이며, 대부분의 Observable은
  
  Cold Observable이다. 
  
  
# Hot Observable
  
  
  (= Connectable Observable)
  
  구독자의 존재 여부와 관계없이 데이터를 발행하는 Observable
  
  구독자는 구독한 시점부터 Observerble에서 발행한 값을 받는다.  
  
  즉, 구독자로서는 Observable에서 발행하는 데이터를 처음부터 모두 수신할 것으로 보장할 수 없다.
  
  Hot Observable의 예로는 마우스, 키보드, 시스템, 센서 데이터와 주식가격 등이 있다.
  
  관련 메서드는 publish / multicast / connect / replay / replayAll / share / shareReplay 등이 있다.  
   
  #### Hot Observable은 **배압**(Back Pressure)를 고려해야 한다!
  
  배압이란 데이터를 발행하는 속도와 구독자가 처리하는 속도의 차이가 클 때 발생하는 것이다.
