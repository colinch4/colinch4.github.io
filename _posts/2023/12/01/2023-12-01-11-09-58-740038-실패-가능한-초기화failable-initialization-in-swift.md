---
layout: post
title: "[swift] 실패 가능한 초기화(Failable Initialization) in Swift"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

Swift에서는 객체의 초기화를 위해 초기화 메소드를 사용합니다. 일반적으로 초기화 메소드는 새로운 객체를 성공적으로 초기화할 수 있어야 하지만, 때로는 초기화가 실패할 수도 있습니다. 이러한 경우에 사용되는 것이 **실패 가능한 초기화(Failable Initialization)** 입니다.

실패 가능한 초기화는 객체 생성을 시도하고, 생성이 실패할 경우 `nil` 을 반환하는 초기화 메소드입니다. 이를 사용하여 오류 처리를 간편하게 할 수 있습니다.

## 실패 가능한 초기화 구현하기

실패 가능한 초기화는 클래스, 구조체, 열거형에서 사용할 수 있습니다. 초기화 메소드 정의 시 반환 타입으로 `?` 를 사용하여 실패 가능한 초기화를 선언합니다. 예를 들어, 아래는 실패 가능한 초기화를 가진 `Person` 구조체의 예시입니다.

```swift
struct Person {
    let name: String
    let age: Int
    
    init?(name: String, age: Int) {
        if name.isEmpty || age < 0 {
            return nil
        }
        
        self.name = name
        self.age = age
    }
}
```

위의 코드에서 `name`이 빈 문자열이거나 `age`가 0보다 작을 경우 초기화가 실패하고 `nil`을 반환합니다.

## 실패 가능한 초기화 사용하기

실패 가능한 초기화를 사용할 때에는 일반적으로 옵셔널(`Optional`) 타입을 사용합니다. 이를 통해 초기화가 실패한 경우 `nil`이 반환되는지 확인할 수 있습니다.

```swift
let person1 = Person(name: "John", age: 25)
// 성공적으로 초기화되어 옵셔널 타입이 아닌 값이 반환됨

let person2 = Person(name: "", age: 30)
// 초기화에 실패하여 nil이 반환됨
```

## 실패 가능한 초기화와 일반 초기화의 차이점

실패 가능한 초기화와 일반 초기화의 가장 큰 차이점은 초기화가 실패할 때 어떻게 처리되는지에 있습니다. 실패 가능한 초기화는 `nil`을 반환하여 초기화가 실패했음을 나타내지만, 일반 초기화에서는 실패시 오류를 던지게 됩니다.

실패 가능한 초기화의 사용은 초기화 프로세스 중간에서 검증이 필요한 경우, 옵셔널 값을 통해 실패를 처리할 수 있는 경우 등에 유용합니다.

## 결론

Swift에서 실패 가능한 초기화를 사용하면 초기화 과정에서 발생 가능한 실패를 더욱 명확하게 다룰 수 있습니다. 옵셔널 타입을 사용하여 초기화가 성공했는지 실패했는지 확인할 수 있으며, 오류 처리 로직을 조금 더 효율적으로 작성할 수 있습니다.

더 자세한 내용은 공식 [Swift 문서](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html)를 참조하시기 바랍니다.