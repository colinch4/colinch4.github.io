---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드 유효성 검사 에러 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

많은 애플리케이션에서는 서버로부터 받은 JSON 데이터를 객체로 매핑하여 사용해야 합니다. Swift에서 ObjectMapper는 JSON 데이터를 Swift 객체로 변환할 때 편리한 도구입니다. 하지만 때로는 서버에서 올바르지 않은 데이터가 반환될 수도 있습니다. 이러한 경우 ObjectMapper를 사용하여 필드 유효성을 검사하고 에러 처리하는 방법을 알아보겠습니다.

## ObjectMapper 소개

ObjectMapper는 Swift에서 JSON 데이터를 Swift 객체로 변환하는 라이브러리입니다. ObjectMapper를 사용하면 JSON 데이터를 Swift 객체로 변환하거나 Swift 객체를 JSON 데이터로 변환하는 것이 편리해집니다.

ObjectMapper를 사용하기 위해 `import ObjectMapper`라는 문구를 소스 코드 상단에 추가해야 합니다. ObjectMapper는 `map()` 메소드를 제공하여 JSON 데이터를 Swift 객체로 변환합니다. 변환할 Swift 객체는 `Mappable` 프로토콜을 채택해야 합니다.

## 필드 유효성 검사

JSON 데이터에서 필드 유효성을 검사하기 위해 ObjectMapper의 `map()` 메소드를 사용할 수 있습니다. ObjectMapper는 유효성 검사를 위해 다양한 방법을 제공합니다. 예를 들어, 필수 필드가 있는지 확인하거나 특정 필드 값의 범위를 검사할 수 있습니다.

예를 들어, 우리가 User 객체를 생성하고 싶다고 가정해봅시다. User 객체에는 id, name, age 필드가 필수적으로 존재해야하고, age는 18세 이상이어야 합니다.

```swift
class User: Mappable {
    var id: Int!
    var name: String!
    var age: Int!

    required init?(map: Map) {}

    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        age <- map["age"]
    }
}
```

이제 JSON 데이터를 이용하여 User 객체를 생성하는 예제를 살펴보겠습니다. ObjectMapper의 `map()` 메소드를 사용하여 JSON 데이터에서 User 객체를 생성합니다.

```swift
let json = "{\"id\": 1, \"name\": \"John Doe\", \"age\": 25}"
if let user = Mapper<User>().map(JSONString: json) {
    // 유효성 검사
    if user.id == nil || user.name == nil || user.age == nil {
        // 필수 필드가 없는 경우 에러 처리
        print("필수 필드가 없습니다.")
    }
    else if user.age < 18 {
        // age 필드가 18세 미만인 경우 에러 처리
        print("나이가 18세 미만입니다.")
    }
    else {
        // 유효한 데이터인 경우 처리
        print("유효한 데이터입니다.")
    }
}
else {
    // JSON 데이터를 매핑할 수 없는 경우 에러 처리
    print("JSON 데이터 매핑 에러")
}
```

위의 예제는 `map()` 메소드를 통해 JSON 데이터에서 User 객체를 생성한 뒤, 필수 필드와 필드 값의 유효성을 검사하고 에러를 처리하는 방법을 보여줍니다.

## 정리

Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드 유효성을 검사하고 에러를 처리하는 방법을 알아보았습니다. ObjectMapper는 JSON 데이터를 Swift 객체로 변환할 때 사용되는 강력한 도구이며 유효성 검사를 통해 올바르지 않은 데이터를 처리할 수 있습니다. ObjectMapper를 통해 안전하고 견고한 애플리케이션을 개발할 수 있습니다.

더 자세한 내용은 [ObjectMapper 공식 문서](https://github.com/tristanhimmelman/ObjectMapper)를 참조하세요.