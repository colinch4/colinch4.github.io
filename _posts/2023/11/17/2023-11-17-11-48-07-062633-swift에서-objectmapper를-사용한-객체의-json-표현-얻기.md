---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용한 객체의 JSON 표현 얻기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 JSON과 객체 간의 변환을 쉽게 처리하기 위해 ObjectMapper라는 라이브러리를 사용할 수 있습니다. ObjectMapper를 사용하면 객체를 JSON으로 변환하거나, JSON을 객체로 변환하는 작업을 간편하게 할 수 있습니다. 이번 게시물에서는 Swift에서 ObjectMapper를 사용하여 객체의 JSON 표현을 얻는 방법을 알아보겠습니다.

## ObjectMapper란?

ObjectMapper는 Swift에서 JSON과 객체 간의 변환을 쉽게 처리하기 위한 라이브러리입니다. 이 라이브러리는 Swift의 Codable 프로토콜을 확장하여 JSON과 객체 간의 변환을 자동으로 처리해줍니다. ObjectMapper를 사용하면 JSON을 객체로 변환하거나, 객체를 JSON으로 변환하는 작업을 직접 구현할 필요가 없어집니다.

## ObjectMapper 설치하기

먼저 ObjectMapper를 프로젝트에 설치해야 합니다. ObjectMapper는 CocoaPods나 Swift Package Manager를 통해 설치할 수 있습니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다:

```ruby
pod 'ObjectMapper'
```

그리고 `pod install` 명령어를 실행하여 ObjectMapper를 설치합니다. Swift Package Manager를 사용한다면, Xcode의 "File" -> "Swift Packages" -> "Add Package Dependency"를 선택하여 ObjectMapper를 검색하고 추가합니다.

## ObjectMapper를 사용하여 객체의 JSON 표현 얻기

ObjectMapper를 사용하여 객체의 JSON 표현을 얻는 것은 매우 간단합니다. ObjectMapper는 객체를 JSON으로 변환하기 위해 `toJSON` 메소드를 제공합니다. 아래는 ObjectMapper를 사용하여 객체의 JSON 표현을 얻는 예제 코드입니다:

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

let person = Person(name: "John", age: 30)

if let json = person.toJSON() {
    print(json)
}
```

위의 예제 코드에서는 `Person`이라는 구조체를 정의하고, `Mappable` 프로토콜을 구현했습니다. `Mappable` 프로토콜은 ObjectMapper에서 요구하는 프로토콜로, `init?(map: Map)` 메소드와 `mapping(map: Map)` 메소드를 선언해야 합니다.

`mapping(map: Map)` 메소드에서는 객체의 각 속성을 JSON의 특정 필드와 매핑시킵니다. 위의 예제에서는 `name` 속성을 JSON의 "name" 필드에 매핑시키고, `age` 속성을 JSON의 "age" 필드에 매핑시켰습니다.

마지막으로, `person.toJSON()` 메소드를 호출하여 객체의 JSON 표현을 얻을 수 있습니다. 이렇게 얻어진 JSON 데이터는 `Any?` 타입이므로, 원하는 경우 JSONSerialization 등을 사용하여 필요한 작업을 수행할 수 있습니다.

## 결론

Swift에서 ObjectMapper를 사용하여 객체의 JSON 표현을 얻는 것은 매우 간단합니다. ObjectMapper를 사용하면 객체를 JSON으로 변환하고, JSON을 객체로 변환하는 작업을 간단하게 처리할 수 있습니다. ObjectMapper를 사용하면 JSON과 객체 간의 변환을 수동으로 구현할 필요가 없어지므로, 생산성을 높일 수 있습니다.

## 참고 자료

- [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)