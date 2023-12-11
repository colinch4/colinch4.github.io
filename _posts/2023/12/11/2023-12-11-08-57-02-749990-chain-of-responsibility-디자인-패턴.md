---
layout: post
title: "[swift] Chain of Responsibility 디자인 패턴"
description: " "
date: 2023-12-11
tags: [swift]
comments: true
share: true
---

Chain of Responsibility는 객체 간의 상호작용에서 발생하는 요청을 수신하는 객체들 간의 결합을 줄이는 디자인 패턴입니다. 이 패턴은 요청을 생성하는 객체와 이 요청을 처리하는 객체를 분리하여 서로에게 영향을 주지 않고 유연하게 상호작용할 수 있도록 합니다.

## 패턴 개요

이 패턴은 요청을 처리할 수 있는 여러 객체를 하나의 체인으로 연결하여 각 객체가 순차적으로 요청을 처리하도록 합니다. 요청을 처리할 객체가 없을 경우, 요청은 체인을 따라 전파되며, 처리 가능한 객체가 발견될 때까지 계속됩니다. 이 패턴은 객체 간의 결합을 약화시키고, 클라이언트와 서버 간의 유연한 통신을 가능하게 합니다.

## 구성 요소

### Handler

모든 처리자의 공통 인터페이스를 정의합니다. 이 인터페이스는 요청을 처리하는 메서드를 정의하며, 다음 처리자의 링크를 설정하고, 요청을 전달하는 방법도 포함합니다.

### ConcreteHandler

`Handler` 인터페이스를 구현하는 객체로, 자신이 처리할 수 있는 요청을 처리합니다. 또한 다음 처리자의 링크를 설정하여 요청을 전달하는 역할을 수행합니다.

### Client

요청을 생성하고 체인의 첫 번째 처리자에게 전달하는 객체입니다.

### 예제 코드

```swift
protocol Handler {
    var next: Handler? { get set }
    func handleRequest(request: Int)
}

class ConcreteHandler1: Handler {
    var next: Handler?
    
    func handleRequest(request: Int) {
        if request <= 10 {
            print("ConcreteHandler1 처리: \(request)")
        } else if let next = next {
            next.handleRequest(request: request)
        }
    }
}

class ConcreteHandler2: Handler {
    var next: Handler?
    
    func handleRequest(request: Int) {
        if request > 10 && request <= 20 {
            print("ConcreteHandler2 처리: \(request)")
        } else if let next = next {
            next.handleRequest(request: request)
        }
    }
}

class Client {
    var handler: Handler
    
    init(handler: Handler) {
        self.handler = handler
    }
    
    func makeRequest(request: Int) {
        handler.handleRequest(request: request)
    }
}

let handler1 = ConcreteHandler1()
let handler2 = ConcreteHandler2()
handler1.next = handler2

let client = Client(handler: handler1)
client.makeRequest(request: 5)
client.makeRequest(request: 15)
```

## 결론

Chain of Responsibility 디자인 패턴은 객체 간의 결합을 줄여 유연하고 확장 가능한 구조를 구축하는 데 유용합니다. 이 패턴을 사용하면 요청을 처리하는 방법을 동적으로 변경할 수 있으며, 새로운 처리자를 간단히 추가하여 시스템을 확장할 수 있습니다.

## 참고 자료
- [Design Patterns: Elements of Reusable Object-Oriented Software, Gang of Four](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)