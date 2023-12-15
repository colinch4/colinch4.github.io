---
layout: post
title: "[swift] 제네릭 타입(Generics types)과 제네릭 함수(Generic functions)의 차이점은?"
description: " "
date: 2023-12-15
tags: [swift]
comments: true
share: true
---

## 제네릭 타입(Generics types)
제네릭 타입은 **함수, 구조체, 열거형, 클래스**와 같은 데이터 타입을 정의할 때 사용됩니다. 제네릭 타입을 사용하여 **다양한 타입의 데이터를 처리할 수 있는 코드를 작성**할 수 있습니다. 

예를 들어, 배열이나 딕셔너리와 같은 데이터 구조를 정의할 때 **특정한 데이터 타입에 의존하지 않고 다양한 타입의 데이터를 다룰 수 있는 타입을 정의**할 수 있습니다.

```swift
struct Queue<T> {
    var items = [T]()
    
    mutating func enqueue(_ item: T) {
        items.append(item)
    }
    
    mutating func dequeue() -> T? {
        if items.isEmpty {
            return nil
        } else {
            return items.removeFirst()
        }
    }
}
```

위 코드에서 `Queue` 구조체는 제네릭 타입 `T`를 사용하여 큐에 저장되는 데이터의 타입에 의존하지 않고 재사용 가능한 큐를 정의합니다.

## 제네릭 함수(Generic functions)
제네릭 함수는 **여러 타입의 매개변수와 반환 타입을 가지도록 작성**할 수 있는 함수입니다. 제네릭 함수를 사용하면 **타입 안전성을 유지하면서 여러 타입에서 작동하는 코드**를 작성할 수 있습니다.

```swift
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

위 코드에서 `swapTwoValues` 함수는 제네릭 함수로 정의되어 있으며, 두 개의 값을 서로 교환하는 기능을 수행하고 있습니다.

그러므로, 제네릭 타입과 제네릭 함수는 **타입 안전성을 유지하면서 재사용 가능하고 유연한 코드의 작성**을 도와주는데, 제네릭 타입은 데이터 타입을 정의할 때 사용되고, 제네릭 함수는 여러 타입의 매개변수와 반환 값을 가지도록 작성할 때 사용됩니다.