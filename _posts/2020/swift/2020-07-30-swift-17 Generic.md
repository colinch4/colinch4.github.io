---
layout: post
title: "[swift] 17. 제네릭(Generic)"
description: " "
date: 2020-07-30
tags: [swift]
comments: true
share: true
---

### Generic 함수
- type을 특정하지 않은 형태로 정의할 때.

### 사용 예
```swift
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}


var someInt = 3
var anotherInt = 107
swapTwoValues(&someInt, &anotherInt)
// someInt is now 107, and anotherInt is now 3

var someString = "hello"
var anotherString = "world"
swapTwoValues(&someString, &anotherString)
// someString is now "world", and anotherString is now "hello"
```

### 타입 제한
- 상속받아야 하는 클래스나 프로토콜을 명시할 수 있다. 

```swift
func someFunction<T: SomeClass, U: SomeProtocol>(someT: T, someU: U) {
    // function body goes here
}


// 아래 예에서 value == valueToFind 를 하기 위해 T 가 Equatable을 구현해야 한다는 것을 명시
func findIndex<T: Equatable>(of valueToFind: T, in array:[T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

### 프로토콜
- associatedtype typealias 로 타입을 지정 가능

```swift
protocol MyProtocol {
    associatedtype MyElement
    func sayHello(ele: MyElement)
}

struct MyStruct1: MyProtocol {
    typealias MyElement = Int
    func sayHello(ele: MyElement) {
        print("hello: \(ele)")
    }
}

struct MyStruct2: MyProtocol {
    typealias MyElement = String
    func sayHello(ele: MyElement) {
        print("hello: \(ele)")
    }
}

MyStruct1().sayHello(ele:1)
// print "hello 1"
MyStruct2().sayHello(ele:"foo")
// print "hello foo"
```

### extension associatedtype
```swift
protocol MyProtocol {
    associatedtype MyElement
    func sayHello(ele: MyElement)
}


extension MyProtocol where MyElement == String {
    func sayHello(ele: MyElement) {
       print("Hello String")
    }
}

extension MyProtocol where MyElement == Int {
    func sayHello(ele: MyElement) {
        print("Hello Int")
    }
}


struct MyStruct1: MyProtocol {
    typealias MyElement = Int
}

struct MyStruct2: MyProtocol {
    typealias MyElement = String
}


MyStruct1().sayHello(ele:"string")
// print "hello foo"
MyStruct2().sayHello(ele:0)
// print "hello 1"
```
