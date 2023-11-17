---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 객체의 속성을 JSON으로 직렬화하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 매우 효과적이고 강력한 라이브러리입니다. 이 라이브러리를 사용하면 객체를 JSON으로 직렬화하고, JSON을 객체로 역직렬화할 수 있습니다. ObjectMapper를 사용하는 방법에 대해 알아보겠습니다.

## 1. ObjectMapper 설치

먼저, ObjectMapper를 사용하기 위해 프로젝트에 라이브러리를 추가해야 합니다. Swift 패키지 매니저를 사용한다면, `Package.swift` 파일에 다음 의존성을 추가합니다:

```swift
dependencies: [
    .package(url: "https://github.com/tristanhimmelman/ObjectMapper.git", .upToNextMajor(from: "4.2.0"))
]
```

CocoaPods를 사용하거나 수동으로 추가하는 방법은 ObjectMapper의 공식 GitHub 저장소에서 확인할 수 있습니다.

## 2. ObjectMapper 사용하기

`ObjectMapper`를 사용하려면, 직렬화하거나 역직렬화할 객체가 `Mappable` 프로토콜을 따르도록 해야 합니다.

객체를 JSON으로 직렬화하려면, 다음과 같이 `toJSON()` 메서드를 호출합니다:

```swift
import ObjectMapper

class User: Mappable {
    var name: String?
    var age: Int?
    
    required init?(map: Map) { }
    
    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}

let user = User()
user.name = "John Appleseed"
user.age = 30

let json = user.toJSON()
print(json)
```

위의 코드는 User 객체를 생성하고, name 속성과 age 속성을 설정한 후 `toJSON()` 메서드를 호출하여 객체를 JSON으로 직렬화합니다. JSON 결과는 다음과 같습니다:

```json
{
    "name": "John Appleseed",
    "age": 30
}
```

## 3. JSON을 객체로 역직렬화하기

JSON을 객체로 역직렬화하려면, 다음과 같이 `Map` 객체를 생성한 후 `mapJSON(_:)` 메서드를 호출합니다:

```swift
let json = """
{
    "name": "John Appleseed",
    "age": 30
}
"""

if let user = Mapper<User>().map(JSONString: json) {
    print(user.name) // John Appleseed
    print(user.age) // 30
}
```

위의 코드는 JSON을 User 객체로 역직렬화하는 예시입니다. `mapJSON(_:)` 메서드를 사용하여 JSON 문자열을 `Map` 객체로 변환한 후, `Mapper<User>().map(JSONString:)` 메서드를 호출하여 JSON을 객체로 역직렬화합니다.

## 4. ObjectMapper의 고급 사용법

ObjectMapper에는 다양한 기능과 사용법이 있습니다. 매핑에 대한 유효성 검사, 배열 매핑, 카멜 케이스와 스네이크 케이스의 매핑, 커스텀 매핑 등의 기능을 사용할 수 있습니다. 더 자세한 내용은 ObjectMapper의 공식 문서와 예시를 참조하시길 바랍니다.

## 참고 자료

- ObjectMapper GitHub 저장소: [https://github.com/tristanhimmelman/ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)
- ObjectMapper 문서: [https://github.com/tristanhimmelman/ObjectMapper#usage](https://github.com/tristanhimmelman/ObjectMapper#usage)