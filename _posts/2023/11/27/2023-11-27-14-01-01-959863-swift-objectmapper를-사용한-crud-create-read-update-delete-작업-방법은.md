---
layout: post
title: "[swift] Swift ObjectMapper를 사용한 CRUD (Create, Read, Update, Delete) 작업 방법은?"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 개요
이번 블로그 포스트에서는 Swift ObjectMapper를 사용하여 CRUD (Create, Read, Update, Delete) 작업을 수행하는 방법에 대해 알아보겠습니다. Swift ObjectMapper는 JSON과 Swift 객체간의 매핑을 쉽게 처리해주는 라이브러리입니다.

## ObjectMapper 설치
먼저, ObjectMapper를 사용하기 위해 프로젝트에 라이브러리를 추가해야 합니다. CocoaPods를 사용하신다면 `Podfile`에 다음과 같이 ObjectMapper를 추가해주세요.

```ruby
pod 'ObjectMapper'
```

라이브러리를 추가한 후 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 객체와 JSON 매핑
아래 예시를 통해 Swift 객체와 JSON 데이터를 매핑하는 방법을 알아보겠습니다.

```swift
import ObjectMapper

class User: Mappable {
    var id: Int?
    var name: String?
    var email: String?

    required init?(map: Map) {}

    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}

let jsonString = """
{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
}
"""

if let user = User(JSONString: jsonString) {
    print(user.id) // 1
    print(user.name) // John Doe
    print(user.email) // johndoe@example.com
}
```

위의 코드에서는 `User` 클래스를 정의하고 `Mappable` 프로토콜을 구현합니다. `Mappable` 프로토콜은 `init?(map: Map)`과 `mapping(map: Map)` 메서드를 요구합니다.

`mapping(map: Map)` 메서드에서는 객체의 각 속성과 JSON 데이터의 필드를 연결합니다. 이렇게 연결된 매핑 정보를 통해 ObjectMapper는 객체를 생성하고 값을 채웁니다.

## Create (생성)
새로운 객체를 생성하여 서버에 전송하기 위해서는 JSON 데이터를 생성해야 합니다. ObjectMapper를 사용하면 Swift 객체를 JSON 문자열로 변환하기 매우 간단합니다. 아래 예시를 참고하세요.

```swift
let newUser = User()
newUser.name = "Alice"
newUser.email = "alice@example.com"

if let jsonString = newUser.toJSONString() {
    // jsonString을 서버에 전송하거나 다른 처리를 수행합니다.
    print(jsonString)
}
```

위의 코드에서는 `User` 객체를 생성하고 필드 값을 설정한 뒤, `toJSONString()` 메서드를 사용하여 객체를 JSON 문자열로 변환합니다.

## Read (조회)
서버로부터 받은 JSON 데이터를 객체로 변환하기 위해서는 ObjectMapper의 `mapObject(_: JSON)` 메서드를 사용합니다. 아래 예시를 참고하세요.

```swift
let jsonFromServer = """
{
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com"
}
"""

if let user = Mapper<User>().map(JSONString: jsonFromServer) {
    print(user.id) // 2
    print(user.name) // Bob
    print(user.email) // bob@example.com
}
```

위의 코드에서는 `mapObject(_: JSON)` 메서드를 사용하여 JSON 데이터를 `User` 객체로 변환합니다. 변환된 객체를 사용하여 필요한 작업을 수행할 수 있습니다.

## Update (수정)
기존 객체를 수정하기 위해서는 JSON 데이터를 수정하고 ObjectMapper의 `update(_: to: JSON)` 메서드를 사용합니다. 아래 예시를 참고하세요.

```swift
let jsonToUpdate = """
{
    "name": "Charlie"
}
"""

if let userToUpdate = Mapper<User>().map(JSONString: jsonToUpdate) {
    userToUpdate.id = 3

    if let updatedJSON = Mapper().toJSONString(userToUpdate) {
        // updatedJSON을 서버에 전송하거나 다른 처리를 수행합니다.
        print(updatedJSON)
    }
}
```

위의 코드에서는 JSON 데이터를 수정하고 `update(_: to: JSON)` 메서드를 사용하여 기존의 객체를 수정합니다. 수정된 객체를 다시 JSON 문자열로 변환할 수 있습니다.

## Delete (삭제)
객체를 삭제하려면 해당 객체를 서버로 전송하거나 서버에 삭제 요청을 보내야 합니다. 이 과정은 서버와의 통신에 따라 다르므로 서버에서의 삭제 처리 방법에 따라 구현되어야 합니다.

## 결론
Swift ObjectMapper를 사용하여 CRUD 작업을 수행하는 방법에 대해 알아보았습니다. ObjectMapper는 Swift 객체와 JSON 데이터 간의 매핑을 효율적으로 처리해주어 간편한 개발을 가능하게 해줍니다.