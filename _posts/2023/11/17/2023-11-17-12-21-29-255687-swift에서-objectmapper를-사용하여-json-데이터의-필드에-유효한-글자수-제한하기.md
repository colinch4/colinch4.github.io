---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 유효한 글자수 제한하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

JSON 데이터를 받아와서 Swift에서 사용하기 위해 ObjectMapper라는 라이브러리를 사용하는 경우가 많습니다. 이 라이브러리를 사용하면 JSON 데이터를 쉽게 Swift 객체로 매핑할 수 있습니다. 이번 글에서는 ObjectMapper를 사용하여 JSON 데이터의 필드에 유효한 글자수 제한을 적용하는 방법을 알아보겠습니다.

## ObjectMapper란?

ObjectMapper는 Swift에서 사용하는 객체 매핑 라이브러리입니다. 이 라이브러리를 사용하면 JSON 데이터를 Swift 객체로 변환하거나 Swift 객체를 JSON 데이터로 변환할 수 있습니다. ObjectMapper는 Swift 4 이전의 버전에서 많이 사용되었지만, Swift 4에서는 Codable 프로토콜을 사용하는 것을 권장합니다. 그러나 여전히 ObjectMapper를 사용하는 경우가 많기 때문에 이 글에서는 ObjectMapper를 사용하여 JSON 데이터의 필드를 제한하는 방법을 알아보겠습니다.

## ObjectMapper를 사용한 JSON 매핑

ObjectMapper를 사용하여 JSON 데이터를 매핑하려면 우선 JSON 데이터를 담을 Swift 객체를 만들어야 합니다. 예를 들어, 유저 정보를 담는 User 클래스를 만들어보겠습니다.

```swift
import ObjectMapper

class User: Mappable {
    var id: Int?
    var name: String?

    required init?(map: Map) {
    }

    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
    }
}
```

위의 코드에서는 ObjectMapper의 `Mappable` 프로토콜을 구현한 `User` 클래스를 정의했습니다. 이 클래스는 `id`와 `name`이라는 두 개의 속성을 가지고 있습니다. `mapping` 메서드를 사용하여 JSON 데이터의 각 필드를 해당 속성에 매핑합니다.

이제 ObjectMapper를 사용하여 JSON 데이터를 User 객체로 매핑해보겠습니다.

```swift
let jsonString = """
{
    "id": 1,
    "name": "John Doe"
}

if let user = User(JSONString: jsonString) {
    print(user.id) // 출력: Optional(1)
    print(user.name) // 출력: Optional("John Doe")
}
```

위의 코드에서는 JSON 문자열을 `User` 객체로 매핑하는 방법을 보여줍니다. ObjectMapper의 `init(JSONString:)` 메서드를 사용하면 JSON 문자열을 객체로 변환할 수 있습니다.

## 필드 길이 제한

이제 JSON 데이터의 필드에 유효한 글자수 제한을 적용해보겠습니다. 예를 들어, `name` 필드의 길이를 최대 10글자로 제한하고 싶다고 가정해봅시다.

```swift
import ObjectMapper

class User: Mappable {
    var id: Int?
    var name: String?

    required init?(map: Map) {
    }

    func mapping(map: Map) {
        id <- map["id"]
        name <- (map["name"], MaxLengthTransform(maxLength: 10))
    }
}

struct MaxLengthTransform: TransformType {
    let maxLength: Int

    init(maxLength: Int) {
        self.maxLength = maxLength
    }

    func transformFromJSON(_ value: Any?) -> String? {
        if let stringValue = value as? String {
            return String(stringValue.prefix(maxLength))
        }
        return nil
    }

    func transformToJSON(_ value: String?) -> Any? {
        return value
    }
}
```

위의 코드에서는 `MaxLengthTransform`이라는 트랜스폼 타입을 정의합니다. 이 트랜스폼 타입은 ObjectMapper의 `<<-` 연산자를 통해 `name` 필드에 적용됩니다. `transformFromJSON` 메서드에서는 JSON 데이터를 읽어서 필드의 길이를 최대 길이로 제한하고, `transformToJSON` 메서드에서는 필드 값을 그대로 반환합니다.

이제 ObjectMapper를 사용하여 JSON 데이터를 매핑하면 `name` 필드의 길이가 최대 10글자로 제한될 것입니다.

```swift
let jsonString = """
{
    "id": 1,
    "name": "John Doe"
}

if let user = User(JSONString: jsonString) {
    print(user.id) // 출력: Optional(1)
    print(user.name) // 출력: Optional("John Doe")
}
```

위의 코드에서는 JSON 문자열을 `User` 객체로 매핑하고, `name` 필드의 길이 제한을 확인합니다. `"name"` 필드의 값이 10글자를 초과한다면, 해당 필드의 값은 최대 길이로 제한될 것입니다.

## 결론

이번 글에서는 Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 유효한 글자수 제한을 적용하는 방법을 알아보았습니다. ObjectMapper를 사용하여 JSON 데이터를 매핑하는 방법과 필드 길이 제한을 하는 방법을 소개했습니다. ObjectMapper는 간단하게 JSON 데이터를 Swift 객체로 변환할 수 있기 때문에 많이 사용되지만, Swift 4부터는 Codable 프로토콜을 사용하는 것이 권장되므로 고려해볼만 합니다.