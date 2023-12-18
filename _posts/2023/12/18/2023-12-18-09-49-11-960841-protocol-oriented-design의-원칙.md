---
layout: post
title: "[swift] Protocol Oriented Design의 원칙"
description: " "
date: 2023-12-18
tags: [swift]
comments: true
share: true
---

Protocol Oriented Design은 Swift 프로그래밍 언어에서 강력한 개념이며, 아래의 원칙으로 구성됩니다.

1. **Protocol and Protocol Extensions**

2. **Composition over Inheritance**

3. **Generics**

4. **Value Semantics**

아래에서 각 원칙에 대해 자세히 알아보겠습니다.

## Protocol and Protocol Extensions

`Protocol`은 형식적으로 메소드, 프로퍼티 및 기타 멤버의 요구 사항을 정의합니다. `Protocol`은 다른 `class`, `struct`, 또는 `enum`들에서 채택하여 그 요구 사항을 구현할 수 있습니다. `Protocol`에는 기본 구현이 포함되어 있지 않으므로, `Protocol Extensions`을 통해 공통 기능을 제공할 수 있습니다.

```swift
protocol Vehicle {
    var numberOfWheels: Int { get }
    func start()
}

extension Vehicle {
    func start() {
        print("Starting the vehicle")
    }
}
```

## Composition over Inheritance

상속보다는 합성을 선호하는 것이 `Protocol Oriented Design`의 핵심 원리 중 하나입니다. `Protocol`를 사용하여 코드를 재사용하고, 더 작고 모듈화된 형태의 코드를 작성할 수 있습니다.

```swift
protocol CanFly {
    func fly()
}

protocol CanSwim {
    func swim()
}

struct Bird: CanFly {
    func fly() {
        print("Bird is flying")
    }
}

struct Duck: CanFly, CanSwim {
    func fly() {
        print("Duck is flying")
    }

    func swim() {
        print("Duck is swimming")
    }
}
```

## Generics

`Generics`를 사용하여 타입에 종속되지 않는 유연한 코드를 작성할 수 있습니다. 이는 `Protocol`과 함께 사용할 때 더욱 강력한 기능을 발휘합니다.

```swift
protocol Stack {
    associatedtype Element
    mutating func push(_ item: Element)
    mutating func pop() -> Element?
}

struct IntStack: Stack {
    private var items = [Int]()
    
    mutating func push(_ item: Int) {
        items.append(item)
    }
    
    mutating func pop() -> Int? {
        return items.popLast()
    }
}
```

## Value Semantics

`Struct`와 `Enum`은 값 타입이며, `Value Semantics`을 따릅니다. 이러한 타입은 변경되지 않는다는 보장이 있고, 이에 따라 코드의 예상치 못한 동작을 방지할 수 있습니다.

이러한 원칙을 적용하여 `Protocol Oriented Design`을 구축하면 유연하고 확장 가능한 코드를 작성할 수 있습니다.

### References
- [Protocol-Oriented Programming in Swift](https://developer.apple.com/videos/play/wwdc2015/408/)
- [Swift.org - Protocol-Oriented Programming](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html#)
- [Advanced Swift: Protocol-Oriented Programming - Ray Wenderlich](https://www.raywenderlich.com/6568921-advanced-swift-protocol-oriented-programming)