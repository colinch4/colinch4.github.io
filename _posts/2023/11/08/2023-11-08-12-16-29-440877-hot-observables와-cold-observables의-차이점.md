---
layout: post
title: "Hot Observables와 Cold Observables의 차이점"
description: " "
date: 2023-11-08
tags: []
comments: true
share: true
---

RxJava에서는 Observable에는 두 가지 유형이 있습니다: Hot Observables와 Cold Observables. 이 두 유형은 Observable이 어떻게 동작하는지와 관련된 중요한 차이점이 있습니다.

### Cold Observables
Cold Observables는 Observable을 subscribe 할 때마다 새로운 데이터 스트림을 생성하는 Observable입니다. 간단히 말해, Observer가 subscribe 하면 Observable은 처음부터 데이터를 다시 방출하기 시작합니다. 이는 Observer마다 각자의 독립적인 데이터 스트림을 가지며, Observer 간의 데이터 공유가 없습니다.

```java
Observable<Integer> coldObservable = Observable.range(1, 5);
coldObservable.subscribe(number -> System.out.println("Observer 1: " + number));
coldObservable.subscribe(number -> System.out.println("Observer 2: " + number));
```

위의 예시에서 `coldObservable`은 `1, 2, 3, 4, 5`의 숫자를 방출하는 Observable입니다. 두 개의 Observer가 `coldObservable`을 각각 subscribe하면, 독립적으로 데이터 스트림을 받아오게 됩니다.

### Hot Observables
Hot Observables는 Observable을 subscribe 한 이후부터 Observer가 데이터를 받도록 하는 Observable입니다. 다시 말해, Observable은 subscribe 이전에 이미 데이터를 방출하고 있습니다. 이는 이미 생성된 데이터 스트림이 Observer들에게 공유되는 동시성을 갖습니다.

```java
PublishSubject<Integer> hotObservable = PublishSubject.create();
hotObservable.onNext(1); // 데이터 방출
hotObservable.onNext(2); // 데이터 방출

hotObservable.subscribe(number -> System.out.println("Observer 1: " + number));
hotObservable.onNext(3); // 데이터 방출

hotObservable.subscribe(number -> System.out.println("Observer 2: " + number));
hotObservable.onNext(4); // 데이터 방출
```

위의 예시에서 `hotObservable`은 `PublishSubject`를 사용하여 생성되었습니다. 이미 생성된 데이터 스트림에 각각의 Observer가 subscribe하면, 해당 Observer는 동일한 데이터 스트림을 받아오게 됩니다.

### 요약
- Cold Observables는 Observer가 subscribe 할 때마다 새로운 데이터 스트림을 생성합니다.
- Hot Observables는 이미 생성된 데이터 스트림을 Observer들에게 공유합니다.
- Cold Observables는 독립적인 데이터 스트림을 가지지만, Hot Observables는 동일한 데이터 스트림을 공유합니다.

위에서 설명한 Hot Observables와 Cold Observables의 차이점을 이해하면, RxJava를 사용할 때 적합한 Observable 유형을 선택하는 데 도움이 될 것입니다.

[#RxJava](https://rxjava.dev/)
[#ReactiveProgramming](https://reactivex.io/)