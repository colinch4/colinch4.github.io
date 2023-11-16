---
layout: post
title: "[swift] ObjectMapper를 사용하여 Swift 객체의 배열을 JSON 데이터로 변환하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

JSON 데이터로 변환하려는 Swift 객체 배열을 가지고 있다고 가정해 봅시다. ObjectMapper는 JSON 데이터와 Swift 객체 간의 변환을 도와주는 훌륭한 라이브러리입니다.

아래는 ObjectMapper를 사용하여 Swift 객체 배열을 JSON 데이터로 변환하는 예제 코드입니다.

```swift
import ObjectMapper

struct Person: Mappable {
    var name: String?
    var age: Int?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}

let people: [Person] = [
    Person(name: "John", age: 25),
    Person(name: "Jane", age: 30),
    Person(name: "Mike", age: 35)
]

let jsonString = Mapper().toJSONString(people)
print(jsonString ?? "")
```

위의 예제 코드에서, `Person`이라는 구조체는 ObjectMapper의 `Mappable` 프로토콜을 따르도록 선언되었습니다. `mapping` 메소드를 구현하여 JSON 데이터와 객체의 속성을 매핑시킵니다. `let people: [Person]`은 JSON 데이터로 변환하려는 Swift 객체 배열입니다.

`Mapper().toJSONString(people)`를 사용하여 객체 배열을 JSON 문자열로 변환할 수 있습니다. 변환된 JSON 문자열은 `jsonString` 상수에 저장되며, 이를 출력하면 변환 결과를 확인할 수 있습니다.

이제 `jsonString`을 서버에 전송하거나 파일에 저장하는 등의 작업을 수행할 수 있습니다.

참고 자료:
- [ObjectMapper GitHub 리포지터리](https://github.com/tristanhimmelman/ObjectMapper)