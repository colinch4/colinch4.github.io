---
layout: post
title: "[swift] 16. 프로토콜(Protocol)"
description: " "
date: 2020-07-30
tags: [swift]
comments: true
share: true
---

### Protocol
- Java의 interface와 비슷

### 표현식
```swift
protocol SomeProtocol {
    var value1: Type { get set }
	static var value2: Type { get set }


	init(param: Int)


	func function1() -> Double
	static func function2()
}
```

### init 구현 
- required keyword 추가. 
- superclass의 init을 overriding하고 protocol의 init을 구현하는 경우 required override 를 같이 적는다. 

```swift
protocol SomeProtocol {
    init()
}

class SomeSuperClass {
    init() {
        // initializer implementation goes here
    }
}

class SomeSubClass: SomeSuperClass, SomeProtocol {
    // "required" from SomeProtocol conformance; "override" from SomeSuperClass
    required override init() {
        // initializer implementation goes here
    }
}
```

### 조건에 의한 프로토콜 (Conditionally Conforming to a Protocol)
- 특정 조건을 만족할 때만 따르도록 제한. where 절을 사용해 정의 

```swift
extension Array: TextRepresentable where Element: TextRepresentable {
    var textualDescription: String {
        let itemsAsText = self.map { $0.textualDescription }
        return "[" + itemsAsText.joined(separator: ", ") + "]"
    }
}
let myDice = [d6, d12]
print(myDice.textualDescription)
// Prints "[A 6-sided dice, A 12-sided dice]"
```


### 합성
- 여러 개를 따르는 프로토콜 정의

```swift
protocol Named {
    var name: String { get }
}
protocol Aged {
    var age: Int { get }
}
struct Person: Named, Aged {
    var name: String
    var age: Int
}

// 여러 개의 protocol을 합성한 객체의 선언을 & 로 선언
func wishHappyBirthday(to celebrator: Named & Aged) {
    print("Happy birthday, \(celebrator.name), you're \(celebrator.age)!")
}
let birthdayPerson = Person(name: "Malcolm", age: 21)
wishHappyBirthday(to: birthdayPerson)
// Prints "Happy birthday, Malcolm, you're 21!"
```

### Objc 프로토콜
- @objc protocol 은 @objc optional 로 선택적 구현 조건을 정의할 수 있다. 
- optional 이므로 옵셔널 체이닝으로 확인하여 접근해야 한다. 

```swift
@objc protocol CounterDataSource {
    @objc optional func increment(forCount count: Int) -> Int
    @objc optional var fixedIncrement: Int { get }
}
```
