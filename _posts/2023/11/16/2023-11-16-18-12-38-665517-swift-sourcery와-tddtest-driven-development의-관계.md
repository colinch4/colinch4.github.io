---
layout: post
title: "[swift] Swift Sourcery와 TDD(Test-Driven Development)의 관계"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

![Image](https://www.example.com/swift_sourcery_tdd.png)

## 소개

Swift Sourcery는 Swift 코드 생성 도구로, 소스 코드를 분석하고 템플릿을 이용하여 소스 코드를 생성할 수 있습니다. TDD(Test-Driven Development)는 소프트웨어 개발 방법론 중 하나로, 테스트 코드를 먼저 작성하고 이를 통과하기 위한 코드를 작성하는 방식입니다.

이번 글에서는 Swift Sourcery와 TDD의 관계에 대해 살펴보겠습니다.

## Swift Sourcery와 TDD

Swift Sourcery는 코드를 자동으로 생성해주는 도구이므로, TDD 방식의 개발에 적합한 도구입니다. TDD를 사용하면 테스트 코드를 먼저 작성하고 이를 통과하는 코드를 만들어야 하기 때문에, 코드 생성 도구를 사용하여 보일러플레이트 코드를 줄일 수 있습니다.

보일러플레이트 코드란, 비슷한 기능을 하는 코드들이 반복적으로 작성되는 코드를 말합니다. 예를 들어, 데이터 모델을 생성하는 코드들이 서로 비슷한 패턴을 가지고 있는 경우, 이를 템플릿을 이용하여 자동으로 생성할 수 있습니다.

Swift Sourcery를 사용하여 코드를 자동 생성하면, 개발자는 TDD 방식으로 코드를 작성할 때 집중할 수 있는 시간과 에너지를 확보할 수 있습니다. 보일러플레이트 코드의 생성을 자동화하고, 테스트 코드와 실제 코드를 작성하는 작업을 분리하여 생산성을 향상시킬 수 있습니다.

## 예시

```swift
// MyModel.swift
// Sourcery annotation: AutoMockable

protocol MyModelProtocol {
    var name: String { get }
    var age: Int { get }
}

struct MyModel: MyModelProtocol {
    let name: String
    let age: Int
}
```

위 코드에서는 `AutoMockable`이라는 Sourcery annotation을 사용하여 `MyModel` 프로토콜을 생성하는 템플릿이 있습니다. 이 템플릿을 사용하면, `MyModel`을 준수하는 모델을 생성할 때 자동으로 해당 프로토콜을 구현한 코드가 생성됩니다.

이렇게 생성된 코드를 사용하면, 테스트 코드에서 모델의 프로퍼티를 직접 초기화하는 부분을 제거할 수 있고, 테스트 대상 코드를 더 집중적으로 작성할 수 있게 됩니다.

## 결론

Swift Sourcery는 TDD 개발 방법론과 잘 맞는 도구입니다. 코드 생성을 통해 보일러플레이트 코드 작성을 자동화하고, 테스트 코드와 실제 코드 작성을 분리함으로써 개발자의 생산성을 향상시킬 수 있습니다.

따라서, Swift Sourcery를 TDD와 함께 사용하여 더 효율적이고 유지보수가 용이한 코드를 작성할 수 있습니다.

## 참고 자료

- [Swift Sourcery 공식 문서](https://github.com/krzysztofzablocki/Sourcery)
- [Sourcery를 사용한 Swift 코드 생성](https://sweettutos.com/2021/02/28/generate-code-with-sourcery-in-swift/)
- [Test-Driven Development with Swift](https://www.amazon.com/Test-Driven-Development-Swift-Apple-Platforms/dp/1680502355)