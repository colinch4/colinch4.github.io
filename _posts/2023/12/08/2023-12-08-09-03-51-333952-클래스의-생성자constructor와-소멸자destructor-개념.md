---
layout: post
title: "[swift] 클래스의 생성자(constructor)와 소멸자(destructor) 개념"
description: " "
date: 2023-12-08
tags: [swift]
comments: true
share: true
---

클래스의 생성자(constructor)와 소멸자(destructor)는 객체지향 프로그래밍에서 중요한 개념입니다. 이 두 가지는 클래스의 인스턴스(instance)가 생성될 때와 소멸될 때 실행되는 특별한 메서드입니다. 

### 생성자 (Constructor)

**생성자**는 객체가 만들어질 때 호출되며, 객체의 초기화를 담당합니다. Swift에서는 `init` 키워드를 사용하여 생성자를 정의할 수 있습니다. 생성자는 객체가 만들어지면서 필요한 초기화 작업을 수행하고 클래스의 프로퍼티들을 초기화합니다. 아래는 간단한 예제입니다.

```swift
class Person {
    var name: String

    init(name: String) {
        self.name = name
    }
}

let person1 = Person(name: "John")
```

위 예제에서 `init` 키워드를 사용하여 `Person` 클래스의 생성자를 정의하였고, `name` 프로퍼티를 초기화하는 작업을 수행하였습니다.

### 소멸자 (Destructor)

**소멸자**는 객체가 소멸될 때 호출되며, 객체와 관련된 리소스의 정리나 정리 작업을 담당합니다. Swift에서는 `deinit` 키워드를 사용하여 소멸자를 정의할 수 있습니다. 소멸자는 객체가 메모리에서 해제될 때 호출되므로, 클래스의 인스턴스가 더 이상 필요하지 않을 때 필요한 정리 작업을 수행합니다.

```swift
class Person {
    var name: String

    init(name: String) {
        self.name = name
    }

    deinit {
        print("Person 객체가 메모리에서 해제됩니다.")
    }
}

var person1: Person? = Person(name: "John")
person1 = nil  // Person 객체가 메모리에서 해제됩니다.
```

위 예제에서 `deinit` 키워드를 사용하여 `Person` 클래스의 소멸자를 정의하였습니다. 그리고 `person1` 변수에 `nil`을 할당하여 객체를 메모리에서 해제하면 소멸자가 호출됩니다.

클래스의 생성자와 소멸자는 객체지향 프로그래밍에서 중요한 역할을 담당하며, 올바르고 안전한 객체의 생성과 소멸을 보장하기 위해 잘 활용되어야 합니다.