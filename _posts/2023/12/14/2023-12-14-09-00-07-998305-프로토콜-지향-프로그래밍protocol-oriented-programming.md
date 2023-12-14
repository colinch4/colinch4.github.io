---
layout: post
title: "[swift] 프로토콜 지향 프로그래밍(Protocol-Oriented Programming)"
description: " "
date: 2023-12-14
tags: [swift]
comments: true
share: true
---

프로토콜 지향 프로그래밍(Protocol-Oriented Programming, 이하 POP)은 객체 지향 프로그래밍과 함께 사용되는 디자인 패러다임 중 하나입니다. POP은 객체 지향 프로그래밍과 달리 데이터 처리와 동작 모두에 대해 프로토콜을 활용합니다.

## 프로토콜이란 무엇인가?
프로토콜은 메서드, 프로퍼티 및 기타 요구사항의 청사진을 정의하는데 사용됩니다. 클래스, 구조체 또는 열거형은 해당 프로토콜을 채택하여 요구되는 기능을 구현할 수 있습니다. 이를 통해 타입 간의 일관성을 유지하면서 유연한 코드 구조를 달성할 수 있습니다.

## POP의 장점
POP은 상속보다는 프로토콜을 활용하여 코드 재사용을 강화하는데 주안점을 두고 있습니다. 이를 통해 다형성을 지원하면서 더욱 모듈화된 코드를 작성할 수 있습니다. 또한 프로토콜을 활용한 코딩은 테스트 용이성을 향상시키고, 더 나은 성능을 제공합니다. 또한 다중 상속 문제를 해결하여 코드 유지 보수성과 안정성을 향상시킵니다.

## 예제
```swift
protocol Vehicle {
    var wheels: Int { get }
    func start()
    func stop()
}

struct Car: Vehicle {
    var wheels: Int = 4
    func start() {
        // start car
    }
    func stop() {
        // stop car
    }
}

struct Bike: Vehicle {
    var wheels: Int = 2
    func start() {
        // start bike
    }
    func stop() {
        // stop bike
    }
}
```

위의 예제에서 `Vehicle` 프로토콜은 `start()` 및 `stop()` 메서드를 요구하며, `Car` 및 `Bike` 구조체는 해당 프로토콜을 채택하여 요구된 메서드를 구현합니다.

## 결론
POP은 Swift의 강력한 기능 중 하나이며, 코드의 유연성과 안정성을 향상시키는 데 많은 도움이 됩니다. 객체 지향 패러다임과 결합하여 사용하면 보다 효과적인 코드 설계와 개발을 할 수 있습니다.

참고 문헌:
- [The Swift Programming Language - Protocols](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html)
- [Apple - Protocol-Oriented Programming in Swift](https://developer.apple.com/videos/play/wwdc2015/408/)
- [Advantages of Protocol Oriented Programming in Swift](https://medium.com/flawless-app-stories/advantages-of-protocol-oriented-programming-in-swift-144d9d767b40)