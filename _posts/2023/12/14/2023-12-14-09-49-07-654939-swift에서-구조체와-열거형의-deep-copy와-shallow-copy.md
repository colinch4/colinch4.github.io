---
layout: post
title: "[swift] Swift에서 구조체와 열거형의 deep copy와 shallow copy"
description: " "
date: 2023-12-14
tags: [swift]
comments: true
share: true
---

Swift에서 구조체와 열거형은 값 타입이기 때문에 할당(assign) 시에 딥 복사(deep copy)와 셸로우 복사(shallow copy)의 차이를 이해하는 것이 중요합니다. 이번 블로그 포스트에서는 이 둘의 차이를 설명하고, 각각의 동작을 구현하는 방법에 대해 알아보겠습니다.

## 1. Deep Copy와 Shallow Copy의 차이

**딥 복사(deep copy)**는 새로운 메모리 공간을 할당하고 해당 객체의 값 또는 내부 객체를 복사하는 것을 의미합니다. 이렇게 복사된 객체는 원본 객체와 완전히 분리되어 독립적으로 동작합니다.

**셸로우 복사(shallow copy)**는 새로운 객체를 생성하지만 내부 객체들은 원본 객체와 동일한 메모리 주소를 참조하게 됩니다. 즉, 내부 객체의 변경이 복사본에도 영향을 미칠 수 있습니다.

## 2. 구조체에서의 Deep Copy와 Shallow Copy

구조체는 값 타입이기 때문에 복사 시에는 항상 딥 복사가 이루어집니다. 즉, 새로운 인스턴스가 생성되고 해당 인스턴스 내의 모든 속성들이 복사됩니다.

다음은 Swift에서 구조체를 복사하는 예시 코드입니다.

```swift
struct Person {
    var name: String
}

let person1 = Person(name: "Alice")
var person2 = person1 // 딥 복사가 이루어짐
person2.name = "Bob"

print(person1.name) // 출력 결과: "Alice"
print(person2.name) // 출력 결과: "Bob"
```

## 3. 열거형에서의 Deep Copy와 Shallow Copy

열거형의 경우에도 구조체와 마찬가지로 값 타입이기 때문에 복사 시에는 딥 복사가 이루어집니다. 모든 케이스와 연관 값이 복사되며, 새로운 인스턴스가 생성됩니다.

다음은 Swift에서 열거형을 복사하는 예시 코드입니다.

```swift
enum Direction {
    case north
    case south
    case east
    case west
}

let direction1 = Direction.north
var direction2 = direction1 // 딥 복사가 이루어짐
direction2 = .south

print(direction1) // 출력 결과: north
print(direction2) // 출력 결과: south
```

## 결론

Swift에서는 값 타입인 구조체와 열거형을 복사할 때 딥 복사가 이루어집니다. 이를 통해 객체 간의 독립성을 유지하고 예기치 않은 상태 변화를 방지할 수 있습니다.

딥 복사와 셸로우 복사의 개념을 이해하고, Swift에서는 값 타입을 다룰 때 항상 딥 복사가 이루어진다는 점을 기억하는 것이 중요합니다.

참고문헌:
- [The Swift Programming Language - Swift 5.5](https://docs.swift.org/swift-book/)
- [Swift.org](https://swift.org/)