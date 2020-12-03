---
layout: post
title: "[swift] 15. 확장(Extension)"
description: " "
date: 2020-07-30
tags: [swift]
comments: true
share: true
---

### Extension
Objective-C 의 카테고리와 비슷

### Extension 으로 할 수 있는 것들.
- Computed instance property, Computed type property 추가 가능
- Instance method, Type method 추가 가능
- 새로운 initializer 제공
- 서브스크립트 정의
- 중첩 타입의 선언과 사용
- 특정 프로토콜을 따르는 타입 만들기

### 표현식
```swift
extension SomeType: SomeProtocol, AnotherProtocol {
    // implementation of protocol requirements goes here
}
```

### Computed instance properties 추가
```swift
extension Double {
    var km: Double { return self 1_000.0 }
    var m: Double { return self }
    var cm: Double { return self / 100.0 }
    var mm: Double { return self / 1_000.0 }
    var ft: Double { return self / 3.28084 }
}
```

### 새로운 initializer 추가
- 다른 initializer 호출 가능
- 다른 initializer 호출전 까지 self 를 접근할 수 없음.
- self 변경 가능. 변경할 경우 mutation 선언 필수

### 인스턴스 메소드 추가
- self를 변경 가능
```swift
extension Int {
    mutating func square() {
        self = self * self
    }
}
var someInt = 3
someInt.square()
// someInt is now 9
```
