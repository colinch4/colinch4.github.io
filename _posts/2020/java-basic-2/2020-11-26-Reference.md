---
layout: post
title: "[자바기초] Reference (참조)"
description: " "
date: 2020-11-26
tags: [java]
comments: true
share: true
---

  
  하나의 객체는 Strong, Soft, Weak, Phantom의 다양한 조합으로 참조될 수 있다.
  
  java.lang.ref 패키지를 이용하여 여러 방식으로 사용자가 reachability를 지정할 수 있고,
  
  이에따라 GC의 여부는 다양하게 달라지게 된다.
 

## Strong reference (강한 참조)
  
  일반적으로 new를 통해서 객체를 생성하게 되면 생기는 참조
  
  강한 참조를 통해 참조되는 객체는 **GC의 대상에서 제외된다**
  
  root set으로부터 시작해서 어떤 reference object도 중간에 끼지 않고 참조 가능한 객체.
  
  
## Soft reference
  
  강한 참조와는 다르게 GC에 의해 수거될 수도 있고, 않을 수도 있다.
  
  메모리에 충분한 여유가 있다면 GC가 수행되더라도 수거되지 않는다.
    
  하지만 oom에 가깝다면 수거될 확률이 높다
  
  Strong reference 는 아니지만, Soft reference만 통과하는 참조 사슬이 **하나라도** 있는 객체
  
  (다른 참조가 있어도 Soft reference만 통과하는 참조 사슬이 있다면 Soft란 소리다.)
  
  
## Weak reference (약한 참조)
  
  약한 참조는 GC가 발생하는 무조건 수거된다.
  
  java.lang.ref.WeakReference 클래스는 참조 대상인 객체를 캡슐화한 WeakReference 객체를 생성한다.
  
  캡슐화된 내부 객체는 weak reference에 의해 참조된다. (WeakReference객체는 strongly reachable 객체이다.)
  
  WeakReference 객체를 통해서만 접근할 수 있는 객체를 **weakly reachable** 이라고 한다!!
  
  (Strong, Soft가 아니면서 WeakReference로만 참조하는 참조 사슬이 있다면 Weak이란 소리다.)
  
  참조가 가능하지만 반드시 항상 유효할 필요는 없는 LRU캐시같은 임시 객체들을 저장하는 구조를 쉽게 만들 수 있다
  
  ```
  WeakReference<Sample> wr = new WeakReference<Sample>(new Sample());
  Sample ex = wr.get(); // wr과 ex 두개의 참조가 생김
  
  ...
  ex = null;  // 하나의 참조를 없앴기 때문에 남은 wr객체는 weakly reachable
  ```
  
## Phantom reference
  
  Strong , Soft, Weak 전부 아닌 객체. 
  
  finalize 되었지만 아직 메모리가 회수되지 않은 상태이다.
  
  Soft, Weak과 다르게 ReferenceQueue를 반드시 사용해야만 한다. 

  GC 대상 여부를 결정하는 부분에 관여하는 soft, weak 과는 달리, 파이널라이즈와 메모리 회수에 관여한다.
  
  객체에 대한 참조가 팬텀 참조만 남게 되면 해당 객체는 바로 파이널 라이즈가 된다.
  
  GC가 객체를 처리하는 순서는 다음과 같다
  
  1. soft
  2. weak
  3. 파이널라이즈
  4. phantom
  5. 메모리 회수
  
  phantomReference를 사용하면 어떤 객체가 파이널라이즈 된 이후에 메모리 회수 시점에 사용자 코드가 관여할 수 있다.
  
  파이널라이즈 이후에 처리해야하는 리소스 정리 등의 작업이 있다면 유용하게 사용할 수 있다.
  
  
## unreachable
  
  root set으로부터 참조되지 않는 객체
  
  

  
