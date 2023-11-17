---
layout: post
title: "[swift] RxCocoa의 Observables과 Observers 개념"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

RxCocoa는 Swift에서 Reactive Programming을 구현하기 위한 프레임워크입니다. Observables과 Observers는 RxCocoa의 핵심 개념 중 일부입니다. 이들은 RxSwift와 함께 사용되어 비동기 이벤트 처리 및 데이터 흐름을 관리하는 데 도움을 줍니다.

## Observables

Observables는 데이터 스트림을 생성하는 것을 의미합니다. 이러한 스트림은 다양한 유형의 이벤트를 포함할 수 있으며, 데이터의 변화 또는 완료 여부 등을 나타낼 수 있습니다. Observables은 기본적으로 subscribe 메소드를 사용하여 Observers에게 이벤트를 전달합니다.

다음은 Observables를 생성하는 예제입니다.

```swift
import RxSwift

let observable = Observable<String>.create { observer in
    observer.onNext("Hello")
    observer.onNext("World")
    observer.onCompleted()

    return Disposables.create()
}
```

위의 예제에서는 `Observable<String>.create`를 사용하여 Observable을 생성합니다. `create` 메소드에는 클로저가 포함되어 있으며, 클로저 내부에서는 Observers에게 이벤트를 전달하는데 사용되는 onNext, onCompleted 등의 메소드를 호출할 수 있습니다.

## Observers

Observers는 Observables에서 발생하는 이벤트를 처리하기 위해 구독하는 개체입니다. Observers는 Observables의 데이터 스트림을 구독하고, 이벤트를 처리하며, 필요에 따라 추가 작업을 수행할 수 있습니다.

다음은 Observables를 구독하는 Observer의 예제입니다.

```swift
observable.subscribe { event in
    switch event {
    case .next(let value):
        print(value)
    case .completed:
        print("Completed")
    case .error(let error):
        print("Error: \(error.localizedDescription)")
    }
}
```

위의 예제에서는 `subscribe` 메소드를 사용하여 observable을 구독합니다. 구독 클로저는 이벤트를 처리하기 위한 코드를 포함합니다. 이 코드는 이벤트의 유형에 따라서 해당 작업을 수행합니다.

## 결론

RxCocoa의 Observables과 Observers는 Reactive Programming을 구현하는 데 중요한 역할을 합니다. Observables은 데이터 스트림을 생성하고, Observers는 이벤트를 처리하고 필요한 작업을 수행합니다. 이를 통해 비동기적인 이벤트 처리와 데이터 흐름을 용이하게 관리할 수 있습니다.

---

참고:

- [RxSwift GitHub repository](https://github.com/ReactiveX/RxSwift)
- [RxCocoa GitHub repository](https://github.com/ReactiveX/RxCocoa)