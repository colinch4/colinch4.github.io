---
layout: post
title: "[swift] Swift에서 ObjectMapper를 이용해 JSON 데이터를 객체로 변환하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 강력한 라이브러리로, JSON 데이터를 Swift 객체로 변환하고 Swift 객체를 JSON 데이터로 변환할 수 있습니다. 이번에는 ObjectMapper를 사용하여 JSON 데이터를 객체로 변환하는 방법에 대해 알아보겠습니다.

## ObjectMapper 설치하기

먼저 ObjectMapper를 설치해야 합니다. CocoaPods를 사용하는 경우, `Podfile`에 다음을 추가합니다.

```swift
pod 'ObjectMapper'
```

그리고 `pod install` 명령을 실행하여 ObjectMapper를 프로젝트에 추가합니다. 만약 Carthage나 Swift Package Manager를 사용하는 경우에도 적절한 방법으로 설치할 수 있습니다.

## JSON 데이터 정의하기

예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해봅시다.

```json
{
  "name": "John Doe",
  "age": 30,
  "email": "johndoe@example.com"
}
```

해당 JSON 데이터를 Swift 객체로 변환하기 위해선, 매칭되는 Swift 클래스를 정의해야 합니다.

```swift
import ObjectMapper

class User: Mappable {
    var name: String?
    var age: Int?
    var email: String?

    required init?(map: Map) {}

    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        email <- map["email"]
    }
}
```

위의 코드에서 `User` 클래스는 `Mappable` 프로토콜을 채택합니다. `Mappable` 프로토콜은 ObjectMapper에서 사용되는 프로토콜이며, `init?(map: Map)`과 `mapping(map: Map)` 메소드를 구현해야 합니다.

`mapping(map: Map)` 메소드 안에서는 Swift 객체의 프로퍼티와 JSON 데이터 사이의 매핑을 정의합니다. `<-` 연산자를 사용하여 JSON 데이터의 키와 매칭될 Swift 객체의 프로퍼티를 지정할 수 있습니다.

## JSON 데이터를 객체로 변환하기

이제 ObjectMapper를 사용해서 JSON 데이터를 객체로 변환해보겠습니다.

```swift
import ObjectMapper

let json = """
{
  "name": "John Doe",
  "age": 30,
  "email": "johndoe@example.com"
}
"""

if let user = Mapper<User>().map(JSONString: json) {
    print(user.name)  // John Doe
    print(user.age)  // 30
    print(user.email)  // johndoe@example.com
} else {
    print("Failed to parse JSON")
}
```

`Mapper<User>().map(JSONString: json)` 코드를 사용하여 JSON 데이터를 `User` 객체로 변환합니다. 변환에 성공하면, `user` 상수에 변환된 객체가 할당됩니다. 그렇지 않은 경우 `nil`이 반환됩니다.

## 정리

이제 JSON 데이터를 Swift 객체로 변환하는 방법을 알게 되었습니다. ObjectMapper를 사용하면 복잡한 JSON 데이터를 Swift 객체로 변환할 수 있어서 데이터 처리 작업을 더욱 편리하게 진행할 수 있습니다. ObjectMapper에는 이외에도 다양한 기능과 옵션이 있으니, 공식 문서 및 예제를 참고하여 더 자세한 사용법을 익혀보시기 바랍니다.

### 참고 자료

- [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)
- [ObjectMapper 공식 문서](https://github.com/tristanhimmelman/ObjectMapper#objectmapper)