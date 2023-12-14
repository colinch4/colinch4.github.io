---
layout: post
title: "[swift] 더하기 연산자의 오버로딩(Operator Overloading for the + Operator)"
description: " "
date: 2023-12-14
tags: [swift]
comments: true
share: true
---

Swift에서 연산자를 오버로딩하여 사용자 정의 타입에 대해 새로운 동작을 지정할 수 있습니다. 더하기(+) 연산자는 두 개의 숫자를 더하는 데 사용할 수 있지만, 사용자 정의 타입의 인스턴스에 대해서도 추가적인 동작을 정의할 수 있습니다.

다음은 Swift에서 더하기 연산자를 오버로딩하여 두 벡터를 더하는 예제 코드입니다.

```swift
struct Vector {
    var x: Double
    var y: Double
    
    static func + (left: Vector, right: Vector) -> Vector {
        return Vector(x: left.x + right.x, y: left.y + right.y)
    }
}
```

위 코드에서 `+` 연산자를 오버로딩하여 두 개의 `Vector` 인스턴스를 더하고 새로운 `Vector` 인스턴스를 반환합니다.

이제 두 `Vector` 인스턴스를 더할 수 있습니다.

```swift
let v1 = Vector(x: 3.0, y: 4.0)
let v2 = Vector(x: 1.5, y: 2.5)
let result = v1 + v2
print(result) // 출력: Vector(x: 4.5, y: 6.5)
```

더하기 연산자를 오버로딩하여 사용자 정의 타입에 대해 새로운 동작을 추가하면 코드를 더 읽기 쉽고 직관적으로 만들 수 있습니다. 이것은 Swift의 강력한 기능 중 하나입니다.

더 많은 정보는 [Swift 공식 문서](https://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html)를 참조하시기 바랍니다.