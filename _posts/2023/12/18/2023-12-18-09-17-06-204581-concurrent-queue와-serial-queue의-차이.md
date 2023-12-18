---
layout: post
title: "[swift] Concurrent Queue와 Serial Queue의 차이"
description: " "
date: 2023-12-18
tags: [swift]
comments: true
share: true
---

Swift에서 Grand Central Dispatch(GCD)를 사용하여 동시성 작업을 처리할 때 Concurrent Queue와 Serial Queue를 사용할 수 있습니다. 그 둘의 차이를 이해한다면 작업을 효율적으로 관리하고 성능을 향상시킬 수 있습니다.

## Serial Queue

*Serial Queue*는 한 번에 하나의 작업만을 처리하며, 작업들을 순차적으로 실행합니다. 작업이 추가된 순서대로 한 작업이 끝나면 다음 작업을 시작합니다.

다음은 *Serial Queue*를 생성하고 작업을 추가하는 간단한 예제입니다.

```swift
let serialQueue = DispatchQueue(label: "com.example.serialQueue")
 
serialQueue.async {
   // 작업 처리
}
```

## Concurrent Queue

*Concurrent Queue*는 여러 작업을 동시에 처리할 수 있습니다. 하지만 *Serial Queue*처럼 작업들을 순차적으로 처리하지는 않습니다. 추가된 순서에 상관없이 여러 작업을 동시에 실행합니다.

다음은 *Concurrent Queue*를 생성하고 작업을 추가하는 예제입니다.

```swift
let concurrentQueue = DispatchQueue(label: "com.example.concurrentQueue", attributes: .concurrent)
 
concurrentQueue.async {
   // 작업 처리
}
```

## 결론

*Serial Queue*는 작업을 순차적으로 처리하는 데에 적합하고, *Concurrent Queue*는 여러 작업을 동시에 처리하는 데에 적합합니다. 상황에 맞게 적절한 Queue를 선택하여 프로그램 성능을 최적화할 수 있습니다.

여기서 *Serial Queue와 Concurrent Queue*에 대한 간단한 설명을 마치겠습니다.