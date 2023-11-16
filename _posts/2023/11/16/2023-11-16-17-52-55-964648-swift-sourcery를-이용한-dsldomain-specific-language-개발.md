---
layout: post
title: "[swift] Swift Sourcery를 이용한 DSL(Domain-Specific Language) 개발"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 개요
DSL(Domain-Specific Language)은 특정 도메인에 특화된 언어로, 해당 도메인의 문제를 해결하기 위해 사용됩니다. Swift는 강력한 메타 프로그래밍 기능을 제공하여, 소스 코드를 생성하고 변환하는 기능을 수행할 수 있습니다. 이번 글에서는 Swift Sourcery를 이용하여 DSL을 개발하는 방법에 대해 알아보겠습니다.

## Swift Sourcery란?
Swift Sourcery는 Swift 코드 생성 도구로, 소스 코드를 분석하여 템플릿에 정의된 코드를 생성할 수 있습니다. 이를 통해 자동으로 반복적이고 지루한 코드 작성 작업을 대신해 줄 수 있습니다. Swift Sourcery는 주석과 어노테이션을 이용해 코드의 생성 규칙을 정의할 수 있습니다.

## DSL 개발 방법
1. Sourcery 설치하기: Swift 프로젝트에서 Swift Sourcery를 사용하기 위해서는 먼저 Sourcery를 설치해야 합니다. [Sourcery 공식 문서](https://github.com/krzysztofzablocki/Sourcery)를 참고하여 설치합니다.

2. 도메인 모델 정의하기: 먼저 DSL을 개발하기 위해 어떤 도메인에 특화된 언어를 개발할지 정의해야 합니다. 예를 들어, 수학 연산 DSL을 개발하고 싶다면 연산자와 함수 등을 설계합니다.

3. 템플릿 작성하기: Sourcery는 소스 코드를 분석하여 템플릿에 정의된 코드를 생성합니다. 따라서 템플릿 파일을 작성해야 합니다. 템플릿에는 생성할 코드의 형식과 규칙을 기술합니다. 예를 들어, 수학 연산 DSL을 위한 템플릿에는 +, -, *, / 연산자를 처리할 로직이 포함될 수 있습니다.

4. 어노테이션 추가하기: DSL로 사용할 코드에는 어노테이션을 추가해야 합니다. 이 어노테이션은 Sourcery에서 분석할 때 사용될 정보를 정의하는 역할을 합니다. 어노테이션을 통해 해당 코드가 DSL로 사용될 것임을 명시할 수 있습니다.

5. 코드 생성하기: Sourcery를 실행하여 코드를 생성합니다. Sourcery는 소스 코드를 분석하고, 템플릿을 적용하여 실제 코드를 생성합니다. 이렇게 생성된 코드는 기존 코드와 함께 프로젝트에 추가되어 사용될 수 있습니다.

## 예시 코드

```swift
// Sourcery 어노테이션을 추가하여 DSL로 사용될 코드를 정의합니다.
// 연산자를 사용한 수학 연산 DSL 예시입니다.

// sourcery: DSL
struct MathDSL {
    var value: Double

    // sourcery: DSLFunction
    func add(_ value: Double) -> MathDSL {
        return MathDSL(value: self.value + value)
    }

    // sourcery: DSLFunction
    func subtract(_ value: Double) -> MathDSL {
        return MathDSL(value: self.value - value)
    }

    // sourcery: DSLFunction
    func multiply(_ value: Double) -> MathDSL {
        return MathDSL(value: self.value * value)
    }

    // sourcery: DSLFunction
    func divide(_ value: Double) -> MathDSL {
        return MathDSL(value: self.value / value)
    }
}

// Sourcery 템플릿을 작성합니다.
// Sourcery는 소스 코드를 분석하여 템플릿에 정의된 코드를 자동으로 생성합니다. 

// sourcery:inline:MathDSL
extension MathDSL {
    // Add 연산자를 사용한 연산 코드를 작성합니다.
    static func + (lhs: MathDSL, rhs: Double) -> MathDSL {
        return lhs.add(rhs)
    }

    // Subtract 연산자를 사용한 연산 코드를 작성합니다.
    static func - (lhs: MathDSL, rhs: Double) -> MathDSL {
        return lhs.subtract(rhs)
    }

    // Multiply 연산자를 사용한 연산 코드를 작성합니다.
    static func * (lhs: MathDSL, rhs: Double) -> MathDSL {
        return lhs.multiply(rhs)
    }

    // Divide 연산자를 사용한 연산 코드를 작성합니다.
    static func / (lhs: MathDSL, rhs: Double) -> MathDSL {
        return lhs.divide(rhs)
    }
}
// sourcery:end

// 사용 예시
let result = MathDSL(value: 10) + 5 - 3 * 2 / 4
print(result.value) // output: 10.5
```

## 결론
Swift Sourcery를 이용하여 DSL을 개발할 수 있습니다. DSL은 특정 도메인에 특화된 언어로, Swift의 메타 프로그래밍 기능을 활용하여 소스 코드를 생성하고 변환할 수 있습니다. DSL을 개발하면 반복적이고 지루한 작업을 자동으로 처리할 수 있으며, 코드 가독성을 향상시킬 수 있습니다.

## 참고 자료
- [Sourcery 공식 문서](https://github.com/krzysztofzablocki/Sourcery)
- [Swift DSL을 통해 코드 품질 향상하기](https://www.swiftbysundell.com/articles/swift-dsls/)
- [Building a Domain Specific Language in Swift](https://academy.realm.io/posts/writing-a-dsl-in-swift/)