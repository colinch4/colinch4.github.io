---
layout: post
title: "[swift] GCD(Grand Central Dispatch)에 대한 이해"
description: " "
date: 2023-12-05
tags: [swift]
comments: true
share: true
---

GCD(Grand Central Dispatch)는 iOS 및 macOS 앱 개발을 위한 동시성 프로그래밍 프레임워크입니다. 이를 사용하면 앱 내에서 동시에 여러 작업을 처리하고, 병렬로 실행되는 작업을 효율적으로 관리할 수 있습니다.

## GCD의 주요 개념

### Dispatch Queue
GCD에서 작업은 Dispatch Queue에 의해 관리됩니다. Dispatch Queue는 작업을 실행하는 스레드의 개념으로 생각할 수 있습니다. 크게 두 가지 유형의 Dispatch Queue가 있습니다.

1. Serial Queue: 작업을 직렬로 실행하는 큐로, 한 번에 하나의 작업만이 실행됩니다. 앞선 작업이 모두 완료된 후에 다음 작업이 실행됩니다.
2. Concurrent Queue: 작업을 병렬로 실행하는 큐로, 동시에 여러 작업이 실행될 수 있습니다.

### Dispatch Work Item
작업은 Dispatch Work Item으로 캡슐화됩니다. 각 작업은 클로저 또는 블록으로 표현될 수 있으며, 필요한 경우 작업의 우선순위 설정 등 다양한 속성을 지정할 수 있습니다.

### Main Queue
GCD의 기본 큐로, UI 업데이트와 같은 작업을 UI 스레드에서 수행하기 위해 사용됩니다. Main Queue는 Serial Queue의 일종이며, 앱의 메인 스레드에서 실행됩니다.

## GCD 사용 예시

```swift
// Serial Queue 생성
let serialQueue = DispatchQueue(label: "com.example.serialQueue")

// Concurrent Queue 생성
let concurrentQueue = DispatchQueue(label: "com.example.concurrentQueue", attributes: .concurrent)

// 작업 예시
let workItem = DispatchWorkItem {
    // 작업을 수행하는 코드 작성
    print("Hello, GCD!")
}

// Serial Queue에서 작업 실행
serialQueue.async(execute: workItem)

// Concurrent Queue에서 작업 실행
concurrentQueue.async(execute: workItem)

// Main Queue에서 UI 업데이트 작업 실행
DispatchQueue.main.async {
    // UI 업데이트 코드 작성
    self.label.text = "Hello, GCD!"
}

```

위 예시에서는 먼저 Serial Queue와 Concurrent Queue를 각각 생성합니다. 작업은 DispatchWorkItem을 생성하여 작업 내용을 클로저로 작성합니다. 그런 다음, 각각의 Queue에서 작업을 실행하거나 Main Queue에서 UI 업데이트 작업을 실행하는 예시를 보여줍니다.

## 결론

GCD는 앱 개발에서 동시성 작업을 효율적으로 처리하는 데 도움을 주는 강력한 도구입니다. Dispatch Queue와 Dispatch Work Item을 활용하여 앱의 성능을 향상시키고, 다양한 작업을 병렬 또는 직렬로 실행할 수 있습니다.

---

참고 자료:
- [Apple Developer Documentation - Grand Central Dispatch](https://developer.apple.com/documentation/dispatch)
- [RayWenderlich - Grand Central Dispatch Tutorial for Swift](https://www.raywenderlich.com/5370-grand-central-dispatch-tutorial-for-swift-4-part-1-2)