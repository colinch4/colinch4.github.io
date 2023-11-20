---
layout: post
title: "[swift] Swift의 GCD (Grand Central Dispatch)를 이용한 비동기 처리"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

Swift 언어는 GCD (Grand Central Dispatch)를 이용하여 비동기 처리를 할 수 있는 강력한 기술을 제공합니다. GCD는 멀티코어 시스템에서 작업을 효율적으로 분배하고 처리하는 방법을 제공하여 앱의 성능을 향상시킬 수 있습니다.

## GCD의 기본 개념

GCD는 큐 (queue) 기반으로 동작합니다. 큐는 작업들이 순서대로 쌓여서 처리될 수 있도록 관리하는 역할을 합니다. GCD는 두 가지 유형의 큐를 제공합니다.

1. Serial Queue: 작업들이 순차적으로 실행되는 큐입니다. 한 번에 하나의 작업만 처리됩니다.
2. Concurrent Queue: 여러 작업이 병렬로 실행되는 큐입니다. 여러 개의 작업이 동시에 처리될 수 있습니다.

## 비동기 처리 예제

비동기 처리를 예제를 통해 살펴보겠습니다. 아래는 GCD를 사용하여 이미지 다운로드를 비동기적으로 처리하는 코드입니다.

```swift
DispatchQueue.global().async {
    // 비동기 작업을 수행하기 위한 코드
    
    // 이미지 다운로드
    guard let url = URL(string: "https://example.com/image.jpg") else { return }
    guard let data = try? Data(contentsOf: url) else { return }
    guard let image = UIImage(data: data) else { return }
    
    // 다운로드 완료 후 UI 업데이트
    DispatchQueue.main.async {
        imageView.image = image
    }
}
```

위의 코드에서 `DispatchQueue.global().async`를 사용하여 이미지 다운로드 작업을 비동기적으로 실행합니다. 다운로드 작업은 백그라운드 스레드에서 처리되며, `DispatchQueue.main.async`를 사용하여 다운로드가 완료된 후에 UI 업데이트를 수행합니다. 이렇게 비동기 처리를 함으로써 앱이 멈추지 않고 사용자에게 응답성을 제공할 수 있습니다.

## 참고 자료

- [Apple Developer Documentation - Grand Central Dispatch](https://developer.apple.com/documentation/dispatch)
- [Ray Wenderlich - Grand Central Dispatch Tutorial for Swift](https://www.raywenderlich.com/5370-grand-central-dispatch-tutorial-for-swift-4-part-1-2)
- [Swift.org - Concurrency](https://swift.org/blog/concurrency/)