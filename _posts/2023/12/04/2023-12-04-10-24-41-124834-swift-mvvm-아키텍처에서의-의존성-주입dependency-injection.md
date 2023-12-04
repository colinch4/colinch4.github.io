---
layout: post
title: "[swift] Swift MVVM 아키텍처에서의 의존성 주입(Dependency Injection)"
description: " "
date: 2023-12-04
tags: [swift]
comments: true
share: true
---

MVVM(Model-View-ViewModel) 아키텍처는 Swift 개발에서 많이 사용되는 패턴 중 하나입니다. 이 아키텍처는 코드의 구조를 체계적으로 유지하고 각각의 역할에 맞게 코드를 분리하여 유지보수성을 높이는 장점이 있습니다. 그러나 MVVM 아키텍처에서는 종종 의존성 주입(Dependency Injection)이 필요한 경우가 있습니다.

의존성 주입은 객체 간의 결합도를 낮추기 위해 사용되는 디자인 패턴입니다. 이 패턴을 사용하면 객체 간의 의존 관계를 외부에서 동적으로 제공할 수 있으므로 코드의 유연성과 재사용성을 증가시킬 수 있습니다.

MVVM 아키텍처에서의 의존성 주입은 주로 ViewModel과 관련된 객체들 사이에서 이루어집니다. ViewModel은 Model과 View 사이의 중재자 역할을 하며, Model로부터 데이터를 가져와 View에게 전달하거나 View로부터의 사용자 입력을 Model에게 전달하는 역할을 합니다. 이때 ViewModel은 Model 객체에 의존하게 됩니다.

일반적으로 의존성 주입은 생성자 주입(Constructor Injection)이 가장 많이 사용됩니다. 생성자 주입은 의존하는 객체를 생성자 매개변수로 전달받는 방식으로 이루어집니다. 이를 통해 의존하는 객체의 타입이 변경되더라도 해당 객체를 사용하는 코드를 수정할 필요가 없게 됩니다.

```swift
class ViewModel {
    let model: Model
    
    init(model: Model) {
        self.model = model
    }
    
    // ViewModel의 나머지 코드
}
```

위의 코드에서 ViewModel은 생성자를 통해 Model 객체를 전달받고, 전달받은 Model 객체를 속성으로 저장합니다. 이렇게 생성된 ViewModel은 Model 객체와의 의존성을 외부에서 주입받게 됩니다. 이후 ViewModel에서 Model 객체를 사용하거나 호출할 때는 주입받은 model 속성을 참조합니다.

의존성 주입을 사용하면 ViewModel의 테스트가 용이해지며, Model 객체에 대한 다른 구현체를 쉽게 전달할 수도 있습니다. 또한, 여러 ViewModel에서 동일한 Model 객체를 공유하는 경우에도 의존성 주입을 통해 이를 처리할 수 있습니다.

MVVM 아키텍처에서 의존성 주입은 코드를 더 유연하고 테스트 가능하게 만들어줍니다. 이를 통해 개발자는 앱의 복잡도를 낮출 수 있으며, 코드를 보다 개선된 구조로 설계할 수 있습니다.

## 참고 자료
- [Swift: The MVVM Design Pattern](https://www.raywenderlich.com/6733535-the-mvvm-design-pattern)
- [Dependency Injection in Swift](https://www.swiftbysundell.com/articles/dependency-injection-in-swift/)