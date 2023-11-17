---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 스키마 검사하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 매우 유용한 도구로 JSON 데이터를 객체로 변환하거나 객체를 JSON으로 변환하는 데 사용할 수 있습니다. 이번 포스트에서는 ObjectMapper를 사용하여 JSON 스키마를 검사하는 방법에 대해 알아보겠습니다.

## ObjectMapper 라이브러리 추가하기

먼저 ObjectMapper를 사용하기 위해 프로젝트에 라이브러리를 추가해야 합니다. Swift Package Manager를 사용하는 경우 `Package.swift` 파일에 다음 종속성을 추가해주세요.

```swift
dependencies: [
    .package(url: "https://github.com/tristanhimmelman/ObjectMapper.git", from: "4.2.0")
]
```

CocoaPods를 사용하는 경우 `Podfile`에 다음과 같이 추가해주세요.

```ruby
pod 'ObjectMapper', '~> 4.2.0'
```

라이브러리를 추가한 후에는 `import ObjectMapper`를 통해 ObjectMapper을 사용할 수 있습니다.

## JSON 스키마 정의하기

JSON 스키마는 단순한 예제를 통해 설명하겠습니다. 예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해봅시다.

```json
{
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}
```

해당하는 객체를 매핑하기 위해 Swift 클래스를 생성해야 합니다. 우선 `Mappable` 프로토콜을 구현한 클래스를 만들어보겠습니다.

```swift
import ObjectMapper

class User: Mappable {
    var name: String?
    var age: Int?
    var email: String?

    required init?(map: Map) {
    }

    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        email <- map["email"]
    }
}
```

위의 코드에서 `Mappable` 프로토콜을 구현된 `User` 클래스가 있습니다. `name`, `age`, `email` 프로퍼티에 각각 매핑할 데이터를 맵핑해주는 `mapping` 함수가 구현되어 있습니다.

## JSON 데이터와 객체 매핑하기

이제 ObjectMapper를 사용하여 JSON 데이터와 객체를 매핑해보겠습니다. 다음은 매핑 예제입니다.

```swift
import ObjectMapper

let jsonString = """
{
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}
"""

if let user = Mapper<User>().map(JSONString: jsonString) {
  print("나이: \(user.age ?? 0)")
}
```

위의 코드에서는 `JSONString`을 이용하여 JSON 데이터를 `User` 객체로 매핑하고 있습니다. `User` 객체의 `age` 프로퍼티를 출력하고 있습니다.

## JSON 스키마 검사하기

JSON 스키마를 검사하기 위해서는 `User` 클래스에 추가적인 코드가 필요합니다. 아래의 코드를 `User` 클래스에 추가해주세요.

```swift
import ObjectMapper

class User: Mappable {
    var name: String?
    var age: Int?
    var email: String?

    required init?(map: Map) {
    }

    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        email <- map["email"]
    }

    func validateSchema() -> Bool {
        if name == nil || age == nil || email == nil {
            return false
        }
        return true
    }
}
```

`validateSchema` 함수는 객체의 프로퍼티들이 모두 값을 가지고 있는지 확인하여 `true` 또는 `false`를 반환합니다.

```swift
import ObjectMapper

if let user = Mapper<User>().map(JSONString: jsonString) {
  if user.validateSchema() {
    print("Valid JSON Schema")
  } else {
    print("Invalid JSON Schema")
  }
}
```

위의 코드는 JSON 데이터를 `User` 객체로 매핑한 후 `validateSchema` 함수를 통해 JSON 스키마를 검사합니다. `true` 또는 `false`를 반환하며, 검사 결과에 따라 메시지를 출력합니다.

## 결론

Swift에서 ObjectMapper를 사용하여 JSON 스키마를 검사하는 방법에 대해 알아보았습니다. JSON 데이터를 객체로 매핑한 후 스키마를 검사하는 것은 데이터의 유효성을 보장하기 위해 중요한 작업입니다. ObjectMapper를 사용하면 간단하게 JSON 데이터와 객체를 매핑하고, 검사를 통해 스키마 일치 여부를 확인할 수 있습니다.