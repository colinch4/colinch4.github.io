---
layout: post
title: "[swift] AsyncSequence와 AsyncIterator의 사용 방법"
description: " "
date: 2023-12-11
tags: [swift]
comments: true
share: true
---

## 소개

비동기 코드를 작성할 때, Swift에서는 `AsyncSequence`와 `AsyncIterator`를 활용할 수 있습니다. 이 두 가지 프로토콜은 비동기적으로 데이터를 생성하고 소비할 수 있도록 도와줍니다. 이번 블로그에서는 이 두 프로토콜의 사용 방법에 대해 알아보겠습니다.

- [AsyncSequence](#asyncsequence)  
- [AsyncIterator](#asynciterator)  

## AsyncSequence

`AsyncSequence`는 비동기적 요소를 생성하는 시퀀스를 나타내는 프로토콜입니다. 예를 들어 비동기적으로 원격에서 데이터를 읽거나, 비동기적으로 처리된 데이터를 반환하는 경우에 활용할 수 있습니다.

아래는 `AsyncSequence`를 사용하여 비동기적으로 데이터를 생성하고 처리하는 간단한 예제입니다. 

```swift
import Foundation

struct MyAsyncSequence: AsyncSequence {
    typealias Element = Int

    func makeAsyncIterator() -> MyAsyncIterator {
        return MyAsyncIterator()
    }
}

struct MyAsyncIterator: AsyncIteratorProtocol {
    mutating func next() async -> Int? {
        await Task.sleep(1_000_000_000) // 1초 대기
        return Int.random(in: 1...100)
    }
}

@MainActor func processAsyncSequence() async {
    var sum = 0
    for await number in MyAsyncSequence() {
        sum += number
    }
    print("Sum of random numbers: \(sum)")
}

Task {
    await processAsyncSequence()
}
```

이 예제에서는 `makeAsyncIterator` 메서드를 사용하여 `MyAsyncIterator`를 생성하고, `next` 메서드 내에서 비동기적으로 요소를 반환합니다. 이를 활용하여 `AsyncSequence`를 사용할 수 있습니다.

## AsyncIterator

`AsyncIterator`는 비동기적인 방식으로 요소를 반복적으로 소비할 수 있도록 하는 프로토콜입니다. `next` 메서드를 사용하여 비동기적으로 다음 요소를 반환합니다.

위에서 작성한 코드와 함께, `AsyncIterator`를 활용하여 비동기적으로 요소를 순회하는 방법을 살펴보았습니다.

이러한 방식을 통해, Swift에서는 `AsyncSequence`와 `AsyncIterator`를 사용하여 비동기적으로 데이터를 생성하고 처리하는 방법에 대해 유연하게 다룰 수 있습니다.

## 결론

위에서 살펴본 것과 같이 `AsyncSequence`와 `AsyncIterator` 프로토콜을 사용하여 비동기적인 작업을 쉽게 다룰 수 있습니다. 이를 활용하면 복잡한 비동기 코드를 간결하게 작성할 수 있는 장점이 있습니다.