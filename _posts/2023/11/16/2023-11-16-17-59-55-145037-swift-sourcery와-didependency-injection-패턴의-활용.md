---
layout: post
title: "[swift] Swift Sourcery와 DI(Dependency Injection) 패턴의 활용"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 목차
- [Swift Sourcery란?](#swift-sourcery란)
- [DI(Dependency Injection)란?](#di-dependency-injection란)
- [Swift Sourcery와 DI 패턴의 결합](#swift-sourcery와-di-패턴의-결합)
- [결론](#결론)

## Swift Sourcery란?

Swift Sourcery는 Swift 코드 생성 도구로, 소스 코드를 분석하여 템플릿 기반으로 코드를 자동으로 생성할 수 있습니다. 이를 통해 반복적이고 지루한 작업을 줄여주고, 코드의 일관성과 유지보수성을 높일 수 있습니다. 

## DI(Dependency Injection)란?

DI는 의존성 주입을 의미하며, 객체 간의 의존 관계를 외부에서 설정하여 객체 간의 결합도를 낮추는 디자인 패턴입니다. DI를 사용하면 클래스간의 결합도를 낮출 수 있어 유연하고 테스트 가능한 코드를 작성할 수 있습니다.

## Swift Sourcery와 DI 패턴의 결합

Swift Sourcery와 DI 패턴을 결합하면 의존성 주입을 쉽게 구현할 수 있습니다. Sourcery를 사용하여 의존성 주입 코드를 자동 생성하면, 반복적인 작업을 줄이고 일관성 있는 코드를 유지할 수 있습니다.

예를 들어, DI 패턴을 사용하여 클래스 간의 의존 관계를 설정하는 경우, Sourcery를 사용하여 의존성 주입 코드를 자동으로 생성할 수 있습니다. 이렇게 생성된 코드는 컴파일 시점에 검증되므로 실수를 방지할 수 있습니다.

```swift
// Generated code by Sourcery

class DependencyContainer {
    static let shared = DependencyContainer()
    
    private init() {}
    
    func resolve<T>() -> T {
        // 의존성 주입 코드
    }
}

protocol Service {
    func performAction()
}

class ConcreteService: Service {
    // ...
}

class ViewController: UIViewController {
    let service: Service
    
    init(service: Service) {
        self.service = service
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // ...
}
```

위의 코드는 Sourcery를 사용하여 의존성 주입을 위한 코드를 자동으로 생성한 예시입니다. `DependencyContainer` 클래스는 의존성을 관리하고, `Service` 프로토콜을 준수하는 `ConcreteService` 클래스를 등록할 수 있습니다. `ViewController` 클래스는 `Service` 프로토콜에 의존하며, `init` 메서드를 통해 의존성을 주입받습니다.

## 결론

Swift Sourcery와 DI 패턴은 코드의 일관성과 유지보수성을 높이는 데 큰 도움을 줍니다. Sourcery를 사용하여 의존성 주입 코드를 자동으로 생성하면, 반복적인 작업을 줄이고 일관성 있는 코드를 작성할 수 있습니다. DI 패턴은 의존 관계를 외부에서 설정함으로써 유연하고 테스트 가능한 코드를 작성할 수 있게 해줍니다.

참고 자료:
- [Sourcery GitHub Repository](https://github.com/krzysztofzablocki/Sourcery)
- [Dependency Injection in Swift by John Sundell](https://www.swiftbysundell.com/articles/dependency-injection-in-swift/)
- [Dependency Injection in Swift using the Protocol-Oriented Approach by Bart Jacobs](https://www.avanderlee.com/swift/dependency-injection-in-swift/)