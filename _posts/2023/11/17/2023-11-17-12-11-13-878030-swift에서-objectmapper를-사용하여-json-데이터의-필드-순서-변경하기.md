---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드 순서 변경하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
JSON 데이터는 일반적으로 필드 순서가 보장되지 않습니다. 그러나 때로는 JSON 데이터를 다른 시스템으로 전송하기 전에 필드 순서를 변경해야 할 수 있습니다. Swift에서 ObjectMapper 라이브러리를 사용하면 JSON 데이터의 필드 순서를 변경할 수 있습니다. 이 블로그 포스트에서는 ObjectMapper를 사용하여 JSON 데이터의 필드 순서를 변경하는 방법을 알아보겠습니다.

## ObjectMapper란?
ObjectMapper는 Swift에서 JSON 데이터와 객체 간의 변환을 쉽게 처리할 수 있는 라이브러리입니다. 이 라이브러리를 사용하면 JSON 데이터를 Swift 객체로 매핑하거나 Swift 객체를 JSON 데이터로 역매핑할 수 있습니다.

## ObjectMapper 설치
ObjectMapper를 사용하기 위해서는 Cocoapods를 통해 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가한 후 `pod install`을 실행하세요:

```ruby
pod 'ObjectMapper'
```

## 필드 순서 변경하기
JSON 데이터의 필드 순서를 변경하려면 ObjectMapper의 `convertToDictionary` 함수를 사용해야 합니다. 이 함수를 사용하면 JSON 데이터를 사전(Dictionary) 객체로 변환할 수 있습니다. 필드 순서를 변경하기 위해 변환된 사전 객체를 사용해야 합니다.

예를 들어, 다음과 같이 JSON 데이터가 있다고 가정해봅시다:

```json
{
   "name": "John",
   "age": 30,
   "location": "New York"
}
```

위 JSON 데이터의 필드 순서를 변경하여 다음과 같은 순서로 만들고 싶다고 가정해봅시다: `age`, `location`, `name`.

Swift 코드를 작성하여 ObjectMapper를 사용하여 필드 순서를 변경할 수 있습니다:

```swift
import ObjectMapper

struct User: Mappable {
   var age: Int?
   var location: String?
   var name: String?

   init?(map: Map) {}

   mutating func mapping(map: Map) {
      age <- map["age"]
      location <- map["location"]
      name <- map["name"]
   }
}

let json = """
{
   "name": "John",
   "age": 30,
   "location": "New York"
}
"""

if let user = Mapper<User>().map(JSONString: json) {
   // 필드 순서 변경
   let dictionary = user.convertToDictionary()
   let reorderedDictionary = dictionary.sorted(by: { $0.0 < $1.0 })

   if let reorderedJSON = Mapper<User>().toJSONString(reorderedDictionary) {
      print(reorderedJSON)
   }
}
```

위 코드에서는 `User`라는 구조체를 정의하고 `Mappable` 프로토콜을 구현했습니다. `Mappable` 프로토콜을 구현함으로써 JSON 데이터와 Swift 객체 간의 매핑을 쉽게 처리할 수 있습니다. 먼저 `User` 객체를 생성하고 JSON 데이터로 변환한 뒤 필드 순서를 변경하기 위해 `convertToDictionary` 함수를 호출합니다. 그리고 필드 순서를 변경한 사전 객체에 대해 `toJSONString` 함수를 호출하여 다시 JSON 데이터로 변환합니다. 변경된 JSON 데이터가 출력됩니다.

## 결론
Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드 순서를 변경하는 방법에 대해 알아보았습니다. ObjectMapper를 사용하면 필드 순서를 쉽게 변경하고, JSON 데이터와 Swift 객체 간의 매핑을 간편하게 처리할 수 있습니다. ObjectMapper의 강력한 기능을 활용하여 JSON 데이터 처리를 더욱 효율적으로 할 수 있습니다.

## 참고 자료
- [ObjectMapper GitHub 레포지토리](https://github.com/tristanhimmelman/ObjectMapper)