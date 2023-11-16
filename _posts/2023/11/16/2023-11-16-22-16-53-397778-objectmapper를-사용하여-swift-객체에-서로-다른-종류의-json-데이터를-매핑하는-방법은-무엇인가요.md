---
layout: post
title: "[swift] ObjectMapper를 사용하여 Swift 객체에 서로 다른 종류의 JSON 데이터를 매핑하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

JSON 데이터를 Swift 객체에 매핑하기 위해 ObjectMapper를 사용하는 것은 매우 간단합니다. ObjectMapper는 JSON 데이터를 Swift 객체로 변환하는 데 사용되는 라이브러리입니다.

다음은 ObjectMapper를 사용하여 서로 다른 종류의 JSON 데이터를 매핑하는 방법에 대한 예시 코드입니다.

먼저, ObjectMapper를 프로젝트에 설치합니다. 아래의 코드를 터미널에 입력하여 CocoaPods를 사용하여 ObjectMapper를 설치할 수 있습니다.

```
pod 'ObjectMapper'
```

그런 다음, ObjectMapper를 import하여 사용할 준비를 합니다.

```swift
import ObjectMapper
```

이제 JSON 데이터를 매핑할 Swift 객체를 만듭니다. Swift 객체는 ObjectMapper의 Mappable 프로토콜을 구현해야 합니다. 다음은 예시를 위해 사용자 정보를 담은 User 클래스를 만들어 볼까요?

```swift
import ObjectMapper

class User: Mappable {
    var id: Int?
    var name: String?
    var email: String?

    required init?(map: Map) {
    
    }

    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

User 클래스는 id, name, email 속성을 가지고 있습니다. 매핑을 위해 Mappable 프로토콜을 구현하였으며, mapping(map:) 메서드를 사용하여 각 속성을 JSON 데이터의 키와 매핑합니다.

이제 다양한 종류의 JSON 데이터를 매핑해보겠습니다.

첫 번째는 다음과 같은 JSON 데이터입니다.

```json
{
  "id": 1,
  "name": "John",
  "email": "example@example.com"
}
```

다음은 해당 JSON 데이터를 매핑하는 코드입니다.

```swift
let userJSON = """
{
  "id": 1,
  "name": "John",
  "email": "example@example.com"
}
"""

if let user = User(JSONString: userJSON) {
    print(user.name) // John
}
```

두 번째는 다음과 같은 JSON 데이터입니다.

```json
{
  "userId": 2,
  "fullName": "Jane Doe",
  "userEmail": "jane.doe@example.com"
}
```

다음은 해당 JSON 데이터를 매핑하는 코드입니다.

```swift
let userJSON = """
{
  "userId": 2,
  "fullName": "Jane Doe",
  "userEmail": "jane.doe@example.com"
}
"""

if let user = User(JSONString: userJSON) {
    print(user.name) // Jane Doe
}
```

마지막으로, 다음과 같은 JSON 데이터입니다.

```json
{
  "userId": 3,
  "fullName": "Alex Smith",
  "emailAddress": "alex@example.com"
}
```

다음은 해당 JSON 데이터를 매핑하는 코드입니다.

```swift
let userJSON = """
{
  "userId": 3,
  "fullName": "Alex Smith",
  "emailAddress": "alex@example.com"
}
"""

if let user = User(JSONString: userJSON) {
    print(user.name) // Alex Smith
}
```

이처럼 ObjectMapper를 사용하여 Swift 객체에 서로 다른 종류의 JSON 데이터를 매핑할 수 있습니다. ObjectMapper는 자동으로 JSON 데이터의 키와 Swift 객체의 속성을 매핑해줍니다. 따라서 JSON 데이터와 Swift 객체의 속성명이 다를 경우에도 손쉽게 매핑할 수 있습니다.

추가적인 ObjectMapper의 기능 및 사용법은 [공식 문서](https://github.com/tristanhimmelman/ObjectMapper)에서 확인할 수 있습니다.