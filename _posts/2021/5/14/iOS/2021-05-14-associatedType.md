---
layout: post
title: "[iOS] associatedType"
description: " "
date: 2021-05-14
tags: [ios]
comments: true
share: true
---

## associatedType
- associated type 은 protocal에서 사용될 임의의 타입이름을 주는것 -> 프로토콜을 정의하면서 그 때 타입을 정의 (제네릭과 비슷한 개념)     

## 사용법
```swift
protocol Example {
    associatedtype Item
    func append(_ item: Item)
}
```

- Example 프로토콜에서 Item이라는 타입을 만들어 사용. 하지만 Item이 어떤 타입이 될지 모르는 상태 
- 타입이 지정될 때까지는 Item이라는 임의의 타입으로 알고 있겠다는 의미
- 이제 이 프로토콜을 정의할 때는 typealias나 generic을 사용해 Item의 타입을 지정할 수 있다.    

```swift
struct TypeExample {
    typealias Item = Int
    
    var items = [Item]()
    
    func append(_ item: Int) {
        self.items.append(item)
    }
}
```
- 위처럼 프로토콜을 준수하여 generic 없이 struct를 만들어 사용할 수 있다.
