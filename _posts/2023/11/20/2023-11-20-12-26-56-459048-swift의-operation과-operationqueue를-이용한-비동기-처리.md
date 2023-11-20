---
layout: post
title: "[swift] Swift의 Operation과 OperationQueue를 이용한 비동기 처리"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

Swift는 비동기 처리를 위해 `Operation`과 `OperationQueue`라는 두 가지 클래스를 제공합니다. 이들을 사용하면 백그라운드에서 작업을 실행하고, 작업들을 관리하고 조율할 수 있습니다. 이번 블로그 포스트에서는 Swift의 `Operation` 및 `OperationQueue` 클래스를 사용하여 비동기 처리를 구현하는 방법에 대해 알아보겠습니다.

## Operation 클래스

`Operation` 클래스는 비동기 작업의 단위를 나타냅니다. 일반적으로 `Operation` 클래스를 상속받아 새로운 작업 클래스를 정의하고, `main()` 메서드를 오버라이드하여 실제 작업을 구현합니다.

```swift
class MyOperation: Operation {
    override func main() {
        // 비동기 작업을 수행하는 코드
    }
}
```

`main()` 메서드 내에서는 비동기 작업을 수행할 코드를 작성합니다. 이 작업은 백그라운드 스레드에서 실행되며, 작업이 완료될 때까지 기다리게 됩니다.

## OperationQueue 클래스

`OperationQueue` 클래스는 `Operation` 객체를 관리하고, 작업을 실행하는 용도로 사용됩니다. `OperationQueue`를 사용하여 작업을 추가하면, 해당 작업이 자동으로 생성된 스레드에서 실행되며 실행 순서는 `OperationQueue`에 의해 관리됩니다.

```swift
let operationQueue = OperationQueue()

let operation1 = MyOperation()
let operation2 = MyOperation()

operationQueue.addOperation(operation1)
operationQueue.addOperation(operation2)
```

위의 예시에서는 두 개의 작업인 `operation1`과 `operation2`를 `OperationQueue`에 추가하였습니다. 이후 `OperationQueue`는 할당된 스레드에서 작업을 실행하며, 작업의 실행 순서와 동시성을 조절합니다.

## 작업 간의 의존성 추가하기

`OperationQueue`를 사용하면 작업간의 의존성을 설정하여 작업 간의 순서를 정할 수 있습니다. 예를 들어, A 작업이 B 작업에 의존한다면, A 작업은 B 작업의 실행 완료를 기다려야만 실행됩니다.

```swift
let operationQueue = OperationQueue()

let operation1 = MyOperation()
let operation2 = MyOperation()

operation2.addDependency(operation1)

operationQueue.addOperation(operation1)
operationQueue.addOperation(operation2)
```

`operation2`가 `operation1`에 의존한다고 설정하려면 `addDependency()` 메서드를 사용합니다. 이후 `OperationQueue`에 작업들을 추가하면, `operation2`는 `operation1`이 완료될 때까지 기다린 후 실행됩니다.

## 작업의 상태 및 진행도 모니터링하기

`Operation` 및 `OperationQueue` 클래스를 사용하면 작업의 상태 및 진행도를 모니터링할 수 있습니다. `Operation` 클래스에는 작업의 진행 상태를 추적할 수 있는 `isExecuting`, `isFinished` 등의 속성이 있으며, `OperationQueue` 클래스에는 진행 중인 작업들의 진행 상태 정보를 제공하는 `operations` 속성이 있습니다.

## 결론

Swift의 `Operation` 및 `OperationQueue` 클래스를 사용하면 비동기 작업을 쉽게 구현하고 관리할 수 있습니다. 다양한 작업을 조율하고 작업 간의 의존성을 설정하여 복잡한 비동기 처리를 심플하게 구현할 수 있습니다. 관심있는 분들은 공식 Swift 문서에서 더 자세한 내용을 찾아보시기 바랍니다.

## 참고 자료
- [Apple Developer Documentation - Operation](https://developer.apple.com/documentation/foundation/operation)
- [Apple Developer Documentation - OperationQueue](https://developer.apple.com/documentation/foundation/operationqueue)