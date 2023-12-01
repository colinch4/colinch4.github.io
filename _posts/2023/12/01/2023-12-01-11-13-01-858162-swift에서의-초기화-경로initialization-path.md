---
layout: post
title: "[swift] Swift에서의 초기화 경로(Initialization Path)"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

Swift는 안전하고 강력한 초기화 과정을 가지고 있습니다. 클래스나 구조체의 인스턴스를 생성할 때 초기화 과정을 거쳐서 원하는 상태로 설정할 수 있습니다. 이 과정은 초기화 경로(Initialization Path)라고도 알려져 있습니다.

## 초기화 경로란?

초기화 경로는 클래스나 구조체의 인스턴스를 초기화하기 위해 거쳐야 하는 일련의 단계를 나타냅니다. 이 단계는 프로퍼티(속성)의 값을 설정하는 데 필요한 과정을 의미합니다. 초기화 경로를 따라야만 인스턴스를 적절하게 초기화할 수 있습니다.

## 초기화 경로의 종류

Swift에서는 다음과 같은 세 가지 종류의 초기화 경로를 제공합니다:

1. **Designated Initializers (지정 초기화자)**: 클래스나 구조체의 인스턴스를 생성할 때 가장 기본적인 초기화 경로입니다. 다른 초기화 경로의 구현에 이 초기화 경로를 내부적으로 호출할 수 있습니다.

2. **Convenience Initializers (편의 초기화자)**: 추가적인 설정 옵션을 제공하는 초기화 경로입니다. 보통 해당 타입의 다른 초기화 경로를 호출하여 내부적으로 처리합니다.

3. **Automatic Initializers (자동 초기화자)**: 모든 프로퍼티에 기본값이 설정되어 있는 경우 자동으로 제공되는 초기화 경로입니다. 일반적으로 구조체에서 사용됩니다.

## 초기화 경로의 순서

Swift에서는 초기화 경로가 설정되는 순서에 엄격한 규칙을 가지고 있습니다. 각각의 초기화 경로는 상위 경로 또는 동일한 수준의 다른 경로를 호출할 수 있지만, 하위 경로를 호출할 수는 없습니다. 또한, 초기화 경로는 인스턴스 프로퍼티를 자기 자신의 초기값으로만 설정할 수 있으며, 다른 인스턴스나 타입의 프로퍼티를 참조할 수 없습니다.

## 예제 코드

```swift
class Person {
    let name: String
    let age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    convenience init(name: String) {
        self.init(name: name, age: 0)
    }
    
    convenience init(age: Int) {
        self.init(name: "Unknown", age: age)
    }
}

let john = Person(name: "John Doe")
print(john.name) // 출력: John Doe
print(john.age) // 출력: 0

let jane = Person(age: 25)
print(jane.name) // 출력: Unknown
print(jane.age) // 출력: 25
```

위의 예제 코드에서 `Person` 클래스는 두 개의 지정 초기화자와 두 개의 편의 초기화자를 가지고 있습니다. `init(name:age:)` 초기화 경로가 가장 기본적인 초기화 경로이며, `convenience init(name:)`과 `convenience init(age:)` 초기화 경로는 추가적인 설정 옵션을 제공합니다.

## 참고 자료

- [The Swift Programming Language - Initialization](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html)