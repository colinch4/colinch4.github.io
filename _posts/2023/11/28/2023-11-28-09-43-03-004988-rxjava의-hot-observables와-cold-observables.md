---
layout: post
title: "[java] RxJava의 Hot Observables와 Cold Observables"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

RxJava는 ReactiveX의 자바 구현체로서, 비동기 및 이벤트 기반 프로그래밍을 쉽게 처리할 수 있는 도구입니다. RxJava에서는 Observable 패턴을 사용하여 데이터 스트림을 생성하고 주고 받을 수 있습니다. Observable은 두 가지 유형으로 나뉘는데, Hot Observables와 Cold Observables가 있습니다.

## Cold Observables

Cold Observables는 Observables이 데이터 스트림을 발행할 때 마다 새로운 값을 생성하는 방식입니다. 매번 새로운 Subscriber가 Observable에 구독할 때마다, 독립적인 데이터 스트림이 생성됩니다. 각 Subscriber는 중복되지 않는 값을 독립적으로 받게되므로, 동시에 여러 Subscriber가 데이터를 처리할 수 있습니다.

```
Observable<Integer> coldObservable = Observable.just(1, 2, 3, 4, 5);

coldObservable.subscribe(value -> {
    // 데이터 처리
});

coldObservable.subscribe(value -> {
    // 다른 데이터 처리
});
```

위의 코드에서 `Observable.just()` 메서드로 생성된 Cold Observables는 매번 독립적인 데이터 스트림을 생성합니다. 따라서 두 개의 Subscriber가 각자 독립적인 데이터를 받아서 처리할 수 있게 됩니다.

## Hot Observables

반면, Hot Observables는 데이터 스트림을 공유하고 동시에 여러 Subscriber에게 전달하는 방식입니다. Hot Observables는 이미 데이터를 발행하고 있을 때 Subscriber가 구독하여 데이터를 받습니다. 따라서 Subscriber는 처음부터 데이터를 받지 못할 수도 있습니다.

Hot Observables는 `ConnectableObservable`을 사용하여 생성할 수 있으며, `connect()` 메서드를 호출하여 데이터 스트림을 시작할 수 있습니다.

```
ConnectableObservable<Integer> hotObservable = Observable.just(1, 2, 3, 4, 5).publish();

hotObservable.subscribe(value -> {
    // 데이터 처리
});

hotObservable.subscribe(value -> {
    // 다른 데이터 처리
});

hotObservable.connect();
```

위의 코드에서는 `Observable.just().publish()`를 사용하여 Hot Observables를 생성하고, `connect()` 메서드로 데이터 스트림을 시작합니다. 이후 각 Subscriber가 데이터를 받게 됩니다. Hot Observables는 같은 데이터를 여러 Subscriber에게 동시에 전달하므로, 데이터의 손실이 발생할 수 있습니다.

## 결론

RxJava에서는 Hot Observables와 Cold Observables를 구분하여 사용할 수 있습니다. Cold Observables는 매번 새로운 Subscriber에게 독립적인 데이터 스트림을 생성하여 처리하는 반면, Hot Observables는 이미 생성된 데이터 스트림을 공유하고 여러 Subscriber에게 동시에 전달합니다. 적절한 상황에 맞게 사용하여 비동기 및 이벤트 기반 프로그래밍을 유연하게 처리할 수 있습니다.

---

참고:
- [RxJava Documentation](https://github.com/ReactiveX/RxJava)
- [ReactiveX Documentation](http://reactivex.io/documentation)
- [Introduction to RxJava](https://code.tutsplus.com/tutorials/getting-started-with-reactivex-programming-in-java--cms-28396)