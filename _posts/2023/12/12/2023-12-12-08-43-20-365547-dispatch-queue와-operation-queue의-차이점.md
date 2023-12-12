---
layout: post
title: "[swift] Dispatch Queue와 Operation Queue의 차이점"
description: " "
date: 2023-12-12
tags: [swift]
comments: true
share: true
---

iOS 및 macOS 앱에서 백그라운드 작업을 관리할 때는 보통 Dispatch Queue와 Operation Queue를 사용합니다. 이 두 가지 큐는 다양한 작업을 비동기적으로 실행하고 다른 스레드에서 작업을 관리하는 데 사용됩니다. 그러나 Dispatch Queue와 Operation Queue 사이에는 몇 가지 중요한 차이점이 있습니다.

## Dispatch Queue

Dispatch Queue는 **단순하고 가벼운 작업을 처리**하는 데 사용됩니다. 이 큐는 GCD(Grand Central Dispatch)를 기반으로 하며, 간단한 클로저나 함수를 사용하여 백그라운드에서 실행할 작업을 정의할 수 있습니다.

```swift
let queue = DispatchQueue(label: "com.example.queue")
queue.async {
    // background task
}
```

Dispatch Queue는 FIFO(먼저 온 것이 먼저 처리됨) 방식으로 작업을 처리하며, 큐의 우선 순위를 조절할 수 없습니다. 따라서 작업 간의 의존성을 설정하거나 작업을 취소하거나 다시 시도하는 등의 고급 기능을 제공하지 않습니다.

## Operation Queue

반면에, Operation Queue는 **더 복잡하고 고수준의 작업을 관리**하는 데 사용됩니다. 이 큐는 Operation 객체를 사용하여 작업을 정의하고, 작업 간의 의존성을 설정하거나 작업을 취소하거나 재시도하는 등의 고급 기능을 제공합니다.

```swift
let queue = OperationQueue()
let operation = BlockOperation {
    // background task
}
queue.addOperation(operation)
```

Operation Queue를 사용하면 작업 간의 의존성을 쉽게 처리하고, 작업의 실행 순서를 지정하고, 동시에 실행할 수있는 작업의 수를 제어하는 등의 유연성을 제공받을 수 있습니다.

## 결론

간단한 백그라운드 작업을 처리하는 경우에는 Dispatch Queue가 적합하며, 더 복잡하고 유연한 작업 관리가 필요한 경우에는 Operation Queue를 사용하는 것이 좋습니다. 두 큐를 적절하게 활용하여 앱의 성능을 최적화하는 것이 중요합니다.

참고: [Apple Developer Documentation](https://developer.apple.com/documentation/dispatch)