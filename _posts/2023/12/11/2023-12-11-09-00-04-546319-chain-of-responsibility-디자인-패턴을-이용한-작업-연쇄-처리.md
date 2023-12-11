---
layout: post
title: "[swift] Chain of Responsibility 디자인 패턴을 이용한 작업 연쇄 처리"
description: " "
date: 2023-12-11
tags: [swift]
comments: true
share: true
---

작업 연쇄 처리는 객체들 사이에 작업을 순차적으로 전달하여 처리하는 디자인 패턴입니다. 이때, 처리를 담당하는 객체들은 연쇄를 이루며, 각 객체는 작업을 처리하거나 다음 처리자로 작업을 전달할 수 있습니다. Chain of Responsibility 패턴을 이용하여 이런 작업 연쇄 처리를 구현할 수 있습니다.

## 패턴 구현 예시

아래는 Swift 언어를 사용하여 Chain of Responsibility 디자인 패턴을 이용한 작업 연쇄 처리의 간단한 예시 코드입니다.

```swift
// 작업을 처리하는 추상 클래스
protocol Handler {
    var nextHandler: Handler? { get set }
    func handleRequest(request: String)
}

// 실제 작업을 처리하는 클래스
class ConcreteHandlerA: Handler {
    var nextHandler: Handler?
    
    func handleRequest(request: String) {
        if request == "A" {
            // 작업 처리 로직
        } else {
            nextHandler?.handleRequest(request: request)
        }
    }
}

class ConcreteHandlerB: Handler {
    var nextHandler: Handler?
    
    func handleRequest(request: String) {
        if request == "B" {
            // 작업 처리 로직
        } else {
            nextHandler?.handleRequest(request: request)
        }
    }
}

// 클라이언트
class Client {
    private var handler: Handler
    
    init(handler: Handler) {
        self.handler = handler
    }
    
    func executeRequest(request: String) {
        handler.handleRequest(request: request)
    }
}
```

이 예시 코드에서는 `Handler` 프로토콜을 정의하고, `ConcreteHandlerA`와 `ConcreteHandlerB` 클래스가 이를 구현합니다. `Client` 클래스는 작업을 실제로 전달하고 처리합니다.

## 패턴의 장점

Chain of Responsibility 패턴을 사용하면 작업 처리자간의 결합도를 낮출 수 있습니다. 각 처리자는 자신의 역할에만 집중하며 다음 처리자에 대한 정보만 가지고 있으면 됩니다. 이로써 유연한 설계가 가능하며, 새로운 처리자를 추가하거나 기존의 처리자를 변경하더라도 다른 처리자에 영향을 주지 않습니다.

## 결론

Chain of Responsibility 디자인 패턴을 이용한 작업 연쇄 처리는 복잡한 작업 처리 과정을 분리하여 각 단계별로 담당하도록 설계할 수 있게 합니다. 이를 통해 유연하고 확장 가능한 시스템을 구축할 수 있습니다. Swift와 같은 객체지향 언어에서 이 디자인 패턴을 적용하여 가독성 높고 유지보수가 용이한 코드를 작성하는 데 도움이 됩니다.

## 참고문헌
- [Design Patterns: Elements of Reusable Object-Oriented Software (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides)](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented-dp-0201633612/dp/0201633612/)
- [Refactoring.Guru - Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)