---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 변경 감지 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

많은 앱이 서버와 통신하여 JSON 형식의 데이터를 받아와야 합니다. 이러한 데이터를 Swift 객체로 매핑하는 작업은 번거로울 수 있습니다. 하지만, ObjectMapper라는 라이브러리를 사용하면 이 작업을 쉽게 처리할 수 있습니다. 

이번 포스트에서는 ObjectMapper를 사용하여 JSON 데이터의 필드에 변경이 있었는지 감지하는 방법에 대해 알아보겠습니다.

## ObjectMapper 라이브러리 설치하기
먼저, ObjectMapper 라이브러리를 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 ObjectMapper를 추가합니다.

```
pod 'ObjectMapper'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드하고 프로젝트에 포함시킵니다.

## ObjectMapper 사용하기

먼저, JSON 데이터를 매핑할 Swift 구조체나 클래스를 정의해야 합니다. 예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해봅시다.

```json
{
    "name": "John",
    "age": 25,
    "email": "john@example.com"
}
```

이 JSON 데이터를 매핑하기 위해 다음과 같은 Swift 구조체를 정의합니다.

```swift
struct User: Mappable {
    var name: String?
    var age: Int?
    var email: String?
    
    init?(map: Map) {
        
    }
    
    mutating func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        email <- map["email"]
    }
}
```

위의 예제에서 `name`, `age`, `email` 프로퍼티를 정의하였고, `Mappable` 프로토콜을 채택하였습니다. 

`init?(map: Map)` 메서드는 객체의 초기화를 담당하며, `mapping(map: Map)` 메서드에서 JSON 데이터를 어떻게 매핑할지 정의합니다.

이제 ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 매핑할 수 있습니다. 아래 예제를 참고해주세요.

```swift
import ObjectMapper

let jsonString = "{\"name\":\"John\",\"age\":25,\"email\":\"john@example.com\"}"
if let user = Mapper<User>().map(JSONString: jsonString) {
    // 매핑 성공
    // 변경 감지 처리 등 추가 작업을 수행할 수 있음
} else {
    // 매핑 실패
}
```

위의 예제에서는 `Mapper<User>().map(JSONString: jsonString)` 코드를 사용하여 JSON 데이터를 `User` 객체로 매핑합니다. 매핑이 성공하면 변경 감지 처리 등의 추가 작업을 수행할 수 있습니다.

## 변경 감지 처리하기

JSON 데이터를 Swift 객체로 매핑한 후에는 필드의 변경 여부를 확인할 수 있습니다. ObjectMapper에서는 `didChangeValue(forKey:)` 메서드를 사용하여 필드의 변경을 감지할 수 있습니다. 아래 코드를 참고해주세요.

```swift
class User: Mappable {
    var name: String? {
        didSet {
            // name 필드 변경 시 호출되는 코드
        }
    }
    var age: Int? {
        didSet {
            // age 필드 변경 시 호출되는 코드
        }
    }
    var email: String? {
        didSet {
            // email 필드 변경 시 호출되는 코드
        }
    }
    
    //...
}
```

위의 예제에서는 `name`, `age`, `email` 필드가 변경될 때마다 `didSet` 블록이 실행됩니다. 이곳에 필드가 변경되었을 때 수행할 작업을 추가할 수 있습니다.

이제 Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 변경 감지 처리하는 방법에 대해 알아보았습니다. ObjectMapper를 사용하면 복잡한 JSON 데이터를 쉽게 매핑하고, 변경 감지 처리 등의 추가 작업을 수행할 수 있습니다.